from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        result = minimum = 0

        for num in nums:
            result = result + num
            minimum = min(minimum, result)

        return abs(minimum) + 1

