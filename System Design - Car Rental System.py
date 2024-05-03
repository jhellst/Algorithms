# Car Rental System: System Design
#   - Pseudocoded response, with data structures outlined in Python

# Requirements:

# Car rental system
#   - Has a system that lets you "book" cars that are available
#   - Cars in the system represented by a class
#       - Make, model, year, vehicle_type, daily_rate, status
#   - The system needs to allow a "user" to reserve a car for a specified date.

# Questions:
#   - What info do we need regarding the renter of the vehicle?
#       - Assuming abstraction of a "Person" class that contains name, etc.

# Classes:
#   - VehicleRentalSystem
#       - vehicles: {} -> Dict containing all cars in rental system.
#       - vehicles_available: set()
#       - cur_time: datetime
#       - rental_revenue: float ($)

#   - Methods:
#       - def reserve_vehicle(self, car, person, start_date, end_date):
#           - Takes an available rental and rents it -> removed from cars_available
#           - Q: How do we rent a car? Randomly assigned? Searched for? We select and see if it's available? -> Assuming random assignment.
#               -> Take a random vehicle from cars dict, and rent it for specified time frame IF it's available.

#       - def return_vehicle(self, car, person, start_date, end_date):
#           - Takes a rented car and "returns" it -> makes it available to rent, again.
#   Also, we could consider methods to 1) modify/extend/cancel a reservation and 2) add a car


#   - Vehicle -> Stores all info about a single vehicle
#       - Make: str
#       - model: str
#       - year: int
#       - vehicle_type: str/enum

# Total Hierarchy:
#   - class CarRentalSystem:
#       - class Rental:
#           - class Vehicle:
# "The CarRentalSystem holds instances of Rental -> these instances correspond to a single Vehicle each, and each Rental can be reserved if it is not already."

# - Rental:
#       - vehicle: Vehicle -> Contains all info about the vehicle
#       - daily_rate: float
#       - late_fee: float -> daily rate for late returns
#       - available: Bool
#       - start_date: datetime or None
#       - end_date: datetime or None

#       - def rent_vehicle(self, start_date, end_date): -> Makes vehicle unavailable until end_date
#       - def return_vehicle(self): -> Makes vehicle available and erases start/end dates.
#           - Return value is the $ amount that the customer owes (we're assuming that the customer pays at the end, AND they pay based on actual days and not the reservation).