#implement using a stack
#push on to stack wehn iterating through string then pop off when we get a "#"
#edge cases: ?? ????
#stats---------------------------------------------------
#runtime: 28ms runtime beats 87.2% of python3 submissions
#memory usage 13.9 mb, beats 36.1% of python3 submissions
class Solution():
    def backspaceCompare(self, S: str, T: str):
        stackS = []
        stackT = []
        for letter in S:
            if letter == '#' and len(stackS) > 0:
                stackS.pop()
            elif letter == '#' and len(stackS) == 0:
                continue
            else:
                stackS.append(letter)
        for letter in T:    
            if letter == '#' and len(stackT) > 0:
                stackT.pop()
            elif letter == '#' and len(stackT) == 0:
                continue
            else:
                stackT.append(letter)
        if ''.join(stackS) == ''.join(stackT):
            return True
        return False
test = Solution()
print(test.backspaceCompare(S = "a##c", T = "#a#c"))