def part3(arr,start,end):
    res=[]
    pivot=arr[start]
    for elem in arr[start:end+1]:
        if elem<pivot:
            res.append(elem)
    i=len(res)
    res.append(pivot)
    for elem in arr[start:end+1]:
        if elem>pivot:
            res.append(elem)
    arr[start:end+1]=res
    return start+i

def quicksort(arr,start,end):

    if start>=end:
        return
    # print(arr[start:end+1],start,end)
    # print(start,end)
    i=part3(arr,start,end)
    # print(i)
    quicksort(arr,start,i-1)
    quicksort(arr,i+1,end)
    print(arr[start:end+1])
arr=[2,5,1,8,0,1,4,5,3,1,0]
arr=[5, 8, 1, 3, 7, 9, 2]
# print(sorted(arr))
# quicksort(arr,0,len(arr)-1)
# print(arr)
quicksort(arr,0,len(arr)-1)

