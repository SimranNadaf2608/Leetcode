class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        h = {}
        for i in nums:
            h[i] = True
        for i in range(len(nums)):
            if i in h:
                h[i+1] = True
            elif i not in h:
                h[i] = True
        print(h)

        for i in h:
            if i not in nums:
                return i


        # h = {}
        # for i in nums:
        #     h[i] = 1
        # print(h)
        # for i in range(len(nums)):
        #     if i not in h:
        #         h[i] = 1
        #     elif i in h:
        #         h[i+1] = 1
        # print(h)
        # for i in h:
        #     if i not in nums:
        #         return i
     
        