#Video-https://drive.google.com/open?id=1KCkTPZFZHmKcTuKfA1fnuQVZycpcdCo2
#Video2-https://drive.google.com/open?id=1nCIpVyuZN9sgzEQc35R3yHHncKTeoZwy
import time

n=10

def binary_search_rec(arr,srch):
    mid=len(arr)//2
    if len(arr)==0:
        return None #no need
    if arr[mid]==srch:
        return mid
    if arr[mid]>srch:
        return binary_search_rec(arr[:mid],srch)
    elif arr[mid]<srch:
        temp=binary_search_rec(arr[mid+1:],srch)
        if temp is not None:
            return mid +1 + temp
start_time=time.time()
# print(binary_search_rec(list(range(n)),n))
# print(time.time()-start_time)

def binary_search_itter(arr,srch):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==srch:
            return mid
        if arr[mid]>srch:
            high=mid-1
        elif arr[mid]<srch:
            low=mid+1
    return None
start_time=time.time()
# print(binary_search_itter(list(range(n)),n))
# print(time.time()-start_time)

#Simple way of writing Binary_search recursion:
found_index=0
def binary_search_rec1(arr,srch,low,high):
    global found_index
    if low>high:
        found_index= -1
    else:
        mid=(low+high)//2
        if arr[mid]==srch:
            found_index=mid

        elif arr[mid]>srch:
             binary_search_rec1(arr,srch,low,mid-1)
        else:
             binary_search_rec1(arr,srch,mid+1,high)
print(binary_search_rec1(list(range(n)),11,0,n-1))
print(found_index)

