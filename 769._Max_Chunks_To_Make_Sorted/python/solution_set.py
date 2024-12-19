class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        num_map = set()
        for i in range(len(arr)):
            if i not in num_map:
                num_map.add(i)
            else:
                num_map.remove(i)
            val = arr[i]
            if val not in num_map:
                num_map.add(val)
            else:
                num_map.remove(val)

            if not num_map:
                chunks += 1

        return chunks
