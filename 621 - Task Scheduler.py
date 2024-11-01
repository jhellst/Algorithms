# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
# Return the minimum number of CPU intervals required to complete all tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:
# Input: tasks = ["A","A","A", "B","B","B"], n = 3
# Output: 10
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

# Constraints:

#     1 <= tasks.length <= 104
#     tasks[i] is an uppercase English letter.
#     0 <= n <= 100



class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Use max_heap and queue.
        #   - max_heap: Stores [-char_count, char] for each task.
        #   - delay_queue: Stores chars that still need to be
        # With a given interval, certain chars will be placed in the delay_queue until enough time has passed.
        # When enough time has passed, we can return it to the heap.

        task_counter = collections.Counter(tasks)
        max_heap = [[-count, key] for key, count in task_counter.items()]
        heapq.heapify(max_heap)

        time = 0
        delay_queue = collections.deque()

        while max_heap or delay_queue: # Continue operations until both the heap and queue are empty (only then are all tasks completed)

            if max_heap: # If any elements on heap, we can complete one task.
                cur_count, cur_char = heapq.heappop(max_heap)
                cur_count += 1

                # Place this item on the delay_queue, unless count has been reduced to 0.
                if cur_count < 0:
                    delay_queue.append([time + n + 1, cur_count, cur_char]) # time_to_return is time + interval

            time += 1

            # Now, move any items from the queue that are out of the delay period.
            while delay_queue and delay_queue[0][0] == time:
                cur_time_to_return, cur_count, cur_char = delay_queue.popleft()
                heapq.heappush(max_heap, [cur_count, cur_char])

        return time

# Time Complexity: O(n * log(k)) -> Traverse all tasks (and intervals) and conduct heap operations on all tasks.
# Space Complexity: O(k) -> O(n) -> All unique tasks to be stored in heap/queue/counter. In worst case, each task is unique.



# 2nd Solution:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # We can use a stack/queue to simulate tasks becoming "completable".
        #   - Pop the task from the queue that is 1) not in cooldown and 2) has the most # remaining.

        c = Counter(tasks)
        max_heap = [] # [-count, char]
        delay_queue = deque() # [char, time_to_unblock, count] -> time_to_unblock is (time + n).

        for key in c:
            heapq.heappush(max_heap, [-c[key], key])

        # Process:
        #   - Pop from max_heap to get next task. Then, decrement task count and "complete" it.
        #   - If that task still has count > 1, we need to put it on the delay queue.
        #   - On each loop, check left side of delay_queue to see if any tasks can return to the max_heap.

        time = 0

        while max_heap or delay_queue: # As long as tasks remain on the max_heap OR on the delay_queue, we need to continue.

            while delay_queue and delay_queue[0][1] < time:
                cur_char, time_to_unblock, cur_count = delay_queue.popleft()
                heapq.heappush(max_heap, [-cur_count, cur_char])

            if max_heap: # Complete a task, then add it to the delay queue (if needed).
                neg_cur_count, cur_task = heapq.heappop(max_heap)
                cur_count = -neg_cur_count
                if cur_count > 1: # Add to delay_queue
                    delay_queue.append([cur_task, time + n, cur_count - 1])

            time += 1

        return time

# Time Complexity: O(n * log(n)) -> Conduct heap operations on a heap of up to n unique tasks.
# Space Complexity: O(2 * n) -> O(n) -> Store up to n tasks on heap/queue data structures.