class Solution:
    def remove_special_consecutive(self, arr, x, y):
        # code here
   
        stack=[]
        for i in range(len(arr)):
            if arr[i]==x and len(stack)==0:
                stack.append(arr[i])
            elif arr[i]==y and len(stack)==0:
                stack.append(arr[i])
            elif arr[i]==x and stack[-1]==x:
                continue
            elif arr[i]==y and stack[-1]==y:
                continue
            else:
                stack.append(arr[i])
        return stack