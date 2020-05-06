#Question-https://www.hackerrank.com/challenges/countingsort4
#Video-[23:00] https://drive.google.com/open?id=1yeml3IWLbPFQMAuy9-5VosdSfZGHq-El
def countSort(arr):
    count_arr=[0]*100
    # [[0]*4 for i in range(4)]
    for inner_arr in arr[:len(arr)//2]:
        inner_arr[1]='-'
    for elem in arr:
        elem[0]=int(elem[0])
        count_arr[elem[0]]+=1
    for indx,elem in enumerate(count_arr[1:],1):
        count_arr[indx]+=count_arr[indx-1]
    res=[0]*len(arr)
    for inner_arr in arr[::-1]:
        res[count_arr[inner_arr[0]]-1]=inner_arr[1]
        count_arr[inner_arr[0]]-=1
    return res
print(countSort([['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], ['0', 'to'], ['1', 'be'], ['5', 'question'], ['1', 'or'], ['2', 'not'], ['4', 'is'], ['2', 'to'], ['4', 'the']]))
