# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:

# Input: citations = [1,3,1]
# Output: 1

# Constraints:

# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Calculate the researcher's h-index -> calculated as max score "n" where "n" # of that score or higher exists.
        # We want to sort or use a heap here, and store [count, score].

        citations.sort()

        for i, score in enumerate(citations):
            h_count = len(citations) - i

            if h_count <= score:
                return h_count

        return 0





# 2nd Solution:

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Return the H-Index of the researcher, given an array of citations.
        # Process:
        #   - Sort citations array and traverse from highest to lowest, tracking count and value.
        #   - Once count < cur_val, we can return the val (that is the H-Score).

        citations.sort(reverse=True)

        cur_val = 0
        cur_count = 0
        res = 0

        for citation in citations:
            cur_val = citation
            cur_count += 1

            if cur_count == cur_val:
                return cur_val
            elif cur_count < cur_val:
                res = max(res, cur_count)

        # Now, we know that cur_count was never <= cur_val. For that reason, we want to return cur_count.
        return res

# Time Complexity: O(n + n * log(n)) -> Sort array of length n, then traverse it once.
# Space Complexity: O(1) -> No additional storage used.