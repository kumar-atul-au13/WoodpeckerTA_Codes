def countingSort(arr):
    count_arr=[0]*100
    # [[0]*4 for i in range(4)]
    for elem in arr:
        count_arr[elem]+=1
    for indx,elem in enumerate(count_arr[1:],1):
        count_arr[indx]+=count_arr[indx-1]

    return count_arr
countingSort([5,2,3,5,2,2,4,6,6,6,8,8])