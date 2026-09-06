class Solution:
    def minParentheses(self, s):
        # code here
        stack=[]
        c=0
        for ch in s:
            if  ch=='(' :
                stack.append(ch)
            elif ch==')' and len(stack)==0:
                stack.append(ch)
            
            elif ch==')' and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(ch)
       
        c=len(stack)
            
        return c