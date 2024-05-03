# System Design - Blackjack
#   - Pseudocoded answer

# Requirements:
#   - Up to n # of players can sit at a table and play Blackjack against the dealer.
#   - m # of decks are shuffled together. After a certain # of cards are dealt (and we're in-between rounds), we re-shuffle every card to create the full "shoe".
#   - Specific payout odds for blackjack.

#   - During a round of play, the dealing occurs and then each player plays in order.
#       - When it's a player's turn, they can hit or stay.
#       - If their total cards sum up to > 21, they lose and their turn is over.
#       - If sum is == 21 -> you win and your payout is increased by the blackjack bonus

#   - Each "seat" can hold an instance of a Player object
#       - Each Player has name/id, amount_cash, cards_held,

# OOP Design:

# class Blackjack:
#   - seats: dict -> Maps each seat.

class BlackJackTable:
    def __init__(self, seats: list, minimum_bet: int, cash_balance: int):
        self.seats = seats
        self.cash_balance = cash_balance
        self.current_game = None # Can be None or an instance of Game class.
        self.minimum_bet = minimum_bet
        self.total_earnings = 0

    def start_new_game(self, seats):
        # sets current_game to a new game
        self.current_game = Game()

    def add_cash(self, amount):
        self.cash_balance += amount
    def remove_cash(self, amount):
        if self.cash_balance > amount:
            self.cash_balance -= amount
        else:
            print("Not enough cash to take desired amount from table.")

class Card: # Card value, suit, and faceup/facedown.
    # Method to allow for card to be flipped.
    self.value
    self.suit
    self.face_up: bool

class Game:
    def __init__(self, seats: list):
        self.cur_pot = 0
        self.seats = seats # list of seats (should only be 8 or 10 max). Each seat can be empty OR contain a player object.
        self.player_turn = 0 # index of player's turn. Will return to 0 once we reach final index.
        self.player_results = [] # Heap containing [total, Player]
        self.dealer_result = [] # Contains final total
        self.player_blackjack = False # bool -> Switches to true IF a blackjack happens. This affects the payout.

    # Methods:
    def start_game(self): # Shuffle the decks and deal.
    def deal_game(self, seats: list):
    def shuffle_deck(self):

    # Need to let players place bets.
    def place_bet(self, player, amount):
        # add to self.cur_pot.

    def play_player_turn(self): # Process a player's turn.
    def play_dealer_turn(self): # Process the dealer's turn

    # Deal 2 cards to each player.
    # Note: Loop through self.seats and allow every player to play in order.
    #   - Make sure that dealer only gets to play


    def process_card_dealt(self, player): int
        # Adds that card and returns the new cur_total.
        # If cur_total == 21, immediately end and add to self.player_results.
        # If cur_total > 21, end turn and don't append to self.player_results.
        # If cur_total < 21, present player with option to hit or stay.

    def hit(self, player):
        # Draws card from the top of the deck and adds to cur_hand. Increment cur_total and validate.

    def stay(self):
        # Ends a player's turn. Increments game index.

    def check_result(self):
        # After the game, need to see who gets paid out. If dealer wins, he takes the entire pot.
        # If the dealer loses, every player who didn't bust wins.

    def pay_winners(self):
        # For each player in self.player_results, pay them back the $ amount they bet.
        #   - Note: There's a modifier on $ amount if a blackjack occurs.
        #   - Remove that $ from the table and decrement the cash_reserves on the table.

    def dealer_wins(self):
        # If the dealer wins, add each player's bet to self.cash_balance.

class Player:
    def __init__(self, id: str, cash: int):
        self.id = id
        self.cash = cash
        self.cur_hand = [] # List of Card objects.
        self.cur_total = 0



# Clarifying Questions/Assumptions:
#   - Do we need to keep track of money earned/lost?
#   - Assuming 1 table with 1 dealer and interchangable players.