class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        answers = [-1 for _ in range(len(queries))]
        i = 0
        for query in queries:
            if query[1] < query[0]:
                query[0], query[1] = query[1], query[0]
            query.append(i)
            i += 1
        queries.sort(key = lambda x: x[1], reverse = True)

        dec_stack = []
        current = len(heights) - 1
        for query in queries:
            i, j, index = query
            if i == j or heights[i] < heights[j]:
                answers[index] = j
            else:
                while(current > j):
                    while(dec_stack and dec_stack[-1][0] <= heights[current]):
                        dec_stack.pop()
                    dec_stack.append([heights[current], current])
                    current -= 1

                while(dec_stack and dec_stack[-1][0] <= heights[j]):
                    dec_stack.pop()
                # print(dec_stack)
                if dec_stack:
                    l, r = 0, len(dec_stack) - 1
                    best_fit = -1
                    while(l <= r):
                        mid = (l + r) // 2
                        if dec_stack[mid][0] > heights[i]:
                            best_fit = dec_stack[mid][1]
                            l = mid + 1
                        else:
                            r = mid - 1
                    answers[index] = best_fit

        return answers


