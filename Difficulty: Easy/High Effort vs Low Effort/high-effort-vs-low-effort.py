class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        no_task, max_task = 0, 0
        for hi, lo in zip(h, l):
            no_task, max_task = max_task, max(max_task + lo, no_task + hi)
        return max_task