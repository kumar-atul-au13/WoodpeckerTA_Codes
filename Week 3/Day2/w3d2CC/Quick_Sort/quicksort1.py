#Question-https://www.hackerrank.com/challenges/quicksort1
#Video-[Start Time 4:50]https://drive.google.com/open?id=1LcuasCoKJrBBQ8x1Yid4cppQg5uMAtL6
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