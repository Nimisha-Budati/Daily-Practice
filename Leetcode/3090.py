#3090. Maximum Length Substring With Two Occurrences
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count={}
        left=0
        ans=0
        for right in range(0,len(s)):
            if s[right] not in count:
                count[s[right]]=0
            count[s[right]]+=1
            while count[s[right]]>2:
                count[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans