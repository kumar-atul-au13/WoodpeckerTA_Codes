#Question-https://www.hackerrank.com/challenges/the-power-sum/problem
#Video-https://drive.google.com/open?id=1PNGT_8r_A72qd1YmqjE0468Zy70-ElH6

def powerSum(x, n, start=1):
    if x<0:
        return 0
    if x==0:
        print(x,n)
        return 1
    sum=0
    x_root=round(x**(1/n))
    for possible in range(start,x_root+1):
        sum+=powerSum(x-possible**n,n,possible+1)
    return sum

