class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = {}
        for char in s:
            if char in s_counts:
                s_counts[char] += 1
            else:
                s_counts[char] = 1
        t_counts = {}
        for char in t:
            if char in t_counts:
                t_counts[char] += 1
            else:
                t_counts[char] = 1
        if s_counts == t_counts:
            return True
        return False
"""
first check if strings are equal length and output false if not 
"""