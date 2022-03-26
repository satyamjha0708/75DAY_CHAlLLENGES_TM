# Problem No 169
# Problem of Day2


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        return nums[len(nums)//2]
    
    