class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        sum_ = 0
        i = 1
        count = 0
        while(sum_ <= maxSum  - i and i <= n):
            if i not in banned:
                sum_ += i
                count += 1
            i += 1

        return count
