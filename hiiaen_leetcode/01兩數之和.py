"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
"""

# 解法1（暴力）
from typing import List, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[list[int]]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    continue

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # 输出: [0, 1]
print(solution.twoSum([3, 2, 4], 6))      # 输出: [1, 2]
print(solution.twoSum([3, 3], 6))         # 输出: [0, 1]


# 解法2（字典）
class Solution2:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, nums in enumerate(nums):
            if target - nums in h:
                return [i, h[target - nums]]

            h[nums] = i
        return []