class Solution:
    def canChange(self, start: str, target: str) -> bool:
        prev_space = 0
        start_idx, target_idx = 0, 0
        R_que = []
        while(start_idx < len(start) and start[start_idx] == '_'):
            start_idx += 1
            prev_space += 1
        while(target_idx < len(target) and target[target_idx] == '_'):
            target_idx += 1

        while(start_idx < len(start) and target_idx < len(target)):
            start_letter, target_letter = start[start_idx], target[target_idx]
            if start_letter != target_letter:
                return False

            if R_que and start_idx == R_que[0]:
                R_que.pop(0)

            if target_letter == 'L':
                if prev_space < 0 :
                    return False
                diff = start_idx - target_idx
                if 0 <= diff <= prev_space and not len(R_que):
                    prev_space = diff
                else:
                    return False

            else:
                diff = target_idx - start_idx
                if diff == 0:
                    prev_space = 0
                elif diff > 0:
                    R_que.append(target_idx)
                    prev_space = -diff
                else:
                    return False

            start_idx += 1
            target_idx += 1

            while(start_idx < len(start) and start[start_idx] == '_'):
                if R_que and start_idx == R_que[0]:
                    R_que.pop(0)
                start_idx += 1
                prev_space += 1
            while(target_idx < len(target) and target[target_idx] == '_'):
                target_idx += 1

        while(start_idx < len(start)):
            if start[start_idx] != '_':
                start_idx += 1
                return False
        while(target_idx < len(target)):
            if target[target_idx] != '_':
                target_idx += 1
                return False

        return True

            
