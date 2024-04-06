from collections import *

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        for char in stones:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        result = 0
        for char in jewels:
            if char in freq:
                result = result + freq[char]
        
        return result