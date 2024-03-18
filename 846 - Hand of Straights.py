# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

# Constraints:

# 1 <= hand.length <= 104
# 0 <= hand[i] <= 109
# 1 <= groupSize <= hand.length

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Looking to return True or False.
        # Determine if we can split the array into groups of size groupSize, with each group containing only consecutive numbers.

        # Use a hashmap + set. Get all numbers + count in the hashmap, and all numbers in the set.
        # Start at min number and increment up, trying to find a group of groupSize consecutive numbers. Return False if not found.

        numDict = collections.Counter(hand)
        numSet = set(hand)

        while numSet:
            curMin = min(numSet) # Current min -> Find consecutive numbers from here.
            for i in range(0, groupSize):
                if (curMin + i) in numSet:
                    numDict[curMin + i] -= 1
                    if numDict[curMin + i] == 0:
                        numSet.remove(curMin + i)
                else:
                    return False

        return True

# Time Complexity: O(n) -> Visit each number in hand once, then iterate through them again up to 1 time.
# Space Complexity: O(n) -> Store each number in hashmap and set.
