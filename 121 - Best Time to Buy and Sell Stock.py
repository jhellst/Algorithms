# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy. If we see a cheaper price, then we MUST reset the cost to buy to the new price.

        res = 0
        purchasePrice = prices[0]

        for price in prices[1:]:
            if price > purchasePrice:
                res = max(res, price - purchasePrice)
            else:
                purchasePrice = min(price, purchasePrice)

        return res

# Time Complexity: O(n) -> Single pass of prices array.
# Space Complexity: O(1) -> No additional storage.




# Solution 2:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy solution.
        #   - As we traverse prices array -> Continue to record the min_price.
        #   - At each price, calculate sale price against the current max.

        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit

# Time Complexity: O(n) -> Single pass of prices array.
# Space Complexity: O(1) -> No additional storage space used.