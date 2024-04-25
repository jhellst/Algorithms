# Parking Garage - System Design:
#   - Answer will be pseudocoded, with some data structures/classes written out in Python.

# Requirements:
#   - Needs to have a fixed # of parking spaces, which can be filled or empty.
#   - Needs to determine if we have spaces left for a new vehicle.
#   - Stores parking spots with their current status (empty or filled with a car) -> Use a hashmap to store this.
#   - Any rules for which spots a car can park in? Can they pick any spot, or is their spot assigned somehow? -> Assuming that the spot is "selected" by the driver.

#   - What info provided for a car that parks? Assuming a "Car" class which contains info about the vehicle.
#   - Different type of spaces? -> Assume just 1 type here, but could consider compact/large/truck spots (with corresponding "type" info saved in car class, as well).

#   - Multiple floors? If so, each space will have to store that info.
#       - Assuming just 1 floor currently.
#   - Any functionality for time/pay? Or are we just tracking cars right now?
#       - How does a customer pay? Upfront, or calculated from time spent in garage? Assuming calculated based on time spent in garage.
#   - Functionality for a car to "leave garage" -> Removes that car from the parking spot (hashmap). Also, calculates total # owed for parking at this time (if needed).


# Class Design:

class Car:
    def __init__(self, id, color...): # Doesn't truly need any of this info to perform basic operations. ID might be nice for a "lookup" of a car's parking space.
        self.id = id
        self.color = color

class ParkingGarage:
    def __init__(self, num_spaces, rate):
        # Initialize the "garage" with all empty spaces.
        self.parking_spaces = {i: None for i in range(num_spaces)} # Contains each spot (with unique id).
        self.capacity = num_spaces
        self.current_count = 0
        self.current_time = 0 # Some method to increment time and use that to calculate time/$ for a car leaving the garage.
        self.rate = rate # Hourly rate for parking.

    # Functionality to "park" a car. Need to error-check to make sure the space is empty.
    def park_car(self, car, space):
        if not self.parking_spaces[space]:
            self.current_count += 1
            self.parking_spaces[space] = [car, self.current_time]
        else: # Error / message that car is already in the spot.
            print("Spot isn't open!")

    def unpark_car(self, space): # Removes car from a space AND calculates amount owed.
        if self.parking_spaces[space]:
            time_taken = self.current_time - self.parking_spaces[space][1]
            amount_owed = time_taken * self.rate
            # Have customer "pay" and send message that car has left.
            print("Car has left, amount paid: ", amount_owed)
            self.parking_spaces[space] = None
        else:
            print("No car in specified spot.")


class ParkingSpace:
    def __init__(self, initial_park_time=None, car=None):
        self.car = car
        self.initial_park_time = initial_park_time

    def calculate_amount_owed(self):

    def park_car(self):

    def unpark_car(self):




# Other possible functionality to add:
#   - Instead of selecting a spot, add option to also randomly assign a spot.
#   - Option to pay upfront for a pre-set amount of time.
#   - Possible functionality to store more info in the "Car" class.
#   - Possible option to create a "Space" class that stores info for the car, start_time, etc. -> GOOD IDEA.

# What other info could we store?
#   - Amount $ earned by garage.
#   - Tracked # of cars in/out of garage (currently only tracking current occupants of garage)
#   - Are there open/close times, or times where the hourly rate is different? Is there an all-day rate?
#       - Could be important to include this functionality to make the garage more robust.
#   - Possibly allow a customer to "lookup" their car in a hashmap. Allows the customer to use their car_id to find what space they are parked in.
#   - Employees? Elevators?