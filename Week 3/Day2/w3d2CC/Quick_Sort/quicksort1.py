def quickSort(arr):
    before=[]
    equal=[]
    after=[]
    pivot=arr[0]
    for ch in arr:
        if ch==pivot:
            equal.append(ch)
        elif ch<pivot:
            before.append(ch)
        else:
            after.append(ch)
    before.extend(equal)
    before.extend(after)
    return before
print(quickSort([4, 5, 3, 7, 2]))