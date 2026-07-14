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
                num1, num2 = token_stack.pop(), token_stack.pop()
                result = ops[token](num2, num1)
                token_stack.append(int(result))
                continue

            token_stack.append(int(token))

        return token_stack[0]