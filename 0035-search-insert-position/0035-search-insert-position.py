class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1 
        while(i <= j):
            mid = i + (j-i)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid] :
                j = mid-1
            else:
                i = mid+1  
        return i            
                 



          #insert at the end ....ex-3 , len(a) = 3 ..so tyarget is greater that nums[i] ,,it comes out from while loop and return i ---appends target at last index
        