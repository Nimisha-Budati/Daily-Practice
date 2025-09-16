class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(self, a, b):
        return a * b // self.gcd(a, b)
    def replaceNonCoprimes(self, nums):
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) > 1 and self.gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.lcm(a, b))
        return stack
nums_str = input("Enter numbers separated by commas: ").split(',')
nums = []
for s in nums_str:
    nums.append(int(s))
sol=Solution()
print(sol.replaceNonCoprimes(nums))