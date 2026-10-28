class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            pre[i] = prod
        prod = 1
        for i in range(len(nums)-1, -1,-1):
            prod *= nums[i]
            suf[i] = prod
        #edge case
        if len(nums) == 2:
            nums[0] = suf[1]
            nums[1] = pre[0]
            return nums

        print(nums)
        print(pre)
        print(suf)

        nums[0] = suf[1]
        nums[len(nums)-1] = pre[len(nums)-2]
        for i in range(1, len(nums)-1):
            nums[i] = pre[i-1]*suf[i+1]
        return nums
