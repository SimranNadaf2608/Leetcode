class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = ''
        for i in digits:
            val = val + str(i) 
        # print(val)
        val = str(int(val)+1)
        # print(val) 
        d = []
        for i in val:
            s = int(i)
            d.append(s)
        return d


        
        
        