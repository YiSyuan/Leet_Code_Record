# 1
from typing import List

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        for k, x in enumerate(nums):
            for key, value in enumerate(nums):
                if k == key:
                    continue
                
                if x + value == target:
                    return [k, key]
