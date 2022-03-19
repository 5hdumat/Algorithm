# https://leetcode.com/problems/task-scheduler/
import collections
import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        res = 0
        counter = collections.Counter(tasks)

        while True:
            sub_count = 0

            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                res += 1

                counter.subtract(task)
                counter += collections.Counter()

            if not counter:
                break

            # print(n , sub_count + 1)
            # that is that there must be at least "n" units of time between any two same tasks.
            res += n - sub_count + 1

        print(res)
        return res


s = Solution()
s.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
s.leastInterval(["A", "A", "A"], 2)
# s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
