class Solution:
    def twoSum(self, nums: List[int], target: int) :
        mp={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in mp:
                return [mp[complement], i]
            mp[num] = i