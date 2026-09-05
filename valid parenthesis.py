class Solution:
    def isBalanced(self, s):
        # code here
        stack=[]
        if len(s)==1:
            return False
        for ch in s:
            if ch=='[' or ch=='{' or ch=='(':
                stack.append(ch)
           
            elif ch==']':
                if len(stack)==0:
                    return False
                elif stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            elif ch=='}':
                if len(stack)==0:
                    return False
                elif stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            else:
                if len(stack)==0:
                    return False
                elif stack[-1]=='(':
                    stack.pop()
                else:
                    return False
        else:
            
            if(len(stack)==0):
                return True
            else:
                return False
            
        