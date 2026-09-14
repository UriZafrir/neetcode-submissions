class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while j-i > 0:
            if s[i]!=s[j]:
                temp=s[i]
                s[i]=s[j]
                s[j]=temp
            i+=1
            j-=1
"""
let's try
Input: s = ["n","e","e","t"]
i=0
j=3
s[0]="t"
s[j]="n
i=1
j=2
do nothing
i=2
j=1

["r","a","c","e","c","a","r"]
i=0
j=6
temp="r"
s[i]="r"
do nothing
i=1
j=5
do nothing
i=2
j=4
do nothing
i=3
j=3
"""


