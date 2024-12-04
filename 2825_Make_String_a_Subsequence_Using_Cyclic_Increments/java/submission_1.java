class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False
        i, j = 0, 0
        next_letter = {chr(97 + i): chr(i + 98) for i in range(25)}
        next_letter['z'] = 'a'
        while(i < len(str1) and j < len(str2)):
            if str1[i] == str2[j] or next_letter[str1[i]] == str2[j]:
                j += 1
            i += 1
        return j == len(str2)
