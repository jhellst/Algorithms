# Electronic Voting System - System Design Interview Question (Pseudocode)
#   - Some data structures and methods outlined in Python, but pseudocode mainly specified.

# Requirements:

# Electronic Voting System
#   - Allows (qualified) voters to submit their answers 1 time.
#   - Contains (or accepts as input) a poll + rules for voting. -> To simplify, we'll assume that top 3 receiving votes are returned as output when results are requested.

# Questions:
#   - How do voters "vote"? -> In voting booths, where their answers will be accepted via a terminal where you click your votes and submit.
#   - Not using a voter booth? -> No.


# Class Design:
#   - Voting System
#       - Interacts with various Voting Booths that all use the same poll and send results (real-time) to the system ledger/directory.

class VotingSystem:
    def __init__(self, poll: dict, valid_machines: dict, eligible_voters: dict):
        self.poll = poll # dict containing all questions to vote on.
        self.votes = {} # When a vote is submitted, we add their vote to this dict under the key for its vote.
        #   -> To simplify, we're just going to count votes.
        #   -> This dict could contain nested dictionaries for each polling question.

        self.valid_machines = valid_machines # Dict that contains all machines for validation of sent results. Paired with results dict as value pair.
        self.eligible_voters = eligible_voters # All voters who can vote in this poll.

        # Methods:
        #   - Validate voter -> Checks a voter's info to ensure that they're in the system AND haven't voted yet.
        #       -> Checks a voter's name + SSN -> determines if they can vote.

        #   - Tally Results -> Looks through self.votes and returns the max, or top n vote recipients.


class VotingBooth:
    # Want to send submitted votes to the VotingSystem. Might also want to maintain some Booth-specific counting stats, as well.
    def __init__(self, id, location):
        self.votes = {} # When a vote is submitted, we add their vote to this dict under the key for its vote.
        self.id = id
        self.location = location

    # Methods:
    #   - Submit Vote -> Takes a voter's sumbission and adds it to the VotingSystem's total results (and the VotingBooth results).
    #       -> Also marks that voter as "voted" in the overall system. Therefore, they won't be able to vote again in any other booths (or the same one).

    # Voter, user flow:
    #   - Voter shows up to booth, inputs their voter info (name + SSN) -> call to VotingSystem to validate_voter -> if voter is validated (in the voters dict + not already voted), we receive the poll on the screen.
    #   - Then, user can submit their vote(s) -> Upon submit, this result is sent to VotingSystem -> result added (possibly to a total_votes dict AND a booth_specific dict).
    #       -> Upon submission, mark that user as "voted" in self.eligible_voters dict. That way, they won't be able to vote in the same poll again.


# Other questions:
#   - Do we need to have start/end dates for the poll input in the system?
#   - Do we care about any other voter info, besides name, SSN, and their vote result?
#   - Is a voter eligible for only 1, or a few, polling locations? Or can they vote anywhere 1 time?