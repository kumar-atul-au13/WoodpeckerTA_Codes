def part(arr,start,end):
    # print(start,end,arr[start:end+1],arr)
    if start==end:
        return start
    pivot=arr[end]
    left,right=start-1,start
    while right<end:
        if arr[right]<=pivot:
            arr[left+1],arr[right]=arr[right],arr[left+1]
            left+=1
        right+=1
    # for shift in range(start+1,left+1):
    #     arr[shift-1]=arr[shift]
    # arr[left]=pivot
    arr[left+1],arr[end]=pivot,arr[left+1]
    # print(start,end,arr[start:end+1],arr,arr[left])
    print(arr,start,end)
    return left+1

def quicksort(arr,start,end):

    if start>=end:
        return
    # print(arr[start:end+1],start,end)
    # print(start,end)
    i=part(arr,start,end)
    # print(i)
    quicksort(arr,start,i-1)
    quicksort(arr,i+1,end)
    # print(arr[start:end+1])

arr=[1, 3, 9, 8, 2, 7, 5]
# print(sorted(arr))
# quicksort(arr,0,len(arr)-1)
# print(arr)
quicksort(arr,0,len(arr)-1)

