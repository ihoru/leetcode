# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

from ic import ic

ic

import math


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = math.prod(nums)
        if product == 1:
            return nums
        elif product != 0:
            return [
                product // nums[i]
                for i in range(len(nums))
            ]
        else:
            return [
                math.prod(nums[:i]+nums[i+1:])
                for i in range(len(nums))
            ]
