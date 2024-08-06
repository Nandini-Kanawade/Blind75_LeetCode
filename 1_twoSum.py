'''
https://leetcode.com/problems/two-sum/description/
1. Two Sum
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, (len(nums))):
        #         if (nums[i]+nums[j]==target):
        #             return [i,j]
        mapp={}
        for i in range(len(nums)):
            x=target-nums[i]
            if x in mapp:
                return [i, mapp[x]]
            mapp[nums[i]]=i
            
        
