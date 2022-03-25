
# Problem No 121
# Problem for Day 1


class Solution:
    def maxProfit(self,prices):
        b=0
        ans=0
        s=1
        while s<len(prices):
            curr=prices[s]-prices[b]
            if prices[s]>prices[b]:
                ans=max(ans,curr)
                
            else:
                b=s
            
            s+=1
                
        return ans