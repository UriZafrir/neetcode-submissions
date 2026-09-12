class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s+=char.lower()
        for i in range(len(clean_s)//2):
            if clean_s[i]!=clean_s[len(clean_s)-i-1]:
                return False
        return True


"""
clean_s = ""
for char in s:
    if char.isalnum():
        clean_s+=char.lower()
for i in range(0,len(s)//2,1):
    for j in range(len(s)-1)
    if s[i]!=s[len(s)-i-1]:
        return False
return True
"""


"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(0,len(s)//2,1):
            j=len(s)-1 # last index of string
            s_middle=len(s)//2
            if not s[i].isalnum():
                i+=1
            if not s[j].isalnum():
                j+=1
            if s[i]!=s[len(s)-i-1]:
                return False
"""


"""
        for i in range(0,len(s)//2,1):
            for j in range(len(s)-1)
            if s[i]!=s[len(s)-i-1]:
                return False
        return True
"""

"""
        for i in range(0,len(s)//2,1):
            if not s[i].isalnum
            if s[i]!=s[len(s)-i-1]:
                return False
        return True
#need to ignore case and also all non-alphanumeric
so first both for 
i need to set only once both i and j=len(s)-i-1 then have two loops
"""