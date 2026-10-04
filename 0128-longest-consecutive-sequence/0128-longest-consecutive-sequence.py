class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        count = 1
        nums.sort()
        last_smaller = float('-inf')
        for i in range(len(nums)):
            if nums[i]-1 == last_smaller:
                count += 1
                last_smaller = nums[i]
            elif nums[i] != last_smaller:
                count = 1
                last_smaller = nums[i]
            longest = max(longest, count)
        return longest



        # h = {}
        # for i in nums:
        #     h[i] = 1
        # print(h)
        # longest = 0
        # for i in h:
        #     if i-1 not in h:
        #         current = i
        #         count = 0
        #         while current+1 in h:
        #             current += 1
        #             count += 1
        #         longest = max(longest , count+1)
        # return longest

