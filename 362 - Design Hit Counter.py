# Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).
# Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

# Implement the HitCounter class:

# HitCounter() Initializes the object of the hit counter system.
# void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
# int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).

# Example 1:

# Input
# ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
# [[], [1], [2], [3], [4], [300], [300], [301]]
# Output
# [null, null, null, null, 3, null, 4, 3]

# Explanation
# HitCounter hitCounter = new HitCounter();
# hitCounter.hit(1);       // hit at timestamp 1.
# hitCounter.hit(2);       // hit at timestamp 2.
# hitCounter.hit(3);       // hit at timestamp 3.
# hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
# hitCounter.hit(300);     // hit at timestamp 300.
# hitCounter.getHits(300); // get hits at timestamp 300, return 4.
# hitCounter.getHits(301); // get hits at timestamp 301, return 3.

# Constraints:

# 1 <= timestamp <= 2 * 109
# All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
# At most 300 calls will be made to hit and getHits.

# Follow up: What if the number of hits per second could be huge? Does your design scale?



# Pseudocode:
# Design a "Hit Counter"
#   - Counts the # of hits received over the past 5 mins (300 seconds).
#   - As input, system takes a timestamp (seconds) to register a hit.
#   - Remove the "expiring" timestamps once they are over 5 mins in the past.

# When we record a hit, we can immediately advance to the provided timestamp. Remove all required timestamps.

class HitCounter:

    def __init__(self):
        self.hits = deque() # Contains timeStamp from the "hit" operation. We can remove it (starting from the beginning) if it's 5 or more minutes ago.
        self.curTime = 0 # Time in seconds.

    def hit(self, timestamp: int) -> None: # Register a hit, and remove all hits that are 5+ minutes ago. Make sure to adjust time
        self.curTime = timestamp
        self.hits.append(timestamp)

        while self.hits and self.hits[0] <= self.curTime - 300:
            self.hits.popleft()

    def getHits(self, timestamp: int) -> int: # Returns the # of hits in the last 5 minutes, given a timestamp.
        self.curTime = timestamp

        while self.hits and self.hits[0] <= self.curTime - 300:
            self.hits.popleft()

        return len(self.hits)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


# Time Complexity:
#   - hit: O(k) -> In worst case, pop the entirety of self.hits (k elements).
#   - getHits: O(k) -> In worst case, pop the entirety of self.hits (k elements).
# Space Complexity: O(n) -> In worst case, the data structure will contain every "hit" that has occured.