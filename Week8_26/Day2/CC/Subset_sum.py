#Question-https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
def callsum(arr,given_sum=None):
    tsm=sum(arr)
    if given_sum:
        sm=given_sum
    else:
        if tsm%2==1:
            return
        sm=tsm/2
    if sm>tsm:
        return False
    dp=[[False]*sm for _ in range(len(arr))]


