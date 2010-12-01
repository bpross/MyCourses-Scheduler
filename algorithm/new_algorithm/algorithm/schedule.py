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

    def print_chromo(self):
        self._class.print_course_class()
        print "Fitness" + str(self.fitness)

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
    If the professor teaching the class does not have an overlapping class    ,fitness++

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
        if len_chromo_list is None:
            self.chromo_list = []
        else:
            self.chromo_list = len_chromo_list*[None]

        if config is None:
            self.config = None
        else:
            self.config = config

        #Holds the last location of every class in the list
        self.hash_map = {}
        #Holds the classes with fitness values of 4
        self.best_of = {}

        self.number_chromosomes = 0
        
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
                print "You need to load a config,\
                before initalizing chromosomes"

            else:
                self.chromo_list = ((self.day_length*self.num_days)*\
                                   (self.config.get_num_rooms()))*[None]
                
        #Seeds the random with system time
        random.seed()  
        for classes in self.config.classes_list:
            
            #Gets random spot for class
            rand = random.randint(0,len(self.chromo_list))
            
            #Used to place classes with long durations
            total_duration = 0
            temp_index = rand
            #Places class in schedule
            while total_duration < classes.duration\
                      and temp_index < len(self.chromo_list):
                    new_chromo = self.insert_chromosome(Chromosome(),temp_index)
                    self.number_chromosomes += 1
                    #Checks to see if the class is already in the hashmap, if not
                    #Class object is added with value being location in list.
                    #Only adds when the class starts
                    if not self.hash_map.has_key(classes):
                        self.hash_map[classes] = temp_index

                    #Assigns the class to the new chromosome
                    new_chromo._class = classes
                    self.calculate_fitness(new_chromo,temp_index)
                    total_duration += 1
                    temp_index += 1
            
    
    def calculate_fitness(self,chromo,index):
        """
        Calculates the fitness of a chromosome
        @param chromo: chromosome to calculate fitness for
        @param index: index in self.chromo_list of the chromosome
        """
        #Incase chromosome has been scheduled before
        chromo.fitness = 0
        
        hold_index = index
        data_tuple = self.get_room_day_numbers(hold_index)
        room_id = data_tuple[1]
        room = self.config.get_room_by_id(room_id)
        course = chromo._class
        #Course might not overlap at current position, but could if duration is
        #longer than 1, this checks for that
        if not chromo.overlap:
            if course.duration > 1:
                count = 0
                while count < (course.duration):
                    index += 1
                    if index < len(self.chromo_list):
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
                    prof_overlap = course.professor_overlap(courses._class)
                    if prof_overlap:
                        break
                if prof_overlap:
                    break
                count += 1

            if not prof_overlap:
                chromo.fitness += 1
        else:
            chromo.fitness += 1

        if chromo.fitness is 4:
            self.best_of[chromo._class] = 4


    def get_overall_fitness(self):
        """
        Calculates the overall fitness of the schedule
        """
        total_fitness = 0
        for chromosome_list in self.chromo_list:
            if chromosome_list:
                for chromosomes in chromosome_list:
                    total_fitness += chromosomes.fitness

        return float(total_fitness/(self.number_chromosomes*4.0))

    

    def perform_crossover(self,start_index,end_index):
        """
        Performs a crossover:
            Crossovers are where two schedules are combined at two random points,
            taking the best chromosomes from either of the schedules
        @param start_index: index of the hashmap to start the crossover
        @param end_index: index of the hashmap to end the crossover
        """
        random_schedule = self.randomize_schedule()
        random_hash_list = random_schedule.hash_map.items()
        while start_index < end_index:
            
            swap_tuple = random_hash_list[start_index]
            swap_class = swap_tuple[0]

            if self.best_of.has_key(swap_class):
                start_index += 1

            else:
                old_position = self.hash_map[swap_class]
                total_duration = 0

                while total_duration < swap_class.duration and old_position < len(self.chromo_list):
                    swap_chromosome = self.get_chromosome_from_list(swap_class,old_position)
                    self.remove_chromosome(swap_chromosome,old_position)
                    total_duration += 1
                    old_position += 1
                new_position = swap_tuple[1]
                self.hash_map[swap_class] = new_position
                total_duration = 0

                while total_duration < swap_class.duration and new_position < len(self.chromo_list):
                    new_chromo = self.insert_chromosome(Chromosome(), new_position)
                    new_chromo._class = swap_class
                    self.calculate_fitness(new_chromo, new_position)
                    total_duration += 1
                    new_position += 1

                start_index += 1
                
    def perform_mutations(self):
        """
        Performs mutations:
          Mutations are where a chromosome is selected at random and moved to a
          random location
        Based on the mutation size
        """
        count = 0
        while count < self.mutation_size:
            random_class_index = random.randint(0,len(self.config.classes_list)-1)
            random_class = self.config.classes_list[random_class_index]
            
            new_position = random.randint(0,len(self.chromo_list))

            old_position = self.hash_map[random_class]
            self.hash_map[random_class] = new_position
            total_duration = 0
            while total_duration < random_class.duration and old_position < len(self.chromo_list):
                removal_chromosome = self.get_chromosome_from_list(random_class,old_position)
                self.remove_chromosome(removal_chromosome,old_position)
                total_duration += 1
                old_position += 1

            total_duration = 0
            while total_duration < random_class.duration and new_position < len(self.chromo_list):
                new_chromo = self.insert_chromosome(Chromosome(),new_position)
                new_chromo._class = random_class
                self.calculate_fitness(new_chromo, new_position)
                total_duration += 1
                new_position += 1
            count += 1
            
    def insert_chromosome(self, chromosome, index):
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
                self.chromo_list[index] = new_list

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

        if not remove_list:
            remove_list = None
        #Reassigns the list to the master chromosome list
        self.chromo_list[index] = remove_list


    def get_chromosome_from_list(self,_class,index):
        """
        Returns the chromosome object from the chromo_list at the given
        index that contains the _class. Returns None if not found
        @param _class: class to be searched for in the list
        @param index: index to search for the class
        """
        search_list = self.chromo_list[index]
        #List doesnt exist
        if search_list is None:
            return None
        #List exists
        else:
            search_chromosome = None
            for chromosomes in search_list:
                #Class is found
                if chromosomes._class is _class:
                    search_chromosome = chromosomes
                    break
                #Class is not found
                else:
                    search_chromosome = None
            
            return search_chromosome

    def algorithm(self):
        """
        Runs the schedule algorithm. Flow of algorithm:
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
        #Loads the config for the rooms/classes
        self.get_config()
        #Creates the first chromosome
        self.init_chromosomes()
        self.get_overall_fitness()
        #Seeds the random with system time
        random.seed()
        generations = 1
        while self.get_overall_fitness() < 1.0:
            #Get random points for crossover
            start_crossover = random.randint(0,self.config.get_num_classes())
            end_crossover = random.randint(0,self.config.get_num_classes())

            #Checks to see which crossover point is greater, Dont want to go
            #From a greater value to lesser value
            if start_crossover <= end_crossover:
                self.perform_crossover(start_crossover,end_crossover)
            else:
                self.perform_crossover(end_crossover, start_crossover)

            #Gets random mutation size and performs mutations
            self.mutation_size = random.randint(0,len(self.chromo_list))
            self.perform_mutations()
            generations += 1
            
        print "Done! Took " + str(generations) + " Generations"

    def print_chromosomes(self):
        count = 0
        print "LENGTH: " + str(len(self.chromo_list))
        while count < len(self.chromo_list):
            chromo_list = self.chromo_list[count]
            day_room = self.get_room_day_numbers(count)
            if chromo_list is not None:
                for chromosomes in chromo_list:
                    print "Day: " + str(day_room[0])
                    print "Hour: " + str(count%self.day_length+1)
                    print "Room: " + str(day_room[1])
                    chromosomes.print_chromo()
                    
                    print "\n\n"
            count += 1

    def get_room_day_numbers(self,index):
        """
        Returns a tuple (day_num, room_num) Based on the index given
        @param index: index to find day and room info
        """

        count = self.config.get_num_rooms()*self.day_length
        old_count = 0
        day_num = 1
        found_day = False
        while not found_day:
            if index < count:
                found_day = True
            else:
                old_count = count
                count += self.config.get_num_rooms()*self.day_length
                day_num += 1

        count = self.day_length
        room_num = 1
        found_room = False
        while not found_room:
            old_count += count
            if index < old_count:
                found_room = True
            else:
                room_num += 1

        tuple = (day_num,room_num)
        return tuple

    def randomize_schedule(self):
        """
        Returns a random schedule based on current schedule
        """
        new_schedule = Schedule(len(self.chromo_list),self.config)
        for classes,index in self.hash_map.items():
            rand = random.randint(0,len(new_schedule.chromo_list))
            total_duration = 0
            temp_index = rand
            while total_duration < classes.duration\
                  and temp_index < len(new_schedule.chromo_list):
                new_chromo = new_schedule.insert_chromosome(Chromosome(),temp_index)
                new_schedule.number_chromosomes += 1
                if not new_schedule.hash_map.has_key(classes):
                    new_schedule.hash_map[classes] = temp_index
                new_chromo._class = classes
                new_schedule.calculate_fitness(new_chromo,temp_index)
                total_duration += 1
                temp_index += 1

        return new_schedule
