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
def merge_itter(arr):
    i=1
    while i<=len(arr):
        for j in range(0,len(arr),2*i):
            arr[j:j+2*i]=merge(arr[j:j+i],arr[j+i:j+2*i])
        i+=1
arr=[2,5,1,2,6,2,3]
merge_itter(arr)



