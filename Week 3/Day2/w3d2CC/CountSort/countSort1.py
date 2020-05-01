#Question-https://www.hackerrank.com/challenges/countingsort1/problem
#Video-[Time 11:00] https://drive.google.com/open?id=1oTRa4ZrGw8lhmKxwQmIoQ8s5dmdx-NIp
#In this question we have to make count_arr
#Value of arr will be represented as indexes of count_arr
#and frequency of occurrence will be corresponding values in count_arr
def countingSort(arr):
    count_arr=[0]*100
    # [[0]*4 for i in range(4)]
    for elem in arr:
        count_arr[elem]+=1
    return count_arr