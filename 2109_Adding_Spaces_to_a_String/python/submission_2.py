class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index = 0
        words = []
        
        for space in spaces:
            words.append(s[index:space])
            index = space
        words.append(s[index:])

        return " ".join(words)
