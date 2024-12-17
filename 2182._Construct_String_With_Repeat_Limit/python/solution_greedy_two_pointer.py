class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = [0 for _ in range(26)]

        for letter in s:
            counts[ord(letter) - ord('a')] += 1

        output = ''
        j = 26
        for i in range(25, -1, -1):
            while(counts[i] > 0):
                if counts[i] > repeatLimit:
                    output += chr(ord('a') + i) * repeatLimit
                    counts[i] -= repeatLimit
                    while(j >= i or counts[j] == 0):
                        j -= 1
                    if j < 0:
                        return output
                    else:
                        output += chr(ord('a') + j)
                        counts[j] -= 1
                else:
                    output += chr(ord('a') + i) * counts[i]
                    counts[i] = 0
        return output
