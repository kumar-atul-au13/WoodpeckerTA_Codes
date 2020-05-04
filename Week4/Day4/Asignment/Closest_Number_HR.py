#Question-https://www.hackerrank.com/challenges/closest-numbers/problem
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