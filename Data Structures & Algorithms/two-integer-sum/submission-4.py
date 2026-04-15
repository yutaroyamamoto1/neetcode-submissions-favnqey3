class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in lst:
                return [lst.index(difference),i]
            else:
                lst.append(nums[i])

                