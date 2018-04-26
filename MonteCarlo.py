'''
Final project: Monte Carlo Simulation for restaurant location
'''

import random
import numpy as np

class Randomvar:

    '''
    This is the class to hold all the random variables. it contains the base number, the fluctuate range of the variables
    and the conditions. In this class all the variables are uniform distribution.
    >>> people = Randomvar(48744,0.08,0.12)
    >>> people.base
    48744
    >>> people.range
    [0.08, 0.12]
    '''

    def __init__(self,base,min=1,max=1):
        self.base = base
        self.min = min
        self.max = max
        self.range = [min,max]
        self.num = self.value()


    def value(self):
        value = random.uniform(self.min,self.max) * self.base
        value = round(value)
        return value


class RandomvarP:
    '''
    In this class, all the variables are modified PERT distribution.
    '''

    def __init__(self,low,likely,high,confidence=2):
        self.low = low
        self.likely = likely
        self.high = high
        self.confidence = confidence
        self.num = self.value()

    def value(self):
        '''
        This function return the value of a number of modified PERT distribution.
        :return:
        '''
        confidence = min(4,self.confidence)
        confidence = max(1,confidence)

        mean = (self.low + confidence * self.likely + self.high) / (confidence + 2)

        a = (mean - self.low)/(self.high - self.low) * (confidence + 2)
        b = ((confidence + 1) * self.high - self.low - confidence * self.likely) / (self.high - self.low)

        beta = random.betavariate(a,b)
        beta = beta * (self.high - self.low) + self.low

        return  beta


# first location for restaurant
# get all the variables

# act people around our restaurant location from monday to friday
act_people = Randomvar(48744,0.08,0.12).num

# the rate from act people to customers
customer_rate = Randomvar(1,0.05,0.10).num

# profit for each person
one_profit = RandomvarP(1,2,4).num

#  people around our restaurant location on Sat or Sun (one day break here)
act_peopled = Randomvar(48744,0.03,0.07).num
# the rate from act people to customers
customer_rated = Randomvar(1,0.07,0.12).num

# profit for each person
one_profitd = RandomvarP(1,2,4).num




# second location for restaurant
# get all the variables

# act people around our restaurant location from monday to friday (one day break)
act_people2 = Randomvar(1000,0.7,1.2).num

# the rate from act people to customers
customer_rate2 = Randomvar(1,0.12,0.18).num

# profit for each person
one_profit2 = RandomvarP(2,3,5).num

#  people around our restaurant location on Sat and Sun
act_peopled2 = Randomvar(1000,1,1.8).num

# the rate from act people to customers
customer_rated2 = Randomvar(1,0.15,0.22).num

# profit for each person
one_profitd2 = RandomvarP(2,3,5).num

for i in range(10000):
    counter = 0
    result1 = act_people * customer_rate * one_profit * 5 + act_peopled * customer_rated * one_profitd
    result2 = act_people2 * customer_rate2 * one_profit2 * 4 + act_peopled2 * customer_rated2 * one_profitd2
    result = result1 -result2
    if result < 0:
        counter = counter + 1

print(counter)
print(counter/10000)



# complex added

class PeopleR():

    '''
    The class to hold all the customers here.
    '''

    def __init__(self, low, likely, high, start, end, mostly, confidence=2):
        self.low = low
        self.likely = likely
        self.high = high
        self.confidence = confidence
        self.start = start
        self.end = end
        self.mostly = mostly


    def mod_pert_random(self, samples=180):
        """Produce random numbers according to the 'Modified PERT'
        distribution.

        :param low: The lowest value expected as possible.
        :param likely: The 'most likely' value, statistically, the mode.
        :param high: The highest value expected as possible.
        :param confidence: This is typically called 'lambda' in literature
                            about the Modified PERT distribution. The value
                            4 here matches the standard PERT curve. Higher
                            values indicate higher confidence in the mode.

        Formulas from "Modified Pert Simulation" by Paulo Buchsbaum.
        """
        # Check minimum & maximum confidence levels to allow:
        confidence = min(4,self.confidence)
        confidence = max(1,confidence)

        mean = (self.low + confidence * self.likely + self.high) / (confidence + 2)

        a = (mean - self.low)/(self.high - self.low) * (confidence + 2)
        b = ((confidence + 1) * self.high - self.low - confidence * self.likely) / (self.high - self.low)

        beta = np.random.beta(a,b,samples)
        beta = beta * (self.high - self.low) + self.low

        return  beta

    def people_lst(self):
        beta = self.mod_pert_random(self.low, self.likely, self.high, samples=180)
        total = int(round(beta.sum()))
        beta1 = self.mod_pert_random(self.start, self.mostly, self.end, samples=total)
        counts, bin_edges = np.histogram(beta1, bins=180)
        cdf = np.cumsum(counts)
        lst = []
        for i, num in enumerate(list(cdf)):
            if i == 0:
                num = list(cdf)[i]
                lst.append(num)
            else:
                num = list(cdf)[i] - list(cdf)[i - 1]
                lst.append(num)
        return lst