#Target time cmplexity O(n*n)
"""This approach is like traversing arr, finding each elements of arr in brr and
deleting the match from brr
So, at last we will be left with numbers in brr which has been dropped from arr, of course with
repetition and in the original order
So, to remove duplicates we will make a set from brr and sort it using sorted()
Here we are passing set to sorted function and sorted is returning a list"""
def missingNumbers1(arr, brr=[]):
    for a in arr:       #consumes O(len(arr))
        brr.remove(a)       #consume O(len(brr))
    return sorted(set(brr))# sorted function runs in nlog(n)
#Line 10 and 11 time complexity is O(len(arr)*len(brr) which will be overall time complexity

#Targe time complexity O(n)
def missingNumbers(arr,brr):
    carr = [0]*101  #short for count array
    res = []
    minb,maxb=min(brr), max(brr)
    # carr=        [1,    0,  2,  1,  0....]
    # Actual Index  0     1   2   3
    # value from b=[200,201,202,203,204....] So we are mapping values of b to index by subtracting minb
    # minb is 200 in this case
    #value from arr or brr will always act as an index of carr after subtracting minb
    for b in brr:
        carr[b-minb] += 1

    #In following three lines I am printing the carr with it's index and corresponding brr value(if present)
    for indx,cnt in enumerate(carr):
        print(*(minb+indx,indx,"count=",cnt,),end="|")
    print()

    #Decreasing count, as we are encountering same elements while traversing arr
    for a in arr:
        carr[a-minb] -= 1

    #printing the count after subtracting the count of elements from arr
    for indx,cnt in enumerate(carr):
        print(*(minb+indx,indx,"count=",cnt,),end="|")
    print()

    for indx,cnt in enumerate(carr):
        if cnt>0:
            res.append(indx+minb)

    return res




arr=[int(x) for x in "203 204 205 206 207 208 203 204 205 206".split()]
brr=[int(x) for x in "203 204 204 205 206 207 204 205 200 205 208 203 206 205 206 204".split()]
print(missingNumbers( arr,brr))
