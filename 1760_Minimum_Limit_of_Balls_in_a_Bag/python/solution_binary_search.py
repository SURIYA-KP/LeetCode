class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        max_bags = min(len(nums) + maxOperations, sum(nums))
        l, r = 1, max(nums)
        penality = 0
        while(l < r):
            mid = (l + r) // 2
            num_bags = 0
            for val in nums:
                num_bags += (val + mid - 1) // mid
            if num_bags > max_bags:
                l = mid + 1
            elif num_bags <= max_bags:
                r = mid
        return l
