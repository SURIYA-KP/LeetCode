class Solution:
    def maxAverageRatio(self, classes: List[int], extraStudents: int) -> float:
        p_que = []
        for val in classes:
            pas, total = val
            if pas != total:
                heapq.heappush(p_que, (1 / (((pas + 1) / (total + 1)) - pas/total), val))
        
        for _ in range(extraStudents):
            if p_que:
                _, best = heapq.heappop(p_que)
                best[0] += 1
                best[1] += 1
                heapq.heappush(p_que, (1 / (((best[0] + 1) / (best[1] + 1)) - best[0]/best[1]), best))

        total = 0
        for val in p_que:
            _, clas = val
            total += clas[0] / clas[1]
        total += len(classes) - len(p_que)
        return total / len(classes)
