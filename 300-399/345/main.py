# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/

from ic import ic  # type: ignore

class Solution:
    vowels = 'aeiouAEIOU'

    def reverseVowels(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        # Convert string to list for in-place modification
        s_list = list(s)
        left, right = 0, len(s) - 1
        
        # Two-pointer approach
        while left < right:
            # Find vowel from left
            while left < right and s_list[left] not in self.vowels:
                left += 1
            
            # Find vowel from right
            while left < right and s_list[right] not in self.vowels:
                right -= 1
            
            # Swap vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        
        return ''.join(s_list)
