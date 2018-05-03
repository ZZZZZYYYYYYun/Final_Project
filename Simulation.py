'''
Final project
'''

import numpy as np
import random


class ArrayGen():

    '''
    This is the generator to get the customers want to come to our restaurant during the open hours.
    >>> a = ArrayGen(0,2,5,180)
    >>> customers = customerGen(a.arr,0,60,180,180)
    >>> customers
    '''

    def __init__(self,low,likly,high,sample,confidence=4):
        self.low = low
        self.high = high
        self.likely = likly
        self.sample = sample
        self.confidence = confidence
        self.arr = mod_pert_random(self.low,self.likely,self.high,self.sample)


def mod_pert_random(low, likely, high,samples,confidence=4):
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
    confidence = min(8, confidence)
    confidence = max(2, confidence)

    mean = (low + confidence * likely + high) / (confidence + 2)

    a = (mean - low) / (high - low) * (confidence + 2)
    b = ((confidence + 1) * high - low - confidence * likely) / (high - low)

    beta = np.random.beta(a, b, samples)
    beta = beta * (high - low) + low
    return beta


def customerGen(array,start,mostly,end,bins):
    '''
    This function is used to generate the customers distribution every period. we will get a list for this funciton
    the value 
    :param array: the array represent customers come distribution
    :param start: start time
    :param mostly: the time most of customers appeared
    :param end: end time
    :param bins: how many check period
    :return: a list represents how many customers visit the restaurant every check period
    '''
    total_c = int(round(array.sum()))
    beta1 = mod_pert_random(start, mostly, end, samples=total_c)
    counts, bin_edges = np.histogram(beta1, bins)
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


def check_table(table):
    '''
    The function used to check how many tables are available for your customers
    :param table: a list contains our list to represent our tables, if the element is 0, which means the table is available.
    otherwise it's unavailable and until the time run out.
    :return: how many are the tables available now
    '''
    counter = 0
    for i in table:
        if i == 0:
            counter = counter + 1
    return counter

def table_time(table,check_time):
    '''
    This function used to update our tables statues by every period. The period can be set by ourselves.
    :param table: the list which represent our table status
    :param check_time: the period we used to do one time check
    :return: a new table represent every update.
    '''
    new_table = []
    for i in table:
        i = i - check_time
        if i > 0:
            new_table.append(i)
        else:
            i = 0
            new_table.append(i)
    return new_table

def check_inq(inque,limit):
    '''
    this function use to represent some of the customers will leave when the number of queue hit a special number, the
    limit number can be modified by the users.
    :param inque: how many customers in the queue supports to be
    :param limit: if the numbers of queue more than the limit number, some customers after limit number will leave
    :return: a int number represent real time customers in queue.
    '''
    if inque > limit:
        inque = limit + random.randrange(inque-limit)
    else:
        inque = inque
    return inque

def pair_c(n,lst,check_time,limit,arry):
    '''
        this function used to calculate the how many customers we support to have, and how many customers we finally get.
    :param n: the tables of positions we have in our restaurant, it can represent the size of restaurant
    :param lst: the lst
    :param limit: the number define the max customers in the queue,(if customers more than this number, some customers
    will leave)
    :return: a list contains the customers we support to have if we get enough positions for them and a actual number of
    customers we got.
    '''
    support_cust = sum(lst)
    a = iter(arry)
    inque, num_c = 0,0
    table = [0] * n
    for i in range(len(lst)):
        table = table_time(table,check_time)
        ava_table = check_table(table)
        inque = inque + lst[i]  # how many customer comes in
        inque = check_inq(inque,limit)
        # print('Minute:', i + 1, '------')
        if inque < ava_table:  # all the customers can get a table
            for i in range(inque):  # assign tables to all the customers
                time = next(a)
                time = int(round(time))
                #             print('time',time)
                #             print(table)
                if time < 4:
                    inque = inque - 1
                    num_c = num_c + 1
                for j in range(len(table)):
                    if table[j] == 0:  # the table is avaiable
                        table[j] = time
                        break
            num_c = num_c + inque
            inque = 0
        else:  # the customers more than avaiable table
            inque = inque - ava_table  # inque is waiting people, and fill in the customers get in
            for i in range(ava_table):
                time = next(a)
                time = int(round(time))
                if time < 4:
                    inque = inque - 1
                    num_c = num_c + 1
                else:
                    for j in range(len(table)):
                        if table[j] == 0:  # the table is avaiable
                            table[j] = time
                            break
            num_c = num_c + ava_table
    return [support_cust, num_c]

# we set the restaurant owned 40 positions, and the queue limitation is 15.

# simulation the restaurant on green street. assume that there will be a lot of customers from Monday to Friday, but less
# customers on weekend. So the restaurant will open from Monday to Friday and one day of weekend.
# Weekday - lunch time:
def a_location():
    month_income = 0
    for i in range(4):
        openday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        week_income = 0
        for i in openday:
            if i is not 'Saturday':
                # customers for lunch
                a = ArrayGen(0,2,5,180) # customers for 3 hours, generator works every minute from 0 - 5, while 2 has highest frequence.
                noon_customers = customerGen(a.arr,0,60,180,180)
                stay_time = mod_pert_random(0, 15, 40, samples=1000)
                customers_list = pair_c(40,noon_customers,1,15,stay_time)
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i,'lunch time---------------')
                profit = mod_pert_random(0.5,2,10,1000)
                noon_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited,'visited',customers_served,'served',lose_customers,'customers left')
                # print('The income is about',noon_income)
                # customers for dinner
                a = ArrayGen(0,2,5,100) # customers for 5 hour, generator works every three minutes from 0 - 5
                night_customers = customerGen(a.arr,0,30,100,100)
                stay_time = mod_pert_random(0,40,90,samples=800)
                customers_list = pair_c(40,night_customers,3,15,stay_time)
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i, 'dinner time---------------')
                profit = mod_pert_random(2, 5, 20, 1000)
                night_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited, 'visited', customers_served, 'served', lose_customers, 'customers left')
                # print('The income is about', night_income)
                day_income = noon_income + night_income
                week_income = week_income + day_income
            else:
                # we assume on weekend we only get 1/3 customers of weekday
                # customers for lunch
                a = ArrayGen(0,2,5,60) # customers for 3 hours, generator works every minute from 0 - 5, while 2 has highest frequence.
                noon_customers = customerGen(a.arr,0,20,60,60)
                stay_time = mod_pert_random(0, 15, 40, samples=1000)
                customers_list = pair_c(40,noon_customers,1,15,stay_time)
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i,'lunch time---------------')
                profit = mod_pert_random(0.5,2,10,1000)
                noon_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited,'visited',customers_served,'served',lose_customers,'customers left')
                # print('The income is about',noon_income)
                # customers for dinner
                a = ArrayGen(0,2,5,100) # customers for 5 hour, generator works every three minutes from 0 - 5
                night_customers = customerGen(a.arr,0,30,100,100)
                stay_time = mod_pert_random(0,40,90,samples=800)
                customers_list = pair_c(40,night_customers,3,15,stay_time)
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i, 'dinner time---------------')
                profit = mod_pert_random(2, 5, 20, 1000)
                night_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited, 'visited', customers_served, 'served', lose_customers, 'customers left')
                # print('The income is about', night_income)
                day_income = noon_income + night_income
                week_income = week_income + day_income
        month_income = month_income + week_income
        # print(month_income)
    month_profit = month_income - 2 * 5000 - 2 * 3000 - 10000
        # month profit = month income - chef's salary - server's salary - rental
    return month_profit

# we set the restaurant owned 60 positions, and the queue limitation is 20.
# location b got large size, so need 1 more server(lower salary) and more rental
# simulation the restaurant on green street. assume that there will be a lot of customers from Monday to Friday, but less
# customers on weekend. So the restaurant will open from Monday to Friday and one day of weekend.
# Weekday - lunch time:

def b_location():
    month_income = 0
    for i in range(4):
        openday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        week_income = 0
        for i in openday:
            if i is not 'Saturday':
                # customers for lunch
                a = ArrayGen(0,2,5,180) # customers for 3 hours, generator works every minute from 0 - 5, while 2 has highest frequence.
                noon_customers = customerGen(a.arr,0,60,180,180)
                stay_time = mod_pert_random(0, 15, 40, samples=1000)
                customers_list = pair_c(60,noon_customers,1,18,stay_time)
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i,'lunch time---------------')
                profit = mod_pert_random(0.5,2,10,1000)
                noon_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited,'visited',customers_served,'served',lose_customers,'customers left')
                # print('The income is about',noon_income)
                # customers for dinner
                a = ArrayGen(0,2,5,100) # customers for 5 hour, generator works every three minutes from 0 - 5
                night_customers = customerGen(a.arr,0,30,100,100)
                stay_time = mod_pert_random(0,40,90,samples=800)
                customers_list = pair_c(60,night_customers,3,18,stay_time)
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i, 'dinner time---------------')
                profit = mod_pert_random(2, 5, 20, 1000)
                night_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited, 'visited', customers_served, 'served', lose_customers, 'customers left')
                # print('The income is about', night_income)
                day_income = noon_income + night_income
                week_income = week_income + day_income
            else:
                # we assume on weekend we only get 1/3 customers of weekday
                # customers for lunch
                a = ArrayGen(0,2,5,60) # customers for 3 hours, generator works every minute from 0 - 5, while 2 has highest frequence.
                noon_customers = customerGen(a.arr,0,20,60,60)
                stay_time = mod_pert_random(0, 15, 40, samples=1000)
                customers_list = pair_c(60,noon_customers,3,18,stay_time)
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i,'lunch time---------------')
                profit = mod_pert_random(0.5,2,10,1000)
                noon_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited,'visited',customers_served,'served',lose_customers,'customers left')
                # print('The income is about',noon_income)
                # customers for dinner
                a = ArrayGen(0,2,5,100) # customers for 5 hour, generator works every three minutes from 0 - 5
                night_customers = customerGen(a.arr,0,30,100,100)
                stay_time = mod_pert_random(0,40,90,samples=800)
                customers_list = pair_c(60,night_customers,3,18,stay_time)
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i, 'dinner time---------------')
                profit = mod_pert_random(2, 5, 20, 1000)
                night_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited, 'visited', customers_served, 'served', lose_customers, 'customers left')
                # print('The income is about', night_income)
                day_income = noon_income + night_income
                week_income = week_income + day_income
        month_income = month_income + week_income
        # print(month_income)
    month_profit = month_income - 2 * 5000 - 3 * 2500 - 15000
    # month profit = month income - chef's salary - server's salary - rental
    return month_profit

# location c is a place a little bit different than location a, we assumed it's in Savoy Plaza. It owns same size with
# location a. this location owns less customers for lunch. but due to less competent, they owns more profits from each
# customers.

def c_location():
    month_income = 0
    for i in range(4):
        openday = ['Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        week_income = 0
        for i in openday:
            if i not in ['Saturday','Sunday']:
                # customers for lunch
                a = ArrayGen(0,2,5,60) # customers for 3 hours, generator works every three minutes from 0 - 5, while 2 has highest frequence.
                noon_customers = customerGen(a.arr,0,15,60,60)
                stay_time = mod_pert_random(0, 15, 40, samples=1000)
                customers_list = pair_c(40,noon_customers,3,15,stay_time)
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i,'lunch time---------------')
                profit = mod_pert_random(0.5,3,12,1000)
                noon_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited,'visited',customers_served,'served',lose_customers,'customers left')
                # print('The income is about',noon_income)
                # customers for dinner
                a = ArrayGen(0,2,5,100) # customers for 5 hour, generator works every three minutes from 0 - 5
                night_customers = customerGen(a.arr,0,30,100,100)
                stay_time = mod_pert_random(0,40,90,samples=800)
                customers_list = pair_c(40,night_customers,3,15,stay_time)
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i, 'dinner time---------------')
                profit = mod_pert_random(3, 6, 20, 1000)
                night_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited, 'visited', customers_served, 'served', lose_customers, 'customers left')
                # print('The income is about', night_income)
                day_income = noon_income + night_income
                week_income = week_income + day_income
            else:
                # we assume on weekend we only get 1/3 customers of weekday
                # customers for lunch
                a = ArrayGen(0,2,5,60) # customers for 3 hours, generator works every minute from 0 - 5, while 2 has highest frequence.
                noon_customers = customerGen(a.arr,0,20,60,60)
                stay_time = mod_pert_random(0, 15, 40, samples=1000)
                customers_list = pair_c(40,noon_customers,3,15,stay_time)
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i,'lunch time---------------')
                profit = mod_pert_random(0.5,2,10,1000)
                noon_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited,'visited',customers_served,'served',lose_customers,'customers left')
                # print('The income is about',noon_income)
                # customers for dinner
                a = ArrayGen(0,2,5,150) # customers for 5 hour, generator works every two minutes from 0 - 5
                night_customers = customerGen(a.arr,0,30,150,150)
                stay_time = mod_pert_random(0,40,90,samples=800)
                customers_list = pair_c(40,night_customers,2,15,stay_time) # check every two minutes
                customers_visited = customers_list[0]
                customers_served = customers_list[1]
                # print(i, 'dinner time---------------')
                profit = mod_pert_random(3, 6, 20, 1000)
                night_income = round(sum(profit[:customers_served]))
                lose_customers = customers_visited - customers_served
                # print(customers_visited, 'visited', customers_served, 'served', lose_customers, 'customers left')
                # print('The income is about', night_income)
                day_income = noon_income + night_income
                week_income = week_income + day_income
        month_income = month_income + week_income
        # print(month_income)
    month_profit = month_income - 2 * 5000 - 2 * 3000 - 6000
        # month profit = month income - chef's salary - server's salary - rental
    return month_profit

# The main program is run the simulation for 500 times and counter which location get max profits for highest times.

def main():
    counter = {'a':0,'b':0,'c':0}
    simulation_times = 500
    for i in range(simulation_times):
        dic = {}
        dic['a'],dic['b'],dic['c'] = a_location(),b_location(),c_location()
        result = max(dic, key=dic.get)
        counter[result] = counter[result] + 1
        print(counter)
    print('Location A has','{:.1%}'.format(counter['a']/simulation_times),'possibilities to get max profits')
    print('Location B has','{:.1%}'.format(counter['b']/simulation_times),'possibilities to get max profits')
    print('Location C has','{:.1%}'.format(counter['c']/simulation_times),'possibilities to get max profits')

main()
