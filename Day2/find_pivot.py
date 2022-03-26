# Problem No 724
# Problem of Day2

class Solution:
    def pivotIndex(self, l: List[int]) -> int:
       
        for i in range(len(l)):
            if sum(l[:i])==sum(l[i+1:]):
                return i


        else:
            return -1