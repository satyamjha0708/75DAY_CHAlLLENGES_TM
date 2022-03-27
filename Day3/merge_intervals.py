# Problem of Day 3
# Problem No 56
class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:
        
        interval.sort(key=lambda x:x[0])
        
        m=[]
        i=1
        start=interval[0][0]
        end=interval[0][1]
        while i<len(interval):
            if end>=interval[i][0]:
                end=max(end,interval[i][1])
                
                
            else:
                m.append([start,end])
                start=interval[i][0]
                 end=interval[i][1]
                
            
                
            i+=1
                
                
        m.append([start,end])
        
        
        
        return m
                
        
                          
                          
        print(m)
                
        