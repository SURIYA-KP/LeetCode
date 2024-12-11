2779._Maximum_Bclass Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        limit = 2 * k
        l, r = 0, 0
        max_beauty = 0
        for r in range(len(nums)):
            if nums[r] - nums[l] <= 2 * k:
                continue 
            else:
                max_beauty = max(max_beauty, r - l)
                while(l <= r and nums[r] - nums[l] > 2 * k):
                    l += 1
        max_beauty = max(max_beauty, r - l + 1)
        return max_beauty
