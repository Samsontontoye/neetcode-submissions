class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq1 = {}
        freq2 = {}

        for character in s:
            freq1[character] = freq1.get(character, 0) + 1
        
        for character in t:
            freq2[character]= freq2.get(character, 0) + 1

        return freq1 == freq2
