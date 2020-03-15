import sys

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        ans = 0
        sign = 1
        operand = 0
        stack = []
        for ch in s:
            #print(stack)
            if ch.isdigit():
                operand = 10 * operand + int(ch)    
            elif ch == '+':
                ans += sign * operand
                sign = 1
                operand = 0
            elif ch == '-':
                ans += sign * operand
                sign = -1
                operand = 0
            elif ch == '(':
                stack.append(ans)
                stack.append(sign)
                
                #reset ans, sign
                ans = 0
                sign = 1

            elif ch == ')':
                ans += sign * operand
                ans *= stack.pop()
                ans += stack.pop()
                operand = 0

        return ans + sign * operand

solution = Solution()
print(solution.calculate("1 + 1"))
print(solution.calculate(" 2-1 + 2 "))
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))
print(solution.calculate("(1-(4+5+2)-3)+(6+8)"))
        