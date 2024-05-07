# Real Time Leaderboard: System Design
#   - Pseudocoded response, with data structures outlined in Python

# Real Time Leaderboard:

# Requirements:
#   - Design a real time leaderboard for a popular competitive game to track the top players that season
#   - Each time a player scores in a game, we want to increment their total score.
#   - Leaderboards are refreshed every 3 months and display to top 25 users.

# Methods:
#   - recordScore(self, player): takes a unique player name/id and increments their corresponding count.
#   - displayLeaderboard(self): returns the top 25 players + their scores.

# Player stats need to be updated immediately upon a player action (score).
# No need for searching players.


# Needed: A system that accepts new "scoring" actions from a specified player.
#   - When a player scores, we want to
#   - Appears that a player scoring in a game will increment their overall score on the leaderboard.

# We want to use a dictionary/hashmap to store all players with their scores. displayLeaderboard() will scan all records and return the top 25 players.
# Do players need to have played recently to be included in the leaderboard? Do their scores ever expire?

# Class Design (OOP):

class Leaderboard:
    def __init__(self): # Assume that 25 users are on leaderboard AND the scores are continually updated. All players' scores are stored forever (assumption).
        self.players = {} # id: score

    def recordScore(self, player_id): # Record a new score for a player. If they exist in self.players, just increment. Otherwise, add them to self.players with a score of 1.
        if player_id in self.players:
            self.players[player_id] += 1
        else:
            self.players[player_id] = 1

    def displayLeaderboard(self): # Takes the top 25 scores.
        leaders = [] # minHeap. Push [score, player] to minHeap.

        for player in self.players:
            player_id, player_score = player, self.players[player_id]

            heapq.heappush(leaders, [player_score, player_id])
            while len(leaders) > 25: # If capacity of leaderboard (25) is exceeded, pop items.
                heapq.heappop(leaders)

        # Now, leaders array contains 25 top scores (with name/id).
        return [[leader[1], leader[0]] for leader in leaders] # Returns name:score

# Time Complexity:
#   - init: O(1)
#   - recordScore: O(1)
#   - displayLeaderboard: O(n * k * log(n)) -> O(n * 25 * log(n)) -> O(n * log(n)) -> For every player stored, we push to heap of 25 (k) items and conduct heap operations on a heap of size 25 (k).
# Space Complexity: