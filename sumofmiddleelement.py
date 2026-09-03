class Solution:
    def findMidSum(self, arr1, arr2):
        left=0
        right=0
        c=0
        first=0
        second=0
        while(left<len(arr1) and right<len(arr2)):
            if(arr1[left]>arr2[right]):
                c+=1
                if(c==len(arr1)):
                    first=arr2[right]
                elif(c==len(arr1)+1):
                    second=arr2[right]
                    return(first+second)
                right+=1
            else:
                c+=1
                if(c==len(arr1)):
                    first=arr1[left]
                elif(c==len(arr1)+1):
                    second=arr1[left]
                    return(first+second)
                left+=1
        if(left==len(arr1)):
            while(right<len(arr2)):
                c+=1
                if(c==len(arr1)):
                    first=arr2[right]
                elif(c==len(arr1)+1):
                    second=arr2[right]
                    return(first+second)
                right+=1
        if(right==len(arr1)):
            while(left<len(arr2)):
                c+=1
                if(c==len(arr1)):
                    first=arr1[left]
                elif(c==len(arr1)+1):
                    second=arr1[left]
                    return(first+second)
                left+=1
                    
            
        
