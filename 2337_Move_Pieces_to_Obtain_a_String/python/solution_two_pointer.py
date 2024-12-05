class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j = -1, -1

        while(i < len(start) and j < len(start)):
            i, j = i + 1, j + 1
            while(i < len(start) and start[i] == '_'):
                i += 1
            while(j < len(target) and target[j] == '_'):
                j += 1

            if i == len(start) or j == len(target):
                return i == j
            
            if target[j] == 'L':
                if not (start[i] == 'L' and i >= j):
                    return False
            
            else:
                if not (start[i] == 'R' and i <= j):
                    return False

        return False
