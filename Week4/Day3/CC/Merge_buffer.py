arr=[9,10,11,12,None,None,None,None]
brr=[0,2,4,8]
crr=[-12,-9,10,11,None,None,None,None]
drr=[-4,0,2,8]

def merge_buffer(arr,brr):
    arr_elem_size=0
    for elem in arr:
        if elem is not None:
            arr_elem_size+=1
    ai=arr_elem_size-1

    bi=len(brr)-1
    l_pos=-1
    while bi>=0:
        print(ai,bi)
        if ai>=0 and arr[ai]>brr[bi]:
            arr[l_pos]=arr[ai]
            ai-=1
        else:
            arr[l_pos]=brr[bi]
            bi-=1
        l_pos-=1
        print(arr)
    return arr
print(merge_buffer(arr,brr))
print(merge_buffer(crr,drr))