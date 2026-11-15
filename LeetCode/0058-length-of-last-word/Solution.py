class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        for i in reversed(s):
           if i ==" ":
            if length>0:
                break
           else:
               length+=1
        return length

        