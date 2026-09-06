class Solution:
    def removePair(self, s):
        stack=[]
        f=''
        ans=''
        for ch in s:
            if len(stack)==0:
                stack.append(ch)
            else:
                if stack[-1]==ch:
                    stack.pop()
                else:
                    stack.append(ch)
        while(len(stack)!=0):
            f+=stack.pop()
        for i in range(len(f)-1,-1,-1):
            ans+=f[i]
        if len(ans)==0:
            return "-1"
        
        return ans
            
        