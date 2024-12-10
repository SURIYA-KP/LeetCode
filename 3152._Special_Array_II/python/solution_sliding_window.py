class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        max_reach = []
        prev = nums[0] % 2

        for i, num in enumerate(nums[1:]):
            current = num % 2
            if current == prev:
                while(len(max_reach) < i + 1):
                    max_reach.append(i)
            else:
                prev = current

        print(max_reach)

        while(len(max_reach) < len(nums)):
            max_reach.append(len(nums) - 1)

        answers = []
        for query in queries:
            if max_reach[query[0]] >= query[1]:
                answers.append(True)
            else:
                answers.append(False)
        print(max_reach)
        return answers
