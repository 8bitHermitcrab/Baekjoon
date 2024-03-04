class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        
        for box, i in boxTypes:
            if box <= truckSize:
                ans += box * i
                truckSize -= box
            else:
                ans += truckSize * i
                break
            
        return ans