class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for ch in tokens:
            if ch not in '+-*/':
                stack.append(int(ch))
            elif ch in '+-*/' and len(stack) > 0:
                n2 = stack.pop()
                n1 = stack.pop()
                
                if ch == '+':
                    stack.append(n1+n2)
                elif ch == '-':
                    stack.append(n1-n2)
                elif ch == '*':
                    stack.append(n1*n2)
                elif ch == '/':
                    stack.append(int(n1/n2))
        
        if len(stack) > 0:
            res = stack.pop()
        return res