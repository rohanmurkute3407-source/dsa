class Solution:
    def nextLargerElement(self, arr):
        # code here
        final=[-1]*len(arr)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            if(len(stack)==0):
                stack.append(arr[i])
                final[i]=-1
            else:
                while(len(stack)>0 and stack[-1]<=arr[i]):
                    stack.pop()
                if(len(stack)==0):
                    stack.append(arr[i])
                    final[i]=-1
                else:
                    final[i]=stack[-1]
                    stack.append(arr[i])
            
        return final
