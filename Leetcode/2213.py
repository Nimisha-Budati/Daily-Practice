#2213. Longest Substring of One Repeating Character
"""
#This is the brute force
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        s=list(s)
        output=[0]*len(queryIndices)
        for i in range(0,len(queryIndices)):
            s[queryIndices[i]]=queryCharacters[i]
            count=0
            max=0
            for j in range(0,len(s)-1):
                if s[j]==s[j+1]:
                    count+=1
                else: 
                    count=0
                if count>max:
                    max=count
            output[i]=max+1
        return output          
"""