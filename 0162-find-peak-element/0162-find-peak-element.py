class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 1
        right = len(nums)-2
        high = len(nums)-1
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[high] > nums[right]:
            return high
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                left = mid+1
            elif nums[mid] > nums[mid+1]:
                right = mid-1
            else:
                left = mid+1
        return -1


        