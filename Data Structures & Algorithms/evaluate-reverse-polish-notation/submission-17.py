import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        token_stack = []
        

        for token in tokens:
            if token in ops:
                num1, op, num2 = int(token_stack.pop()), token, int(token_stack.pop())
                result = ops[op](num2, num1)
                token_stack.append(result)
                continue

            token_stack.append(token)

        return int(token_stack[0])