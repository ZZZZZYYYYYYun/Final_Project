
# Title: JPYY Restaurant Location and Size Decision Maker

## Team Member(s): 
Jianshan Yang，Parth Ved，Yanyu Wang，Yun Zhou

# Monte Carlo Simulation Scenario & Purpose:
Nowdays, investors planning to invest in properties often consider various factors before actually picking a property. We are considering Monte Carlo Simulation for Resturant owner and what would be the best location for them to open a new resturant. The main purpose of the project is to determine which location would yeild more profit and in turn is a better location. We also ask the owner for the resturant size preference and based on it, we would provide the result. 

In this project, we are trying to simulate the weekly profit of restaurants in different locations.
We choose two places, one is a restaurant closer to the campus area of a University (for example Green Street, Champaign, Illinois), and another at some distance from the campus area of the city (For example, Savoy, Champaign, Illinois). For the restaurant in the campus area, there may be a lot of people during weekdays, nevertheless, the number of customers on weekends may be less. For the restaurant in Savoy, there may be more customers on weekends than during weekdays. Based on this situation, we decide to calculate the weekly profits that each restaurant may make and decide which place is better to run a restaurant.

The process of our analysis is top-down.

1.	Profit = Income – Expenses

Usually the profit is represented as this equation. In our project, we suppose that the only expense related to our project is the rental fee. Rental fee depends on the size of the restaurant. Hence, we simplify the profit to be related to the profit of each person and rental fee.

And we get this equation:

2.	Profit = Profit Per Person – Rental Fee

The process for a customer in a restaurant is decided as:
Wait in line(optional), order, decide to go or in restaurant, eating time (if dining at the restaurant).
Under this situation, we decide these factors: 
(1) Wait time, 
(2) Dining time, 
(3) Total number of tables in the resturant(depends on the size of the restaurant), 
(4) Total number of resturants,
(5) Number of customers per minute during specific period (noon, evening).
These factors will determine the profit together.


## Simulation's variables of uncertainty
We assume we have two options for the restaurant. The location will cause two different pseudo-random variables, one is the total number of customers and the other one is profit we get from every customer. The third variable we get is dinning time for every customer. 

* Total number of customers: For this variable, we built a function as generator to get how many customers we will have and how they distribution. We set the open time from 11:00AM to 2:00PM, for every minute, the max customers is 5, min customers is 0, and on most occasions customer count is 2. Base on the PERT distribution, we can get a serial array to get how many customers the resturant could accomodate during this time. We distributed the customers as a PERT distribution from 11:00 AM to 2:00PM and the most customers visit at 12:00PM.

* Dining time: This variable is used to check if the restaurant table is avaiable. We set the range as 0 to 40, less than 3 means the customer come for picking up. They won't use the table. We set highest frequency time as 15. So this will be another PERT distribution. 

* Profit: This variable is for each customer. We assume it's a normal distribution, while the min value is 1 and max value is 4. 

## Hypothesis or hypotheses before running the simulation:
1.	We assume that the two places we choose are different between weekdays and weekends. This hypothesis will make these two places typical.

2.	Customers will prefer to spend more time on dinner than lunch.

3.	The profit (per person) will be more for dinner than for lunch.

4.	The rental fee only related to the location and the area it has.

5.	The time customers spend in the restaurants will be in a range we set.


## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

## All Sources Used:
【1】Kimes, Sheryl E., Jochen Wirtz, and Breffni M. Noone. "How long should dinner take? Measuring expected meal duration for restaurant revenue management." Journal of Revenue and Pricing Management 1.3 (2002): 220-233.

【2】Dorr, John A. "Restaurant management information and control method and apparatus." U.S. Patent No. 4,530,067. 16 Jul. 1985.

We search the information about the Business Model of restuarants and could calculate the number of people come to the restaurants. We also know the longest time they would like to wait in a restaurant.
