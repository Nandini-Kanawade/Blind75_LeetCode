'''
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/description/
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=len(nums)
        for i in range(1,l):
            nums[i] = nums[i-1] + nums[i]
        return nums
