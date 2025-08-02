from ic import ic  # type: ignore

class Solution:
    def reverseVowels(self, s: str) -> str:
        length = len(s)
        if length <= 1:
            return s
        vowels = 'aeiou'
        vowels += vowels.upper()
        right_index = length - 1
        res = []
        replace = {}
        for i, letter in enumerate(s):
            if i in replace:
                letter = replace[i]
            elif letter in vowels:
                new_letter = None
                while i <= right_index:
                    new_letter = s[right_index]
                    if new_letter in vowels:
                        break
                    right_index -= 1

                replace[right_index] = letter
                letter = new_letter
                right_index -= 1
            res.append(letter)
        return ''.join(res)
