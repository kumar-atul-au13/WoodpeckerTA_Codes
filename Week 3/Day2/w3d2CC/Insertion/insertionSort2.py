def insertionSort(arr):
    for key_indx in range(1,len(arr)):
        key=arr[key_indx]
        while arr[key_indx-1]>key and key_indx>0:
            arr[key_indx]=arr[key_indx-1]
            key_indx-=1
        arr[key_indx]=key
        print(arr)
        return arr
