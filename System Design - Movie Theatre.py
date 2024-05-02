# Movie Theatre - System Design:
#   - Answer will be pseudocoded, with some data structures/classes written out in Python.

# Requirements:
#   - Movie theatre, with multiple screening rooms
#   - Each screening room will have a fixed # of seats
#       - Can be empty or occupied
#       - We'll assume that all seats are the same (not in location, but in price/other characteristics)
#   - The $ price for each screening room can be set for each movie/screening
#   - Also would have concessions, but we'll ignore this for now

#   - Do we need to set a schedule for the screening rooms?
#       - If so, we'll need to hold this as part of the OOP class for each individual screening room
#       - If schedule is used, make it so that customers can only enter the room with a ticket IF it's at minimum 20 minutes before the movie starts AND their ticket is correct.

# At the movie theatre level, we need to be able to display (and sell tickets for) every movie that is screening TODAY. Need to have all screenings mapped here
#   - Info needed: Movie/Id, Movie times, screening_room, Price, # tickets left for each time.

# Possibility: Need a class to store info for each customer that enters the theatre. We can store tickets, name/id.

# Interaction with API
#   - Customers must be able to
#       1) Buy a ticket and enter the theatre
#       2) Enter a screening room IF their ticket corresponds to that screening.
#       3) Leave the screening room (might be important to track # in theatre overall, too)
#   - Screening rooms must
#       1) Have a max capacity, and track the capacity of customers
#       2) Have a "seat map" that contains each seat
#           - Each seat needs to store info for if a customer is seated, or if it is empty.


# OOP Class Design:

class MovieTheatre:
    def __init__(self, screening_rooms: dict, total_capacity: int):
        self.screening_rooms = screening_rooms # Contains all of the screening rooms in the theatre.
        self.capacity = total_capacity
        self.movies = {} # MovieName: Movie object
        self.time = datetime.now() # Some way to track the time
        self.total_occupants = 0

        # Possibly want to include details for when the theatre is open/closed. If closed, customers may not enter.
        # Possibly want to include info on # of staff working and their responsibilities.
        # Concession stands would be another detail to include on this level.

    # Methods:
    #   - def enter_theatre()
    #   - def leave_theatre()

class Movie:
    def __init__(self, movie_name: str, screenings: set, rating: str, run_time: int):
        self.name = movie_name
        self.screenings = screenings
        self.rating = rating
        self.run_time = run_time

    # Methods needed to change price, change times (add/remove/modify).
    # def change_price(self):
    # def change_times(self):

class MovieScreening: # Contains info relating to a single screening. Will store total capacity, tickets purchased, the screening_room info, and price.
    def __init__(self, screening_room: ScreeningRoom, seats: dict, price: float, start_time, end_time, movie):
        self.seats = seats
        self.price = price
        self.start_time = start_time
        self.end_time = end_time
        self.movie = movie
        self.screening_room = screening_room # Contains all info for the screening room itself, including occupancy, and capacity.
        #   - Access the screening room's properties here -> manage the capacity of the room here.

    # Methods:
    # def admit_viewer(self, viewer): # Viewer must have a good ticket. If they do, add them to their corresponding seat.
    #   - Handle case to ONLY admit the viewer if they have a valid ticket for this theatre, AND they are at most 20 mins before the start_time.

    # def exit_viewer(self, viewer):

class MovieTicket:
    def __init__(self, movieScreening: MovieScreening, seat: str):
        self.movieScreening = movieScreening
        self.seat = seat


class ScreeningRoom:
    def __init__(self, seats: dict, screenings: dict):
        self.seats = seats
        self.seats_taken = 0
        self.capacity = len(seats)
        self.screenings = screenings # Dict containing the screening/movie schedule.

    # Methods:
    # def admit_viewer(self, viewer, seat):
    # def exit_viewer(self, viewer):
    # def check_status(self):