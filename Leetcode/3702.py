#3702. Longest Subsequence With Non-Zero Bitwise XOR
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor=0
        for i in range(len(nums)):
            xor=xor^nums[i]
        if xor!=0:
            return len(nums)
        for i in range(len(nums)):
            if nums[i]!=0:
                return len(nums)-1
        return 0