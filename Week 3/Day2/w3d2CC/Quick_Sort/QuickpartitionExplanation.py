class bcolors:
    HEADER='\033[95m'
    OKBLUE='\033[94m'
    OKGREEN='\033[92m'
    WARNING='\033[93m'
    FAIL='\033[91m'
    ENDC='\033[0m'
    BOLD='\033[1m'
    UNDERLINE='\033[4m'


def print_util_util(arr):
    res=[]
    for str in arr:
        if len(str)>0:
            res.append(str)
    return " ".join(res)

def print_parted(arr,start,end,pindx):
    before_curr=print_util_util(list(map(str,arr[:start])))
    before_space=" "*len(print_util_util(list(map(str,arr[:start]))))
    shorter=print_util_util(list(map(str,arr[start:pindx])))
    remaining=print_util_util(list(map(str,arr[end+1:])))
    remaining_space=" "*len(arr[end+1:])
    if len(shorter)>0:
        shorter=bcolors.OKGREEN+shorter
    longer=print_util_util(list(map(str,arr[pindx+1:end+1])))
    if len(longer)>0:
        longer=bcolors.OKBLUE+longer
    print(print_util_util([before_space,shorter,bcolors.FAIL+str(arr[pindx]),longer,bcolors.ENDC,remaining_space]))
def print_part_util(arr,left,right,start,end,pvt=False):
    before_curr=print_util_util(list(map(str,arr[:start])))
    before_space=" "*len(print_util_util(list(map(str,arr[:start]))))
    shorter=print_util_util(list(map(str,arr[start:left+1])))
    if len(shorter)>0:
        shorter=bcolors.OKGREEN+shorter
    longer=print_util_util(list(map(str,arr[left+1:right])))
    if len(longer)>0:
        longer=bcolors.OKBLUE+longer
    questioned=str(arr[right])
    before_pivot=print_util_util(list(map(str,arr[right+1:end])))
    pivot=str(arr[end])
    remaining=print_util_util(list(map(str,arr[end+1:])))
    remaining_space=" "*len(arr[end+1:])
    if right<end:
        print(print_util_util([before_space,shorter,longer,bcolors.HEADER+questioned+bcolors.ENDC,before_pivot,
                               bcolors.FAIL+pivot+bcolors.ENDC,remaining_space]))
    else:
        print(print_util_util([before_space,shorter,longer,before_pivot,
                               bcolors.FAIL+pivot+bcolors.ENDC,remaining_space]))
    # if right<end:
    #     print(print_util_util([before_curr,shorter,longer,bcolors.HEADER+questioned+bcolors.ENDC,before_pivot,bcolors.FAIL+pivot+bcolors.ENDC,remaining]))
    # elif pvt:
    #     print(print_util_util([before_curr,shorter,longer,before_pivot,
    #                            bcolors.FAIL+pivot+bcolors.ENDC,remaining]))
    #     print(print_util_util([before_curr,shorter,bcolors.FAIL+pivot,longer+bcolors.ENDC,remaining]))


def part(arr,start,end):
    global shift_quick
    # print(start,end,arr[start:end+1],arr)
    if start==end:
        return start
    pivot=arr[end]

    left,right=start-1,start
    while right<end:
        print_part_util(arr,left,right,start,end)
        if arr[right]<=pivot:
            arr[left+1],arr[right]=arr[right],arr[left+1]
            left+=1
        right+=1
    print_part_util(arr,left,right,start,end,True)
    arr[left+1],arr[end]=pivot,arr[left+1]
    print_parted(arr,start,end,left+1)
    return left+1


def quicksort(arr,start,end):
    if start>=end:
        return
    i=part(arr,start,end)
    quicksort(arr,start,i-1)
    quicksort(arr,i+1,end)


arr=[1,3,9,8,2,7,5]
brr=[5,8,1,3,7,9,2]
quicksort(arr+brr,0,13)
print(*arr)
