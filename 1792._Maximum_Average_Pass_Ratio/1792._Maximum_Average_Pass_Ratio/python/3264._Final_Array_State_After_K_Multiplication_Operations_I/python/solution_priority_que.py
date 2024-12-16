class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        p_que = []
        for i, val in enumerate(nums):
            heapq.heappush(p_que, (val, i))

        for _ in range(k):
            val, i = heapq.heappop(p_que)
            val *= multiplier
            heapq.heappush(p_que, (val, i))

        for val, i in p_que:
            nums[i] = val

        return nums
