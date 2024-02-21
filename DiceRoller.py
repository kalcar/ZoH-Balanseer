import random
import math
import itertools




class Dicetower():

    def __init__(self, *dice):
        self.diestack = self.Diestack(*dice)

        self.aux_diestack = []

        # Not calculated on initalization because its expensive to do so currently
        self.prob_dist = None 

    def add_stack(self, *dice):
        self.aux_diestack.append(self.Diestack(*dice))


    class Diestack():

        def __init__(self,*dice):
            self.dice = list(dice)
            self.face_array = []
            self.average_roll = 0.0
            self.min = 0
            self.max = 0
            for item in self.dice:
                self.face_array.append(item.face_array)
                self.average_roll += item.avg
                self.min += item.min
                self.max += item.max

            self.stddev = self.calc_stddev()


        def get_face_array(self):
            return self.face_array
        
        def roll(self):
            sum = 0
            for die in self.dice:
                sum += die.roll()
            return sum
        
        def get_average_roll(self):
            return self.average_roll
        
        def get_min_roll(self):
            return self.min
        
        def get_max_roll(self):
            return self.max
        
        def calc_stddev(self): # add to stack instead of tower
            self.cartesian = list(itertools.product(*self.face_array))
            temp = 0.0
            for item in self.cartesian:
                num = sum(item)-self.average_roll
                num *= num # same as num to the power 2
                temp += num
            temp /= len(self.cartesian)
            stddev = math.sqrt(temp)
            return stddev
        
        def get_stddev(self):
            return self.stddev
        
        def add_die(self, die):
            self.dice.append(die)
            self.face_array.append(die.face_array)
            self.average_roll += die.avg
            self.max += die.max
            self.min += die.min
            self.stddev = self.calc_stddev()

        def remove_die(self, index: int):
            self.average_roll -= self.dice[index].avg
            self.min -= self.dice[index].min
            self.max -= self.dice[index].max
            del self.dice[index]
            del self.face_array[index]
            self.stddev = self.calc_stddev()
        
        def clear(self):
            self.average_roll = 0.0
            self.min = 0
            self.max = 0
            self.dice.clear()
            self.face_array.clear()
            self.stddev = 0.0
            

        def get_dice(self):
            return self.dice

    
    def print_simple_distribution(self):
        print('min:', self.diestack.min)
        print('-2 std. dev. :', self.diestack.average_roll - self.diestack.stddev*2.0 )
        print('-1 std. dev. :', self.diestack.average_roll - self.diestack.stddev )
        print('0 std. dev. :', self.diestack.average_roll)
        print('+1 std. dev. :', self.diestack.average_roll + self.diestack.stddev )
        print('+2 std. dev. :', self.diestack.average_roll + self.diestack.stddev*2.0 )
        print('max:', self.diestack.max)

    def get_simple_distribution(self): # Theres a better way to calc this. 
        return [self.diestack.min, (self.diestack.average_roll - self.diestack.stddev*2.0),(self.diestack.average_roll - self.diestack.stddev),\
                self.diestack.average_roll, (self.diestack.average_roll + self.diestack.stddev)\
                    , (self.diestack.average_roll + self.diestack.stddev*2.0), self.diestack.max ]
    
    def calc_prob_dist(self):
        possible_rolls = itertools.product(*self.diestack.get_face_array())
        possible_values = []
        value_occurrences = {}
        value_probability = {}

        for possible_roll in possible_rolls:
            possible_values.append(sum(possible_roll))

        for value in possible_values:
                value_occurrences[value] = value_occurrences.get(value, 0) + 1

        total_occurrences = sum(value_occurrences.values())
        for key, number in value_occurrences.items():
            value_probability[key] = number / total_occurrences

        # Store it so it doesn't have to be calculated every time
        self.prob_dist = value_probability

        return value_probability
    
    def get_prob_dist(self):
        if self.prob_dist:
            return self.prob_dist
        else:
            return "Probability distribution not calculated yet."

        




class Die():
    
    def __init__(self, sides):
        self.sides = sides
        self.min = 1
        self.max = sides
        self.avg = (sides/2.0) + 0.5
        self.stddev = math.sqrt(((sides * sides) - 1)/12)
        self.face_array = list(range(1 , sides + 1))

    def roll(self):
        return random.randrange(1, self.sides + 1)

def mod_to_dice(num : int):
    d12s = num/5 # this drops the decimcal, so its always floored
    remainder = num % 5
    match remainder:
        case 0:
            pass
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass

