class Solution:
    def maxLength(self, arr):
        # code here
        maxlen=0
        cs=0
        dict={}
        for i in range(len(arr)):
            cs+=arr[i]
            if cs==0:
                maxlen=max(i+1,maxlen)
            if cs not in dict:
                dict[cs]=i
            else:
                maxlen=max(i-dict[cs],maxlen)
        return maxlen