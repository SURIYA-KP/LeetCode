class Solution:
    def findScore(self, nums: List[int]) -> int:
        p_que = []
        for i, val in enumerate(nums):
            heapq.heappush(p_que, (val, i))
        score = 0
        marked = set()
        while(len(marked) < len(nums)):
            val, i = heapq.heappop(p_que)
            if i not in marked:
                marked.add(i)
                if i + 1 < len(nums):
                    marked.add(i + 1)
                if i > 0:
                    marked.add(i - 1)
                score += val
        return score
