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


# 2nd Solution (Less Optimal):

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Create groups of consecutive cards.
        #   - Return True if possible, False if not.

        # We want to simulate the process of making groups.
        #   - Within this process, return False if we can't make a "straight" in any grouping.
        #   - Use a heap to store the minimum values that are still in the hand.

        c = Counter(hand)
        min_heap = [val for val in c]
        heapq.heapify(min_heap)

        # Now we have the counter AND the heap that orders the values in the hand.
        #   - Process these so that we're creating hands of size groupSize, always starting with the lowest remaining value.

        while min_heap:
            used_numbers = [] # Holds values that will be added back to min_heap.

            prev = None
            for i in range(groupSize):

                if not min_heap:
                    return False

                cur_val = heapq.heappop(min_heap) # Lowest value remaining on the min_heap.
                cur_count = c[cur_val] # Count of cur_val.

                if prev != None and cur_val != prev + 1:
                    return False
                else:
                    new_count = cur_count - 1
                    c[cur_val] = new_count

                    if new_count != 0: # Add back to heap if count still > 0.
                        used_numbers.append(cur_val)
                    # Otherwise, don't add back to heap, because count == 0.

                prev = cur_val

            # Add used_numbers back to min_heap.
            for num in used_numbers:
                heapq.heappush(min_heap, num)

        return not min_heap

# Time Complexity: O(n / groupSize * log(n)) -> Loop up to n // groupSize times and conduct heap operations on heap of size n.
# Space Complexity: O(n) -> Store values on heap of max_length == n.