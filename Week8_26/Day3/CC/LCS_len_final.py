t=int(input())
for tt in range(t):
    m,n=[int(x) for x in input().strip().split()]
    str1=input()
    str2=input()
    dp=[[0]*(len(str2)+1) for _ in range(2)]
    def lcs(str1, str2, m, n):
        i=1
        while i<=m:
            j=1
            while j<=n:
                if str1[i-1]==str2[j-1]:
                    dp[1][j]=1+dp[0][j-1]
                else:
                    # print("hai")
                    dp[1][j]=max(dp[0][j],dp[1][j-1])
                j+=1
            dp[0]=dp[1]
            dp[1]=[0]*(len(str2)+1)
            i+=1
        return dp[0][-1]

    print(lcs(str1,str2,m,n))