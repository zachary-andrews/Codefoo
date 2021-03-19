import sys
import math


class brackets:
    def check(self, bracketString: str) -> str:
        dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        open_bracket_list = "({["
        stack = []
        for bracket in bracketString:
            if bracket in open_bracket_list:
                stack.append(bracket)
            else:
                if stack[-1] != dict.get(bracket):
                    return "No"
                else:
                    stack.pop()
        if len(stack) > 0:
            return "No"
        else:
            return "Yes"
