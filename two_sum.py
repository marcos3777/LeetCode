#1-From two sum
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrNums = {}
        for i, number in enumerate(nums):
            dif = target - number
            if dif in arrNums:
                return [arrNums[dif], i]
            
            arrNums[number] = i

        
        
            
