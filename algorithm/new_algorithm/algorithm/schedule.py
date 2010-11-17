#!/usr/bin/python

#Author: Benjamin Ross
#Date: 11/15

"""
This is the schedule class, used to schedule the classes.
The schedule is a list of lists of chromosomes
The length of the list is the number of rooms*number of days*number of hours

Each chromosome has a fitness, which is determined like this:
If the class uses a spare room, fitness++
If the room has enough seats for the class, fitness++
If the class needs a lab and the room has a lab, fitness++
If the professor teaching the class does not have an overlapping class, fitness++

The algorithm is run, until the total fitness is = 1.0
Total fitness = combined fitness/number of rooms * 4(best fitness)

Crossovers are where two schedules are combined at two random points, taking the best chromosomes from either of the schedules

Mutations are where a chromosome is selected at random and moved to a random location

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


class Schedule:
    """
    As described above. This is the representation of the schedule
    """
    def __init__(self,len_chromo_list = None, config = None):
        """
        Initalizes the schedule
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

                    #No class is schedule in that time slot    
                    if self.chromo_list[rand] is None:
                        new_list = [Chromosome()]
                        new_chromo = new_list[0]
                        self.chromo_list.insert(rand,new_list)
                        self.hash_map[new_chromo] = rand
                    #Class is already scheduled in the time slot
                    else:
                        overlap = true
                        exist_list = self.chromo_list[rand]
                        exist_list.append(Chromosome())
                        new_chromo = exist_list[-1]
                        self.chromo_list[rand] = exist_list
                        self.hash_map[new_chromo] = rand

                    #Assigns the class to the new chromosome
                    new_chromo._class = classes
                    self.calculate_fitness(new_chromo,overlap,rand)
                    total_dir += 1
            
    
    def calulate_fitness(self,chromo,overlap,index):
        """
        Calculates the fitness of a chromosome
        """
        hold_index = index
        room_id = index % self.config.get_num_rooms()
        room = self.config.get_room_by_id(room_id)

        course = chromo.course
        #Course might not overlap at current position, but could if duration is longer than 1, this checks for that
        if not overlap:
            if course.duration > 1:
                count = 0
                while count < (course.duration):
                    index += count
                    check_list = self.chromo_list[index]
                    if check_list:
                        overlap = True
                    count += 1

        #Class does not overlap EVER
        if not overlap:
            course.fitness += 1

        #Room is able to fit the class
        if course.get_room_size() <= room.get_seat_num():
            course.fitness += 1

        #Course needs lab and room has lab
        if course.needs_lab():
            if room.lab_status():
                course.fitness += 1

        #Course doesnt need lab and room doesnt have lab
        if not course.needs_lab():
            if not room.lab_status():
                course.fitness += 1

        #Only way a Professor will have an overlapping class is if the class overlaps with another class
        if overlap:
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
                course.fitness += 1
        else:
            course.fitness += 1


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
        Performs a crossover(defined above) between two schedules
        """
        temp_schedule = Schedule()
        temp_schedule.get_config()
        temp_schedule.init_chromosomes()

        count = start_index
        while count <= end_index:
            cur_chromo_list = self.chromo_list[count]



    def perform_mutations(self):
        """
        Performs mutations(defined above) on a schedule, based on tmutation size
        """
        count = 0
        randm.seed()
        for count < self.mutation_size:
            old_spot = random.randint(0,len(self.chromo_list))
            new_spot = random.randint(0,len(self.chromo_list))

            rand_class = random.randint(0,self.config.get_num_classes())
            
