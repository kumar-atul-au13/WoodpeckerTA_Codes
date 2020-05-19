#Question-https://www.geeksforgeeks.org/counting-inversions/
#Video-https://drive.google.com/open?id=1UOekhSPpjhjlB6Ze77uL-2SFWy4wgJe6
import sys

sys.setrecursionlimit(100000)
t=int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().strip().split(" ")]
    count=0
    # count2=0


    def merge(arr,brr):
        global count
        # global count2
        lena=len(arr)
        lenb=len(brr)
        res=[]
        ia,ib=0,0

        while ia<lena and ib<lenb:
            if arr[ia]<=brr[ib]:
                res.append(arr[ia])
                ia+=1
                count+=ib
            else:
                res.append(brr[ib])
                ib+=1
                # count2+=lena-ia

        for i in range(ia,lena):
            res.append(arr[i])
            count+=lenb
        for i in range(ib,lenb):
            res.append(brr[i])
        return res


    def mergeSort(arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left_sorted=mergeSort(arr[:mid])
        right_sorted=mergeSort(arr[mid:])
        res=merge(left_sorted,right_sorted)
        return res


    mergeSort(arr)
    print(count)