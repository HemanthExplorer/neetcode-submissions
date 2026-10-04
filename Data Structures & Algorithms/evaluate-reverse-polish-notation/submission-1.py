class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in "+-*/":
                v1, v2 = int(stack.pop()), int(stack.pop())
                if ch == "+": res = v2 + v1
                elif ch == "*": res = v2 * v1
                elif ch == "-": res = v2 - v1
                elif ch == "/": res = int(v2 / v1)
                stack.append(int(res))
            else: 
                stack.append(ch)

        return int(stack.pop())
        
