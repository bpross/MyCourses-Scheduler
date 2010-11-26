#!/usr/bin/python

#Author: Benjamin Ross
#Date: 11/15

"""
This is the schedule class, used to schedule the classes.
The schedule is a list of lists of chromosomes
The length of the list is the number of rooms*number of days*number of
hours

Each chromosome has a fitness, which is determined like this:
If the class uses a spare room, fitness++
If the room has enough seats for the class, fitness++
If the class needs a lab and the room has a lab, fitness++
If the professor teaching the class does not have an overlapping class,
fitness++

The algorithm is run, until the total fitness is = 1.0
Total fitness = combined fitness/number of rooms * 4(best fitness)

Crossovers are where two schedules are combined at two random points,
taking the best chromosomes from either of the schedules

Mutations are where a chromosome is selected at random and moved to a
random location

Algorithm Logic:
read in data
initialize chromosome
get_overall_fitness
while overall fitness != 1.0
  get crossover points
  perform crossover
  get mutation size
  perform mutations
  get overall fitness

return schedule
"""

from configuration import Configuration
import random

class Chromosome:
    """
    Used to store the fitness of the class in a certain room
    """
    def __init__(self, _class = None):

        if _class is None:
            self._class = None
        else:
            self._class = _class

        self.fitness = 0
        self.overlap = False

class Schedule:
    """
    This is the schedule class, used to schedule the classes.
    The schedule is a list of lists of chromosomes
    The length of the list is the number of rooms*number of days*number of
    hours
    
    Each chromosome has a fitness, which is determined like this:
    If the class uses a spare room, fitness++
    If the room has enough seats for the class, fitness++
    If the class needs a lab and the room has a lab, fitness++
    If the professor teaching the class does not have an overlapping class,
    fitness++

    The algorithm is run, until the total fitness is = 1.0
    Total fitness = combined fitness/number of rooms * 4(best fitness)
    
    Crossovers are where two schedules are combined at two random points,
    taking the best chromosomes from either of the schedules

    Mutations are where a chromosome is selected at random and moved to a
    random location

    Algorithm Logic:
      read in data
      initialize chromosome
      get_overall_fitness
      while overall fitness != 1.0
      get crossover points
      perform crossover
      get mutation size
      perform mutations
      get overall fitness

      return schedule
      """

    def __init__(self,len_chromo_list = None, config = None):
        """
        Initalizes the schedule
        @param len_chromo_list: length of the new chromosome list
        @param config: config object to base the schedule on
        """
        if len_chromo_list = None:
            self.chromo_list = []
        else:
            self.chromo_list = len_chromo_list*[None]

        if config = None:
            self.config = None
        else:
            self.config = config

        #Holds the last location of every class in the list
        self.hash_map = {}
        #Holds the classes with fitness values of 4
        self.best_of = {}

        #Number of chromosomes to swap
        self.mutation_size = 0
        #Overall fitness of the schedule
        self.total_fitness = 0
        #Hours in the day classes can be held
        self.day_length = 12
        #Days of the week classes can be held
        self.num_days = 5

    def get_config(self):
        """
        Loads the configuration of the classes, courses, rooms and professors
        """
        if self.config is None:
            self.config = Configuration()

        #Hard coded the file for now, will change with Django interface
        self.config.parse_file('config')

    def init_chromosomes(self):
        """
        Initalizes the schedule with random class placement
        """

        #Checks to see chromo_list has a size
        if not self.chromo_list: 
            if self.config is None:
                print "You need to load a config,
                before initalizing chromosomes"

            else:
                self.chromo_list = ((self.day_length*self.num_days)*\
                                   (self.config.get_num_rooms))*[None]
                
        else: #List has size
            random.seed()  #Seeds the random with system time
            for classes in self.classes_list:
                #Gets random spot for class
                rand = random.randint(0,len(self.chromo_list))

                #Used to place classes with long durations
                total_dir = 1 
                #Checks to see if class overlaps with another class
                overlap = false 

                #Places class in schedule
                while total_dir <= classes.duration:
                    if total_dir is > 1:
                        rand += total_dir

                    new_chromo = self.insert_chromosome(None,rand)
                    #Assigns the class to the new chromosome
                    new_chromo._class = classes
                    self.calculate_fitness(new_chromo,rand)
                    total_dir += 1
            
    
    def calulate_fitness(self,chromo,index):
        """
        Calculates the fitness of a chromosome
        @param chromo: chromosome to calculate fitness for
        @param index: index in self.chromo_list of the chromosome
        """
        hold_index = index
        room_id = index % self.config.get_num_rooms()
        room = self.config.get_room_by_id(room_id)

        course = chromo.course
        #Course might not overlap at current position, but could if duration is longer than 1, this checks for that
        if not chromo.overlap:
            if course.duration > 1:
                count = 0
                while count < (course.duration):
                    index += count
                    check_list = self.chromo_list[index]
                    if check_list:
                        chromo.overlap = True
                    count += 1

        #Class does not overlap EVER
        if not chromo.overlap:
            chromo.fitness += 1

        #Room is able to fit the class
        if course.get_room_size() <= room.get_seat_num():
            chromo.fitness += 1

        #Course needs lab and room has lab
        if course.needs_lab():
            if room.lab_status():
                chromo.fitness += 1

        #Course doesnt need lab and room doesnt have lab
        if not course.needs_lab():
            if not room.lab_status():
                chromo.fitness += 1

        #Only way a Professor will have an overlapping class is if the class overlaps with another class
        if chromo.overlap:
            prof_overlap = False
            index = hold_index
            count = 0
            while count < (course.duration):
                index += count
                check_list = self.chromo_list[index]
                for courses in check_list:
                    prof_overlap = course.professor_overlap(courses)
                    if prof_overlap:
                        break
                if prof_overlap:
                    break
                count += 1

            if not prof_overlap:
                chromo.fitness += 1
        else:
            chromo.fitness += 1


    def get_overall_fitness(self):
        """
        Calculates the overall fitness of the schedule
        """
        total_fitness = 0
        for chromosomes in self.chromo_list:
            total_fitness += chromosomes.fitness

        return float(total_fitness/(self.config.get_num_rooms()*4))

    

    def perform_crossover(self,start_index,end_index):
        """
        Performs a crossover:
            Crossovers are where two schedules are combined at two random points,
            taking the best chromosomes from either of the schedules
        @param start_index: index of the hashmap to start the crossover
        @param end_index: index of the hashmap to end the crossover
        """
        temp_schedule = Schedule()
        temp_schedule.get_config()
        temp_schedule.init_chromosomes()
        
        hash_list = temp_schedule.hash_map.items()
        
        while start_index <= end_index:
            swap_tuple = hash_list[start_index]
            swap_chromosome = swap_tuple[0]

            if self.best_of.has_key(swap_chromosome):
                start_index += 1
            else:
                old_position = self.hash_map[swap_chromosome]

                #Delete from old position
                self.remove_chromosome(swap_chromosome,old_position)
                
                #Put in new position
                swap_position = swap_tuple[1]
                #Inserts chromosome into new position
                swap_chromosome = self.insert_chromosome(swap_chromosome,swap_position)
                #Calculates the fitness for the chromosome at the new positon
                self.calculate_fitness(swap_chromosome,swap_position)
                start_index += 1
                
    def perform_mutations(self):
        """
        Performs mutations:
          Mutations are where a chromosome is selected at random and moved to a
          random location
        Based on the mutation size
        """
        count = 0
        randm.seed()
        for count < self.mutation_size:
            old_spot = random.randint(0,len(self.chromo_list))
            new_spot = random.randint(0,len(self.chromo_list))

            rand_class = random.randint(0,self.config.get_num_classes())
            

    def insert_chromosome(self, chromosome = None, index):
        """
        Inserts a chromosome into chromo_list at the given index
        Checks to see if there is over lap or not
        @param chromosome: chromosome to be inserted into the list
        @param index: index where to insert the chromosome
        """
        if chromosome is None:
            #No class is schedule in that time slot    
            if self.chromo_list[index] is None:
                #Create new list with empty chromosome object
                new_list = [Chromsome()]
                #Assigns new_chromo the empty chromosome object
                new_chromo = new_list[0]
                #Inserts the new list into the master chromosome list
                self.chromo_list.insert(index,new_list)
                #Inserts the object and index into the hashmap to know where the class occurs
                self.hash_map[new_chromo] = index
                
            #Class is already scheduled in the time slot
            else:
                #Get the existing list
                exist_list = self.chromo_list[index]
                #Append empty chromosome object to end of list
                exist_list.append(Chromosome())
                #Assigns new_chromo the empty chromosome object
                new_chromo = exist_list[-1]
                #Sets overlap to be true because another class is scheduled at the same time
                new_chromo.overlap = True
                #Reassigns the list in chromo_list
                self.chromo_list[index] = exist_list
                #Inserts the object and index into the hashmap to know hwere the class occurs
                self.hash_map[new_chromo] = index

            #Returns pointer to the inserted chromosome
            return new_chromo

        else:
            #No class is schedule in that time slot    
            if self.chromo_list[index] is None:
                #Inserts the existing chromosome into an empty list
                new_list = [chromosome]
                #Assigns new_chromo to the inserted object
                new_chromo = new_list[0]
                #Inserts the new list into the master chromosome list
                self.chromo_list.insert(index,new_list)
                #Inserts the chromosome and index into the hashmap
                self.hash_map[new_chromo] = index

            #Class is already scheduled in the time slot
            else:
                #Gets the existing list
                exist_list = self.chromo_list[index]
                #Adds the existing chromosome to the end of the existing list
                exist_list.append(chromosome)
                #Assigns new_chromo to the newly inserted chromosome
                new_chromo = exist_list[-1]
                #Inserts the existing list back into the master chromosome list
                self.chromo_list[index] = exist_list
                #Inserts the chromosome and index into the hashmap
                self.hash_map[new_chromo] = index

            #Returns pointer to the chromosome that has been inserted
            return new_chromo


    def remove_chromosome(self,chromosome,index):
        """
        Removes the chromosome from the list at position index
        @param chromosome: chromosome to remove from the list
        @param index: index where the chromosome is located
        """
        #Gets the list at the index
        remove_list = self.chromo_list[index]
        #Uses built in python method to remove chromosome object from list
        remove_list.remove(chromosome)
        #Reassigns the list to the master chromosome list
        self.chromo_list = remove_list
