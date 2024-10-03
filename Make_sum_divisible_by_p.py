#1590. Make Sum Divisible by P
from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p

        if remainder == 0:
            return 0

        prefix_sum = 0
        min_length = len(nums)
        prefix_dict = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num
            current_remainder = prefix_sum % p
            needed_remainder = (current_remainder - remainder) % p

            if needed_remainder in prefix_dict:
                subarray_length = i - prefix_dict[needed_remainder]
                min_length = min(min_length, subarray_length)

            prefix_dict[current_remainder] = i

        return min_length if min_length < len(nums) else -1
