class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_val = 0
        for i in range(len(arr)):
            max_val = max(max_val, arr[i])
            if max_val == i:
                chunks += 1
        return chunks
