class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(2 * stack[-1])
            elif i == "+":
                stack.append(stack[-2] + stack[-1])
            else:
                stack.append(int(i))
        return sum(stack)
            
            