class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_left = values[0] + 0
        best_pair = 0
        for j in range(1, len(values)):
            best_pair = max(best_pair, max_left + values[j] - j)
            if values[j] + j > max_left:
                max_left = values[j] + j
        return best_pair
