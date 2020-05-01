#Question-https://www.hackerrank.com/challenges/correctness-invariant
#video-[Time 19:00] https://drive.google.com/open?id=1wGB_jgfIG1Nq5NtRe7W9x7C0KyLRxYoe
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j > 0) and (l[j] > key): #j>=0 '=' was missing
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
#Find the mistake
#First run the code and see what's wrong
#Well every thing is sorted except the first element
#Compare this code with first Insertion Sort1.py
#In while loop j>0 will be changed to j>=0 All done!