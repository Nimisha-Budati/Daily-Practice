#3471. Find the Largest Almost Missing Integer
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        maximum=max(nums)
        found=[False]*(maximum+1)
        count=[0]*(maximum+1)
        for i in range(len(nums)-k+1):
            found=[False]*(maximum+1)
            for j in range(i,i+k):
                found[nums[j]]=True
            for j in range(maximum+1):
                if found[j]==True:
                    count[j]+=1
        ans=-1
        for i in range(maximum+1):
            if count[i]==1:
                if ans<i:
                    ans=i
        return ans