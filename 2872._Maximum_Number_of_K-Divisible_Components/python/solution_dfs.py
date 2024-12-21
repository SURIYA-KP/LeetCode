class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        def dfs(current, prev):
            current_chunks, current_sum = 0, 0
            for adjacent in adj_list[current]:
                if adjacent != prev:
                    new_chunks, new_sum = dfs(adjacent, current)
                    if new_sum % k == 0:
                        new_chunks += 1
                        new_sum = 0
                    current_chunks += new_chunks
                    current_sum += new_sum
            return current_chunks, current_sum + values[current]

        chunks, _ = dfs(0, -1)
        return chunks + 1
