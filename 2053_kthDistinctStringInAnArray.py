'''
https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
2053. Kth Distinct String in an Array
'''

class Solution:
    def kthDistinct(self,arr: list[str], k: int) -> str:
        freq={}
        for i in arr:
            if (i in freq):
                freq[i] += 1
            else:
                freq[i]=1
        print(freq)
        x=[]
        for i in freq.keys():
            if (freq.get(i)==1):
                x.append(i)
        if (len(x)<k):
            return ""
        else:
            return x[k-1]
