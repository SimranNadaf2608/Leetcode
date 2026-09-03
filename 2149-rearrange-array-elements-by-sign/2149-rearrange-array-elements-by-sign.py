class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i]) 
        res = []

        i = 0
        j = 0
        while i < len(pos) and j < len(neg):
            res.append(pos[i])
            res.append(neg[i])
            i += 1
            j += 1
        return res
