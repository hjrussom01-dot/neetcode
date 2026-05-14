class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            if char not in chars:
                chars[char] = 1
            else: chars[char] += 1
        
        for char in t:
            if char in chars:
                chars[char] -= 1
            else: return False
        
        for num in chars.values():
            if num != 0: return False
        return True