class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ("(", "{", "["):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == "(":
                    if i != ")":
                        return False
                    else:
                        stack.pop()
                elif stack[-1] == "[":
                    if i != "]":
                        return False
                    else:
                        stack.pop()
                elif stack[-1] == "{":
                    if i != "}":
                        return False
                    else:
                        stack.pop()

        return len(stack) == 0


# Closing bracket must follow last opening
# Ensure stack non-empty
