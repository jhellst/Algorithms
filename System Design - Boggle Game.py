# Boggle Game: System Design
#   - Pseudocoded response, with some data structures outlined in Python

# Requirements:
#   - Boggle Game
#   - Needs to be able to keep score across multiple rounds for each player.
#   - Has a 4*4 "grid" and an equal number of dice -> these dice have different letters on each side.
#   - Can "create" a game with x # of players.
#   - Score kept in a dict/array by player. When the game ends (after set # of rounds OR score), we determine the winner.
#   - Possible functionality to provide a words_list (dictionary for the game).

# To play the game:
#   - Select the # of players -> we'll assume between 2 and 8.
#   - When we shuffle the boggle box -> each dice will go in a random spot, in a random orientation.

#   - Players will provide their list of words, which will need to be validated against the board.
#       - In order to validate words, we need to check their words list against the possible words that exist in the grid based on the game dictionary.

# Questions:
#   - Do we need to keep track of multiple full games? -> Assuming just 1 round.
#   - Do we need to include any other player info? Or just 1,2,3,4,5,6? -> Assume that just the player input is fine.
#   - Player class needed? -> Assume no, for now.

# Required Methods:
#   - shuffle_board: randomizes the dice by location and orientation.
#   - generate_word_list: Given a board with dices placed, generate a set of all valid words.

# Class Design:
#   - BoggleGame (includes a board, dice, words_list, players)
#   - Dice (made up of sides, with one active side)
#   - Side (contains just the value)


class BoggleGame:
    def __init__(self, num_players: int, words_list: set, dice: list): # Instead of num_players, possible to just include a list of player instances.
        row = [None] * 4
        self.board = [row[::] for i in range(4)] # 4*4 game board.
        self.words_list = words_list # -> Upon init, we want to convert this into a trie data structure. Or we can provide it, to start.
        self.players = [0] * num_players
        self.dice = dice # List of dice object, each with 6 sides.
        self.turn = 0 # Keeps track of turns (assuming it ends after n turns). We could also end the game after a certain score is reached by one or more players.

    # Methods:
    #   - Shuffle board
    #   - Generate valid_words (after shuffling)
    #   - Play Turn / Calculate Score (takes a single player's list of words and returns a total score for the round + increments that player's score)

    def shuffle_board(self): # Iterates through the 4*4 grid and randomly places a dice that is set to a random side.
        for r in range(4):
            for c in range(4):
                # Select a dice, randomly using a random index from the total range. Remove that dice from the list OR mark it as unavailable.
                # Roll that dice
                # Place that dice in the current cell.
                # Continue until all dice have been randomly placed.

    def generate_valid_words(self):
        # Traverses the board and searches for words of length 3 or greater out of the total words_list.
        # To ensure efficient lookup, we start at each space and DFS, using a trie data structure to enable efficient lookup and "branching" of word possibilities.
        #   - When we're at word_length >= 3, add every word that is valid (and terminating) within the trie.
        # Final result will be a set of all words that were found in the board when compared with the trie of words_list.

    def play_turn(self, player_responses: list): # Inputs each player's answers as an array. For now, we'll assume that the array is just ordered by player_index.
        # Take every player's word_list and generates a dict/counter that includes the count of all responses from any player.
        # Then, for each player, we "score" their responses. The dict will contain word:players -> where "players" is a set.
        #   - For each word in the dictionary with count == 1, we "score" it for the corresponding player. That means that we'll score any word where the lookup dict is length == 1.
        #       - In the case of a "score" -> Calculate the score and increment that index in self.players.

        # If final turn, call end_game()

    def end_game(self): # Automatically ends the game after the nth turn is played (or if the score_limit has been exceeded) -> Return winner (ex: "Player 3"), return placements from the array.

# Scoring rules are pretty basic and are 100% based on the length of the word. Assuming that we'll use a dictionary to lookup the corresponding score based on a word's length.

class Dice:
    def __init__(self, sides: list):
        self.sides = sides # list of exactly 6 sides (though game could be modified for other types of dies)
        self.active_side = sides[0] # Side that is face_up / "active"

    # Methods:
    #   - roll_dice: takes a dice and sets its active side randomly.

class Side:
    def __init__(self, value):
        self.value = value



# Possible Improvements:
#   - Ability to store previous games -> Some dictionary that holds results with an overall score of num_wins kept.
#   - Functionality to have a specified "Player" class that could be placed in the player_list and would play in a similar manner. Only difference would be that the player's info would be stored in the results_dict and could be looked up later. Would also need to provide a player_list upon init.
#   - Side does not necessarily need its own class, each side COULD be selected from the dice's list of sides.