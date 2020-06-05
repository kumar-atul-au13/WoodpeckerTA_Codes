#Question-https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
def callsum(arr,given_sum=None):
    tsm=sum(arr)
    if given_sum:
        sm=given_sum
    else:
        sm=tsm/2
    if sm>tsm:
        return False
    dp=[[False]*(sm+1) for _ in range(len(arr)+1)]
    for row_i in range(len(arr)+1):
        for col_j in range(sm+1):

            if col_j==0:# if the sum is zero
                dp[row_i][col_j]=True
                continue
            if arr[row_i-1]<=col_j:
                dp[row_i][col_j]=dp[row_i-1][col_j] or dp[row_i-1][col_j-arr[row_i-1]]
    i=0
    print(map(str,range(10)))
    for row in dp:
        print(str(arr[i-1]).rjust(2), end=" ")
        i+=1
        print(row)

callsum([2,3,4,7],9)





