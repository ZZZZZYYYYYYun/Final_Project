Create a FORK of this repository to store your code, data, and documentation for the final project. Detailed instructions for this assignment are in the course Moodle site.  The reason I'm asking you to fork this empty repository instead of creating a stand-alone repository is that it will be much easier for me and all students in the course to find all of our projects for code review and for grading. You can even get code review from students in the other section of IS590PR this way.

Even though your fork of this repository shall be public, you'll still need to explicitly add any students on your team as Collaborators in the Settings. That way you can grant them write privileges.

DELETE these lines from TEMPLATE up.

TEMPLATE for your report:

# Title: 

## Team Member(s): Jianshan Yang，Parth Ved，Yanyu Wang，Yun Zhou
(Note: Don't put your email addresses here (which is public).  If a student wants their NAME hidden as well, due to optional FERPA regulations, they can be listed purely by their GitHub ID).

# Monte Carlo Simulation Scenario & Purpose:
(be sure to read the instructions given in course Moodle)
Nowdays, investors planning to invest in properties often consider various factors before actually picking a property. We are considering Monte Carlo Simulation for Resturant owner and what would be the best location for them to open a new resturant. The main purpose of the project is to determine which location would yeild more profit and in turn is a better location. We also ask the owner for the resturant size preference and based on it, we would provide the result. 

In this project, our group are trying to simulate the weekly profit of restaurants in different locations. 
We choose two places, one is a restaurant near Green Street, and another is a restaurant in Savoy. For the restaurant in our university, there may be a lot of people during weekdays, nevertheless, the number of customers on weekends may be less. For the restaurant in Savoy, there may be more customers on weekends than during weekdays. 
Based on this situation, we decide to calculate the weekly profits that each restaurant may make and decide which place is better to run a restaurant.
The process of our analysis is top-down.

1.	Profit = Income – Expenses

Usually the profit is represented as this equation. In our project, we suppose that the only expense related to our project is the rental fee. Rental fee depends on the size of the restaurant. Hence, we simplify the profit to be related to the profit of each person and rental fee.

And we get this equation:

2.	Profit = Profit Per Person – Rental Fee

The process for a customer in a restaurant is decided as:
 wait in line(optional), order, decide to go or in restaurant, eating time (if eat in restaurant)
Under this situation, we decide these factors: the time of waiting in line, the time customers stay, the total tables (depend on the size of the restaurant), the total number in the restaurant, customers per minutes during specific period (noon, evening).
These factors will determine the profit together.




## Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?

## Hypothesis or hypotheses before running the simulation:

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

## All Sources Used:
【1】Kimes, Sheryl E., Jochen Wirtz, and Breffni M. Noone. "How long should dinner take? Measuring expected meal duration for restaurant revenue management." Journal of Revenue and Pricing Management 1.3 (2002): 220-233.

【2】Dorr, John A. "Restaurant management information and control method and apparatus." U.S. Patent No. 4,530,067. 16 Jul. 1985.

We search the information about the Business Model of restuarants and could calculate the number of people come to the restaurants. We also know the longest time they would like to wait in a restaurant.
