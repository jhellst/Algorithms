# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.


class MinStack:
    # Use a stack to store values. Also, use a stack to store minValues.

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min or self.min[-1] >= val:
            self.min.append(val)

    def pop(self) -> None:
        removed = self.stack.pop()

        if self.min[-1] == removed:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# Solution 2:

class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0 or self.mins[-1] >= val:
            self.mins.append(val)

    def pop(self) -> None:
        remove_val = self.stack.pop()
        if self.mins[-1] == remove_val:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# Time Complexity: O(1) -> Every operation is just appending or popping a single item from 2 stacks.
# Space Complexity: O(2 * n) -> O(n) -> In worst case, store every value once in self.stack and self.mins.