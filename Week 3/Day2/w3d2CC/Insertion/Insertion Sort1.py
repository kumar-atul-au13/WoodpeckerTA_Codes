#Question Name- Insertion Sort- Part 1
#Question- https://www.hackerrank.com/challenges/insertionsort1/problem
#Video-https://drive.google.com/open?id=1wGB_jgfIG1Nq5NtRe7W9x7C0KyLRxYoe
"""
In this question we are given an array of which all the elements are sorted except the last
element(called key) and we have put that key in right position.
To insert the key to it's right position we have to move all elements from second last to
key's final position, one position to the right.
And this is what this question asks ie. to show the step
Array needs to be printed after every shift.
"""
def insertionSort1(n, arr):
    key=arr[-1]
    shiftin_index=n-2  #First element to be shifted is second last elements
    #What can be the last possible element to be shifted?-> element at 0th index in case key is smallest
    #So shiftin_index will decrease till 0
    while shiftin_index>=0 and arr[shiftin_index]>key:
        arr[shiftin_index+1]=arr[shiftin_index]
        print(*arr)
        shiftin_index-=1
    arr[shiftin_index+1]=key
    print(*arr)