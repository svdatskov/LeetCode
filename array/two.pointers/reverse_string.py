from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        while i < j:
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            j -= 1
            i += 1
