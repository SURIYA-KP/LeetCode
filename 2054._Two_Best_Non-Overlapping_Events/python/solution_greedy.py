class Solution:
    def maxTwoEvents(self, events):
        timeline = []
        for event in events:
            timeline.append([event[0], 1, event[2]])
            timeline.append([event[1] + 1, 0, event[2]])
        best_total, best_prev = 0, 0
        timeline.sort()
        for time in timeline:
            if time[1]:
                best_total = max(best_total, time[2] + best_prev)
            else:
                best_prev = max(best_prev, time[2])

        return best_total
