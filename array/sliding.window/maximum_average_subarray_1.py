from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        summ = sum(nums[:k])
        max_summ = summ

        for i in range(k, len(nums)):
            summ += nums[i] - nums[i - k]
            if summ > max_summ:
                max_summ = summ


        return max_summ / k