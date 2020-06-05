#Question-https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0

tt=int(input())
for _ in range(tt):
    ln=int(input())
    arr=[int(x) for x in input().strip().split()]
    res=[]
    for i in range(ln):
        mx=0
        for j in range(0,i):
            if arr[j]<arr[i] and res[j]>mx:
                mx=res[j]
        if mx>0:
            res.append(mx+1)
        else:
            res.append(1)
    print(res)