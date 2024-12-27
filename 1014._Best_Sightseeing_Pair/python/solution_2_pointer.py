class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        i, j = 0, 1
        best_pair = 0
        for j in range(1, len(values)):
            if values[i] - (j - i - 1) - values[j - 1] < 0:
                i = j - 1
            best_pair = max(best_pair, values[i] + values[j] + i - j)
        return best_pair
            
