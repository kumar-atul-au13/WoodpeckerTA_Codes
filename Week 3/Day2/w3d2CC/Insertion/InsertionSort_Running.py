#Question-https://www.hackerrank.com/challenges/runningtime
#Video-https://drive.google.com/open?id=1oTRa4ZrGw8lhmKxwQmIoQ8s5dmdx-NIp
"""
In this question we have to count total no of swaps
Insertion sort will go like this
Eg-2 1 3 1 2
First loop-2 1 3 1 2
    Size of sorted array =1
    sorted part= from 0 index to 0 index
    key = 1(i=1 )
    2(0 index) will swap right once, total swap=1
    key(1) will be placed at 0th position
Second loop-1 2 3 1 2
    Size of sorted array =2
    sorted part= from 0 index to 1 index
    key = 3(i=2 )
    Since 1(at 1 index) is smaller than key(3) inner while loop won't run. total swap=0
    and net swap will be zero
Third loop-1 2 3 1 2
    Size of sorted array =3
    sorted part= from 0 index to 2 index
    key = 1(i=3 )
    3 will shift from index 2 to 3, 2 will shift from index 1 to 2  total swap=2
    key(1) will be placed at 1th position
Fourth loop-1 1 2 3 2
    Size of sorted array =4
    sorted part= from 0 index to 3 index
    key = 2(i=4 )
    3 will shift from index 3 to 4,  total swap=1
    key(2) will be placed at 3th position
Final sorted array- 1 1 2 2 3 total swap=1+0+2+1=4
"""
def runningTime(l):
    count=0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
        count+=i-j-1
    return count