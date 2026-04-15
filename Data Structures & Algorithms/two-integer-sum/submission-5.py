class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} #val:index
        for index, value in enumerate(nums):
            map[value] = index
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in map) and i != map.get(diff):
                return [i, map.get(diff)]

                