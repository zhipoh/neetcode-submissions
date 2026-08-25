class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # I have seen this question a few times before but the idea is to use prefix and suffix in place. So don't use extra arrays, keeping space complexity low.

        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res