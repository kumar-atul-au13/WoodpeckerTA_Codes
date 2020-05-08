class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
space=0
def print_util(arr):
    global space
    mid=len(arr)//2
    print(" "*4*space+" ".join(map(lambda x:x.rjust(3),map(str,arr[:mid])))+bcolors.OKGREEN+" "+str(arr[mid]).rjust(3)+" "+bcolors.ENDC+str(' '.join(map(lambda x:x.rjust(3),map(str,arr[mid+1:])))))
    print(" "*4*space+" ".join(map(lambda x:x.rjust(3),map(str,range(space,space+mid))))+" "+str(space+mid).rjust(3)+" "+str(' '.join(map(lambda x:x.rjust(3),map(str,range(mid+1+space,len(arr)+space))))))
    print()

def binary_search_rec(arr,srch):
    global space
    mid=len(arr)//2
    if len(arr)==0:
        return None #no need
    print_util(arr)
    if arr[mid]==srch:
        return mid
    if arr[mid]>srch:
        return binary_search_rec(arr[:mid],srch)
    elif arr[mid]<srch:
        space+=mid+1
        temp=binary_search_rec(arr[mid+1:],srch)
        if temp is not None:
            return mid +1 + temp
print(binary_search_rec(list(range(100,200,3)),127))#find 100 ie first and last element
# print(binary_search_rec([1,4,7,90],90))