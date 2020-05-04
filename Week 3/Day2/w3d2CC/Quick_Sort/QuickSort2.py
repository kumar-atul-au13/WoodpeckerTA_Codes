# def part(arr,start,end):
#     # print(start,end,arr[start:end+1],arr)
#     if start==end:
#         return start
#     pivot=arr[start]
#     left,right=start,start+1
#     while right<=end:
#         if arr[right]<=pivot:
#             arr[left+1],arr[right]=arr[right],arr[left+1]
#             left+=1
#         right+=1
#     # for shift in range(start+1,left+1):
#     #     arr[shift-1]=arr[shift]
#     # arr[left]=pivot
#     arr[left],arr[start]=pivot,arr[left]
#     # print(start,end,arr[start:end+1],arr,arr[left])
#     return left
# def part1(arr,start,end):
#     start_cpy=start
#     pivot=arr[start]
#     while start<end:
#         if arr[start]<=pivot:
#             start+=1
#         elif arr[end]>pivot:
#             end-=1
#         else:
#             arr[start],arr[end]=arr[end],arr[start]
#     if arr[start]>pivot:
#         arr[start-1],arr[start_cpy]=arr[start_cpy],arr[start-1]
#         return start-1
#     else:
#         arr[start],arr[start_cpy]=arr[start_cpy],arr[start]
#         return start
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

