class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def mult(a, b):
            return a * b
        def plus(a, b):
            return a + b
        def subtract(a, b):
            return a - b
        def divide(a, b):
            return int(a / b)

        operations = {"*": mult, "+": plus, "-": subtract, "/": divide}
        stack = []
        for token in tokens:
            if token in operations:
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    curTotal = operations[token](b, a)
                    stack.append(curTotal)
            else:
                stack.append(int(token))
        return stack[0]
