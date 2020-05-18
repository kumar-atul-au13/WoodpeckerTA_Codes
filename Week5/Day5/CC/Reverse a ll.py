#Question-https://www.geeksforgeeks.org/reverse-a-linked-list/
pair_count=0
def merge(arr,brr):
    lena=len(arr)
    lenb=len(brr)
    res=[]
    ia,ib=0,0

    while ia<lena and ib<lenb:
        if arr[ia]<brr[ib]:
            res.append(arr[ia])
            ia+=1
        else:
            res.append(brr[ib])
            ib+=1
    for i in range(ia,lena):
        res.append(arr[i])
    for i in range(ib,lenb):
        res.append(brr[i])
    print(res,arr,brr)
    return res
def mergeSort(arr):
    mid=len(arr)//2
    left_sorted=mergeSort(arr[:mid])
    right_sorted=mergeSort(arr[mid:])
    res=merge(left_sorted,right_sorted)
    return res