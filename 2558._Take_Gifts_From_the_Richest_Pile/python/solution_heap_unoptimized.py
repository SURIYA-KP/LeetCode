class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] *= -1
        heapq.heapify(gifts)
        for i in range(k):
            val = heapq.heappop(gifts)
            val *= -1
            val = math.floor(math.sqrt(val))
            heapq.heappush(gifts, -val)

        return -sum(gifts)
