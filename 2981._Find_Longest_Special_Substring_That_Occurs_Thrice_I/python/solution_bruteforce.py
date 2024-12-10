class Solution:
    def maximumLength(self, s: str) -> int:
        letter = [[] for _ in range(26)]
        max_ = [0 for _ in range(26)]
        prev = s[0]
        count = 0
        for alpha in s:
            if alpha == prev:
                count += 1
            else:
                letter[ord('a') - ord(prev)].append(count)
                max_[ord('a') - ord(prev)] = max(max_[ord('a') - ord(prev)], count)
                count = 1
                prev = alpha
        letter[ord('a') - ord(prev)].append(count)
        max_[ord('a') - ord(prev)] = max(max_[ord('a') - ord(prev)], count)

        best = -1
        for i in range(26):
            if max_[i] > 0:
                top = max_[i]
                for j in range(top, 0, -1):
                    count = 0
                    for val in letter[i]:
                        if val - j +1 > 0:
                            count += val - j +1
                    if count >= 3:
                        best = max(j, best)
                        break
        return best
