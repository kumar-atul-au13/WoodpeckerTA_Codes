#Question-https://www.hackerrank.com/challenges/closest-numbers/problem
#Video-https://drive.google.com/open?id=1-iM4ZRHa1-So76J_QJ6YWm2E33mm9PfY
def closestNumbers(arr):
    arr.sort()
    print(arr)
    initialize=True;
    diff=arr[1]-arr[0]
    res=[arr[0],arr[1]]
    for indx,elem in list(enumerate(arr))[1:-1]:
        print(res,diff)
        if arr[indx+1]-elem==diff:
            res.append(elem)
            res.append(arr[indx+1])
        elif arr[indx+1]-elem<diff:
            res=[]
            res.append(elem)
            res.append(arr[indx+1])
            diff=arr[indx+1]-elem
    return res

print(closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]))
#Using two for loop (easy one)
def closestNumbers(arr):
    arr.sort()
    minimum=arr[1]-arr[0]
    res=[]
    for indx in range(len(arr)-1):
        if arr[indx+1]-arr[indx]<minimum:
            minimum=arr[indx+1]-arr[indx]
    for indx in range(len(arr)-1):
        if minimum==arr[indx+1]-arr[indx]:
            res.append(arr[indx])
            res.append(arr[indx+1])
    return res
print(closestNumbers([5,4,3,2]))