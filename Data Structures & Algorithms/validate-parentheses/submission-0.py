class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        #([{}])

        for ch in s:
            
            if ch in [')', '}', ']']:
                if not stack:
                    return False
                curr_ch = stack.pop()
                if ch == ')' and curr_ch != '(':
                    return False
                if ch == '}' and curr_ch != '{':
                    return False
                if ch == ']' and curr_ch != '[':
                    return False
            else:
                stack.append(ch)

        return len(stack)==0
        