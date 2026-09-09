class Solution:
    def countDistinct(self, arr, k):
        dict={}
        list=[]
        for i in range(0,k):
            if arr[i] not in dict:
                dict[arr[i]]=1
            else:
                dict[arr[i]]+=1
        list.append(len(dict))
        for i in range(k,len(arr)):
            
            if arr[i] not in dict:
                dict[arr[i]]=1
                dict[arr[i-k]]-=1
                if(dict[arr[i-k]]==0):
                    del dict[arr[i-k]]
                list.append(len(dict))
            else:
                dict[arr[i]]+=1
                dict[arr[i-k]]-=1
                if(dict[arr[i-k]]==0):
                    del dict[arr[i-k]]
                list.append(len(dict))
        return list
        