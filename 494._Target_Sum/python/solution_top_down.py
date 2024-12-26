class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def getways(index, new_target):
            if index == len(nums):
                if new_target == 0:
                    return 1
                else:
                    return 0
            return getways(index + 1, new_target - nums[index]) + getways(index + 1, new_target + nums[index])

        return getways(0, target)
