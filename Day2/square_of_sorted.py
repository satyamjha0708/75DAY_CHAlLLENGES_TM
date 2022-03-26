# Problem No 977
# Problem of Day2
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        i=0
        j=len(nums)-1
        
        
        while i<=j:
            if abs(nums[i])>=abs(nums[j]):
                l.append(nums[i]*nums[i])
                i+=1
                
            else:
                l.append(nums[j]*nums[j])
                j-=1
                
            
            
        return l[::-1]
