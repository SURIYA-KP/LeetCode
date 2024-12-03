class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ""
        output += s[0: spaces[0]]
        for i in range(1, len(spaces)):
            output += " " + s[spaces[i - 1]: spaces[i]]
        output += " " + s[spaces[-1]:]

        return output
