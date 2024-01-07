class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            if token not in "+-*/":
                num_stack.append(int(token))
            else:
                right = num_stack.pop()
                left = num_stack.pop()
                if token == "+":
                    new_operand = right + left
                    num_stack.append(new_operand)
                if token == "-":
                    new_operand = left - right
                    num_stack.append(new_operand)
                if token == "*":
                    new_operand = right * left
                    num_stack.append(new_operand)
                if token == "/":
                    new_operand = int(left / right)
                    num_stack.append(new_operand)
        return num_stack[0]

# Apply to last 2 elements in stack
