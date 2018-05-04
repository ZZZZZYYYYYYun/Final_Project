
# Title: JPYY Restaurant Location and Size Decision Maker

## Team Member(s): 
Jianshan Yang，Parth Ved，Yanyu Wang，Yun Zhou

# Monte Carlo Simulation Scenario & Purpose:
Nowdays, investors planning to invest in properties often consider various factors before actually picking a property. We are considering Monte Carlo Simulation for resturant owner and what would be the best location for them to open a new resturant. The main purpose of the project is to determine which location would yeild more profit and in turn is a better location. We also ask the owner for the resturant size preference and based on it, we would provide the result. 

In this project, we are trying to simulate the monthly profit of restaurants in different locations.
We choose three different locations, one is a restaurant closer to the campus area of a University (for example Green Street, Champaign, Illinois), and the second one is at same area, but get larger size than first one. The last location has a little distance from the campus area of the city (For example, Savoy, Illinois). For the restaurant in the campus area, there may be a lot of people during weekdays, nevertheless, the number of customers on weekends may be less. For the restaurant in Savoy, there may be more customers on weekends than during weekdays. Based on this situation, we decide to calculate the monthly profits that each restaurant may make and decide which location is the best choice for a restaurant area.

The process of our analysis is top-down.

1.	Profit = Income – Expenses

Usually the profit is represented as this equation. In our project, we suppose that the expense related to our project are the rental fee and salary for chef and servers.. Rental fee depends on the size of the restaurant. Hence, we simplify the profit to be related to the sum profit of each customers.

And we get this equation:

2.	Profit = Sum(Profit Per Person) – Rental Fee - chef number * chef's salary - server number * server's salary

The process for a customer in a restaurant is decided as:
Wait in line, order, decide to go or in restaurant, eating time (if dining at the restaurant).
Under this situation, we decide these factors: 
(1) Wait time, 
(2) Dining time, 
(3) Total number of tables in the resturant(depends on the size of the restaurant), 
(4) Total number of resturants,
(5) Number of customers per minute during specific period (noon, evening).
These factors will determine the profit together.


## Simulation's variables of uncertainty
We assume we have three options for the restaurant. The location will cause two different pseudo-random variables, one is the total number of customers and the other one is profit we get from every customer. The third variable we get is dinning time for every customer. 

* Location A(busy place during weekday: 40 tables, max queue 15, 2 chef, 2 servers)
    * Open: Mon - Sat
        * Mon - Fri (lunch time): 11am - 2pm(180 mins)
            * Customer distribution: 0-5 per min, 2 has the highest frequency. 
            * Stay time: 0 - 40 mins, 15 has the highest frequency.
            * From 0 - 180 min, the fastigium appears around 60, which means 12am.
            * Profit from each customer: 0.5 - 10 per customer, 2 has the highest frequency.
        * Mon - Fri (dinner time): 5pm - 10pm(300 mins)
            * Customer distribution: 0-5 per 3 mins, 2 has the highest frequency. 
            * Stay time: 0 - 90 mins, 40 has the highest frequency.
            * From 0 - 300 min, the fastigium appears around 90, which means 6:30pm.
            * Profit from each customer: 2 - 20 per customer, 5 has the highest frequency.
        * Sat (lunch time): 11am - 2pm(180 mins)
            * Customer distribution: 0-5 per 3 mins, 2 has the highest frequency. 
            * Stay time: 0 - 40 mins, 15 has the highest frequency.
            * From 0 - 180 min, the fastigium appears around 60, which means 12am.
            * Profit from each customer: 0.5 - 10 per customer, 2 has the highest frequency.
        * Sat (dinner time): 5pm - 10pm(300 mins)
            * Customer distribution: 0-5 per 3 mins, 2 has the highest frequency. 
            * Stay time: 0 - 90 mins, 40 has the highest frequency.
            * From 0 - 300 min, the fastigium appears around 90, which means 6:30pm.
            * Profit from each customer: 2 - 20 per customer, 5 has the highest frequency.

* Location B(busy place during weekday: 60 tables, max queue 18, 2 chef, 2 or 3 servers)
    * Open: Mon - Sat
        * Mon - Fri (lunch time): 11am - 2pm(180 mins)
            * Customer distribution: 0-5 per min, 2 has the highest frequency. 
            * Stay time: 0 - 40 mins, 15 has the highest frequency.
            * From 0 - 180 min, the fastigium appears around 60, which means 12am.
            * Profit from each customer: 0.5 - 10 per customer, 2 has the highest frequency.
        * Mon - Fri (dinner time): 5pm - 10pm(300 mins)
            * Customer distribution: 0-5 per 3 mins, 2 has the highest frequency. 
            * Stay time: 0 - 90 mins, 40 has the highest frequency.
            * From 0 - 300 min, the fastigium appears around 90, which means 6:30pm.
            * Profit from each customer: 2 - 20 per customer, 5 has the highest frequency.
        * Sat (lunch time): 11am - 2pm(180 mins)
            * Customer distribution: 0-5 per 3 mins, 2 has the highest frequency. 
            * Stay time: 0 - 40 mins, 15 has the highest frequency.
            * From 0 - 180 min, the fastigium appears around 60, which means 12am.
            * Profit from each customer: 0.5 - 10 per customer, 2 has the highest frequency.
        * Sat (dinner time): 5pm - 10pm(300 mins)
            * Customer distribution: 0-5 per 3 mins, 2 has the highest frequency. 
            * Stay time: 0 - 90 mins, 40 has the highest frequency.
            * From 0 - 300 min, the fastigium appears around 90, which means 6:30pm.
            * Profit from each customer: 2 - 20 per customer, 5 has the highest frequency.

* Location C(busy place during weekend and night: 40 tables, max queue 15, 2 chef, 2 servers)
    * Open: Tue - Sun
        * Tue - Fri (lunch time): 11am - 2pm(180 mins)
            * Customer distribution: 0-5 per 3 mins, 2 has the highest frequency. 
            * Stay time: 0 - 40 mins, 15 has the highest frequency.
            * From 0 - 180 min, the fastigium appears around 60, which means 12am.
            * Profit from each customer: 0.5 - 12 per customer, 3 has the highest frequency.
        * Tue - Fri (dinner time): 5pm - 10pm(300 mins)
            * Customer distribution: 0-5 per 3 mins, 2 has the highest frequency. 
            * Stay time: 0 - 90 mins, 40 has the highest frequency.
            * From 0 - 300 min, the fastigium appears around 90, which means 6:30pm.
            * Profit from each customer: 3 - 20 per customer, 6 has the highest frequency.
        * Sat - Sun (lunch time): 11am - 2pm(180 mins)
            * Customer distribution: 0-5 per 3 mins, 2 has the highest frequency. 
            * Stay time: 0 - 40 mins, 15 has the highest frequency.
            * From 0 - 180 min, the fastigium appears around 60, which means 12am.
            * Profit from each customer: 0.5 - 10 per customer, 2 has the highest frequency.
        * Sat - Sun (dinner time): 5pm - 10pm(300 mins)
            * Customer distribution: 0-5 per 2 mins, 2 has the highest frequency. 
            * Stay time: 0 - 90 mins, 40 has the highest frequency.
            * From 0 - 300 min, the fastigium appears around 90, which means 6:30pm.
            * Profit from each customer: 2 - 20 per customer, 5 has the highest frequency.           
## Hypothesis or hypotheses before running the simulation:
1.	We assume that the a,b and c location we choose are different between weekdays and weekends. This hypothesis will make these three location typical.

2.  Every customer will use one individually.

3.	Customers will prefer to spend more time on dinner than lunch.

4.  Customers may leave randomly if the line hit the limit value.

5.	The profit (per person) will be more for dinner than for lunch.

6.	The rental fee only related to the location and the area it has.

7.	The time customers spend in the restaurants will be in a range we set.


## Analytical Summary of findings:
* We simulation the scenario 500 times, and find location A is the best.
* We adjust the scenario, to make location B only have 2 servers, location B is the best
## Instructions on how to use the program:
Download the Simulation.py and run.
The parameter simulation_time can be changed. The more time we simulate, the higher accuracy we should get.
## Future work:
In this program, most of paramters are revisable, which means this program can be used to any place if users want to use for another place. Next step will be modified the program to let the user to enter their data, simulate the scenario for them.
## All Sources Used:
【1】Kimes, Sheryl E., Jochen Wirtz, and Breffni M. Noone. "How long should dinner take? Measuring expected meal duration for restaurant revenue management." Journal of Revenue and Pricing Management 1.3 (2002): 220-233.

【2】Dorr, John A. "Restaurant management information and control method and apparatus." U.S. Patent No. 4,530,067. 16 Jul. 1985.

We search the information about the Business Model of restuarants and could calculate the number of people come to the restaurants. We also know the longest time they would like to wait in a restaurant.
