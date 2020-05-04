class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def print_util(arr,key_indx):
    print(bcolors.BOLD+bcolors.HEADER+" ".join(list(map(str,arr[:key_indx])))+bcolors.OKGREEN+" "+str(arr[key_indx])+bcolors.ENDC,*arr[key_indx+1:] )
def print_util1(arr,indx):
    print(*arr[:indx],bcolors.OKBLUE+str(arr[indx])+">"+str(arr[indx+1])+bcolors.ENDC,*arr[indx+2:])
def insertionSort(arr):
    for key_indx in range(1,len(arr)):
        print_util(arr,key_indx)
        key=arr[key_indx]
        while arr[key_indx-1]>key and key_indx>0:
            arr[key_indx]=arr[key_indx-1]
            key_indx-=1
            print_util1(arr,key_indx)
        arr[key_indx]=key
        print(*arr[:key_indx],bcolors.OKBLUE+str(arr[key_indx])+bcolors.ENDC,*arr[key_indx+1:])
    return arr
print(bcolors.HEADER+ "pink"+bcolors.ENDC+"=sorted"+bcolors.OKGREEN+" green"+bcolors.ENDC+"=key"+bcolors.OKBLUE+" blue"+bcolors.ENDC+"=shifting")
print(insertionSort([6,5,1,3,1,9,0]))
print()
# print(insertionSort([3,4,5,6,2,1]))