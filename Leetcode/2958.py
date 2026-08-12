#2958. Length of Longest Subarray With at Most K Frequency
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count={}
        left=0
        ans=0
        for right in range(len(nums)):
            if nums[right] in count:
                count[nums[right]]+=1
            else:
                count[nums[right]]=1
            while count[nums[right]]>k:
                count[nums[left]]-=1
                left+=1
            ans=max(ans, right - left + 1)
        return ans