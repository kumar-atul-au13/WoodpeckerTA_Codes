#Question-https://www.hackerrank.com/challenges/countingsort2/problem
#Video-[Time 17:00] https://drive.google.com/open?id=1oTRa4ZrGw8lhmKxwQmIoQ8s5dmdx-NIp
#Refer video for explanations
def countingSort(arr):
    count_arr=[0]*100
    res=[]
    # [[0]*4 for i in range(4)]
    for elem in arr:
        count_arr[elem]+=1
    for elem,freq in enumerate(count_arr):
        while freq>0:
            res.append(elem)
            freq-=1
    return res