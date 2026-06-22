class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                b = stack.pop()  # popped second operand
                a = stack.pop()  # popped first operand
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))  # truncate toward zero
            else:
                stack.append(int(token))
        
        return stack[0]
