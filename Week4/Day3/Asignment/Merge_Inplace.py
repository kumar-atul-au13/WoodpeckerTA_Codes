#Video-PENDING
#Covered-False
def merge(arr,starta,enda,startb,endb):
    while startb<=endb:
        print(arr,arr[starta],arr[startb])
        if arr[starta]<=arr[startb]:
            starta+=1
        else:
            temp=arr[startb]
            for i in range(enda,starta-1,-1):
                print(arr[i])
                arr[i+1]=arr[i]
            arr[starta]=temp
            startb+=1
            starta+=1
            enda+=1
arr=[1,3,5,7,9,2,4,6,8]
merge(arr,0,4,5,8)
print(arr)