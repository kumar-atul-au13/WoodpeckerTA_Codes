#Question Link-https://www.hackerrank.com/challenges/icecream-parlor/problem
#Video Link-https://drive.google.com/open?id=1qz5xc_cQCcTS9thKSjxcFpBwe5ZAjUuF
#O(N^2) Complexity
#Let's say we have array of length 5 so the indexes will be 0,1,2,3,4
#So, in this approach we will checking the sum in following order
#Outer for loop (line 15) will run 4=len(arr[:-1]) times
#First loop of line 6- first_indx=0: pairs whose sum will be checked are (0 1)(0 2)(0 3)(0 4)
#Second loop first_indx=1 pairs are(1 2)(1 3)(1 4)
#Third loop  first_indx=2 pairs are(2 3)(2 3)
#Fourth loop first_indx=3 pairs are(3 4)
#At any point of these loop if match is found then function returns
#Notice in all the pair of indexes above later one is greater as requested by question
def icecreamParlor1(total,arr):
    #last element is removed as it can't form pairs with element after the last elements
    for first_indx,first in enumerate(arr[:-1]):
        sec_indx=first_indx+1
        while sec_indx<=len(arr)-1:
            if first+arr[sec_indx]==total:
                return first_indx+1,sec_indx+1
            sec_indx+=1
print(icecreamParlor1(3,[1,2]))

#Actual Solution Time complexity O(N)
#We used set to keep track of already visited Elements
#While traversing array we check whether it's other pair(ie. total-curr_element) is already present or not
#When we find the match our goal is to return the index
#For that we will use enumerate(arr) and curr_indx will be always appear after the index of match found
#as viseted set contains elements visited before curr_element
#To get the index of match found, we will use index method on arr
def icecreamParlor(total,arr):
    visited=set()
    for curr_indx,curr_elem in enumerate(arr):  #O(n)
        if total-curr_elem in visited:          #in O(1)
            return arr.index(total-curr_elem)+1,curr_indx+1
        visited.add(curr_elem)

print(icecreamParlor(11,[1,2,5,3,6,7]))