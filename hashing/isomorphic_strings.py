# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
#
#
#
# Example 1:
#
# Input: s = "egg", t = "add"
#
# Output: true
#
# Explanation:
#
# The strings s and t can be made identical by:
#
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:
#
# Input: s = "f11", t = "b23"
#
# Output: false
#
# Explanation:
#
# The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.
#
# Example 3:
#
# Input: s = "paper", t = "title"
#
# Output: true
#
#
#
# Constraints:
#
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = defaultdict(str)
        seen = set()

        for i in range(len(s)):

            if s[i] not in mapping:
                if t[i] in seen:
                    return False

                mapping[s[i]] = t[i]
                seen.add(t[i])

            elif s[i] in mapping and mapping[s[i]] != t[i]:
                return False

        return True

s = Solution()

print(s.isIsomorphic("badc", "baba"))



