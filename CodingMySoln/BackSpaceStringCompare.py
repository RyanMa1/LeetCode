#implement using a stack
#push on to stack wehn iterating through string then pop off when we get a "#"
#edge cases: ?? ????
#stats---------------------------------------------------
#runtime: 28ms runtime beats 87.2% of python3 submissions
#memory usage 13.9 mb, beats 36.1% of python3 submissions
class Solution():
    def backspaceCompare(self, S: str, T: str):
        ansS = ''.join(self.process(S))
        ansT = ''.join(self.process(T))
        return ansS == ansT
    def process(self, stringN):
        stack = []
        for letter in stringN:
            if letter == '#' and len(stack) > 0:
                stack.pop()
            elif letter == '#' and len(stack) == 0:
                continue
            else:
                stack.append(letter)
        return stack

        
test = Solution()
print(test.backspaceCompare(S = "a##c", T = "#a#c"))