from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)
        def can_assign(k):
            sub_tasks = tasks[:k]
            available = workers[m-k:].copy()
            pills_remaining = pills
            for task in reversed(sub_tasks):
                if available[-1] >= task:
                    available.pop()
                else:
                    if pills_remaining == 0:
                        return False
                    idx = bisect_left(available, task - strength)
                    if idx == len(available):
                        return False
                    available.pop(idx)
                    pills_remaining -= 1
            return True
        low, high = 0, min(n, m)
        while low < high:
            mid = (low + high + 1) // 2
            if can_assign(mid):
                low = mid
            else:
                high = mid - 1
        return low
        
