# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

from ic import ic  # type: ignore

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
