__author__ = "Sarp Gurenli"
__copyright__ = "Copyright 2018, Ship Sail Calculator"
__version__ = "1.4"
"""5th Assignment
Complete following functions
Call the functions for some example cases"""
def time(Speed, Distance):
    """This Function gets Speed(knot) and
    distance between ports (km) as inputs.
    It returns how many hour later ship will 
    arrive."""
    time = Distance/Speed # this function divide distance to speed and find the time ant than convert float to integer
    return time
def max_dis(Tank_capacity,Consumption, Speed):
    """This function calculates max distance
    which the ship can go"""
    maxdis = Speed*(Tank_capacity/Consumption) # calculate max distance 
    return maxdis
def enough(Tank_capacity, time, Consumption, Speed=10):
    """This function gets Tank capacity (ton),
        the arriving time to the port (hour) and 
        fuel consuption (ton/day) as input. It prints
        The ship is suitable for this route" if the fuel
        is enough to arrive next port.It will prints 
        The ship is not suitable for this route and it can 
        go maximum XXXXX km" if fuel does not enough."""
    if time*Consumption/24 > Tank_capacity:
        a = max_dis(Tank_capacity,Consumption, Speed)
        print("The ship is not suitable for this route and it can go maximum {0:.2f} km".format(a))
    else:
        print("The ship is suitable for this route")
Speed = float(input("speed(knot):"))*1.8519995 # get knot data and conert to km/h
Distance = float(input("distance between ports (km):")) # get distance between ports 
Tank_capacity = float(input("Enter Tank Capacity(ton):")) # get tank capacity
Consumption = float(input("Enter Fuel Consumption ton/day:")) # get fuel consumption 
b = time(Speed,Distance)
print("----------------------------------------------------------------------------------")
print("{} hour later ship will arrive.".format(b)) # this line shows how many hour later ship will arrive
print("----------------------------------------------------------------------------------")
#print("Max distance is {} km which the ship can go.".format(max_dis(Tank_capacity, Consumption, Speed)))
#print("----------------------------------------------------------------------------------")
#print("The ship is not suitable for this route and it can go maximum {} km".format(enough(Tank_capacity, time, Consumption, Speed=10)))
#print("----------------------------------------------------------------------------------")
enough(Tank_capacity, b, Consumption, Speed)