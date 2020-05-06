#Question-https://www.hackerrank.com/challenges/quicksort4
#Video-https://drive.google.com/open?id=1NRoLDuaHj-86DQte9qp3YO0_2cUl9NHc
n=int(input())
arr=[int(x)for x in input().split()]
shift_quick=0
def part(arr,start,end):
    global shift_quick
    # print(start,end,arr[start:end+1],arr)
    if start==end:
        return start
    pivot=arr[end]
    left,right=start-1,start
    while right<end:
        if arr[right]<=pivot:
            arr[left+1],arr[right]=arr[right],arr[left+1]
            left+=1
            shift_quick+=1
        right+=1
    arr[left+1],arr[end]=pivot,arr[left+1]
    shift_quick+=1
    # print(start,end,arr[start:end+1],arr,arr[left])
    # print(arr,start,end)
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

def runningTime(l):
    countInsert=0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
        countInsert+=i-j-1
    return countInsert
quicksort(arr[::],0,len(arr)-1)
print(runningTime(arr[::])-shift_quick)



