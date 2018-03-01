'''
    Emanuel Gitterle
    Andreas Glarcher
'''
from operator import attrgetter
from collections import namedtuple

Car = namedtuple('Car', ['id', 'score', 'time', 'pos_x', 'pos_y', 'rides_id'])
#Ride = namedtuple('Ride', ['id', 'start', 'finish', 'earliest', 'latest', 'distance'])


# Shedule the rides
# @param vehicle The number N of available vehicles
# @param rides A list of booked Rides namedtuple('Ride', ['id', 'start', 'finish', 'earliest', 'latest', 'distance'])
def shedule(vehicles, rides, bonus):
    rides = __sort(rides)
    
    # init cars
    cars = []
    for i in range(vehicles):
        cars.append(Car(i,0,0,0,0,[]))
        
    # sheduling
    while(True):
        for i in range(len(cars)):
            index = 0
            for j in range(len(rides)):
                if(__check_possible(car[i],rides[j])):
                    __drive(cars[i], rides[index], bonus) 
    return cars
    

# Sort the rides
# @param rides A list of Rides (namedtuple)
def __sort(rides):
    sorted(rides, key=attrgetter('start'))    
    

# Calculate new state of Car after ride
# @param car The car which does the ride
# @param ride given to the car
def __drive(car, ride, bonus):
    t_arrival = abs(car.x_pos - ride.start.x) + abs(car.y_pos - ride.start.y)
    t_driving = abs(ride.start.x - ride.finish.x) + abs(ride.start.y - ride.finish.y)
    time = t_arrival + t_driving
    
    score = t_driving
    if((car.time + t_arrival) == ride.earlist):
        score += bonus
    
    car.time += time
    car.score += score
    car.x_pos = ride.finish.x
    car.y_pos = ride.finish.y
    car.rides_id.append(ride.id)


# checks if that ride can be performed by this car
def __check_possible(car, ride):
    t_arrival = abs(car.x_pos - ride.start.x) + abs(car.y_pos - ride.start.y)
    t_driving = abs(ride.start.x - ride.finish.x) + abs(ride.start.y - ride.finish.y)    
    time = t_arrival + t_driving
    # read rule <= or < !!!!!!!
    if((car.time + time) <= ride.latest):
        return True
    else:
        return False




