# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"


# Constraints:

# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.

class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Add to self.d.
        if key in self.d:
            self.d[key].append([timestamp, value])
        else:
            self.d[key]= [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        # Binary search self.d[key], if there are more than 1 values.
        if key not in self.d:
            return ""
        values = self.d[key]
        left, right = 0, len(values) - 1

        highestValid = ""

        while left <= right:
            mid = (left + right) // 2
            curTimestamp, curValue = values[mid]

            if curTimestamp == timestamp:
                return curValue
            elif curTimestamp > timestamp: # Too high, search to left.
                right = mid - 1
            else:
                highestValid = curValue # Store current answer as highest valid.
                left = mid + 1

        return highestValid



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Time Complexity:
    # - set() -> O(1) -> Add to dict. Single operation for each "set"
    # - get() -> O(log(n)) -> In worst case, will binary search an array containing every value.
# Space Complexity: O(n) -> Store every value once in a hashmap.





# 2nd Solution:

class TimeMap:
    # Data structure must be able to retrieve a value with a given key at (or before) the timestamp.
    #   - Prioritize the later timestamp, if necessary.
    # Solution uses a dict that stores an array for each key.
    # A linked list is another possible option.

    def __init__(self):
        self.map = {} # key: ListNode

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Add key and value to map.
        if key in self.map:
            self.map[key].append([timestamp, value])
        else:
            self.map[key] = [[timestamp, value]]
            self.map[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        # Retrieve from self.map -> return value at key for given timestamp.
        #   - If current timestamp isn't in self.map[key] -> return the largest timestamp <= the provided "get" timestamp.

        if not key in self.map:
            return ""

        # If key exists:
        #   - Return largest timestamp_prev where timestamp_prev <= timestamp.
        #   - If no timestamp_prev <= timestamp, return "".

        # Binary search the array for the timestamp.
        cur_array = self.map[key]
        cur_res = ""

        left, right = 0, len(cur_array) - 1
        while left <= right:
            mid = (left + right) // 2
            cur_timestamp, cur_val = cur_array[mid]

            if cur_timestamp == timestamp:
                return cur_val
            elif cur_timestamp > timestamp: # Search to the left for a smaller timestamp.
                right = mid - 1
            else:
                cur_res = cur_val # Store this val, because it is valid for now and might be the largest valid timestamp.
                left = mid + 1

        return cur_res

# Time Complexity:
    # INIT: O(1)
    # SET: O(log(n)) -> Append new [timestamp, val] and sort the array. In worst case, array is of length == n.
    # GET: O(log(n)) -> Binary search for timestamp within array. In worst case, array is of length == n.
# Space Complexity: O(n) -> In worst case, store every timestamp/value combo in self.map, within an array.