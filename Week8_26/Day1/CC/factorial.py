#Video- Missed recording on june 4th

res=[None]*10
res[0:2]=[1,1]
def factorial(n):
    if n<=1:
        return res[n]
    if not res[n]:
        res[n]=factorial(n-1)*n
    return res[n]
print(factorial(9))
print(res)



res=[1,1]
def fact(n):
    for i in range(2,n+1):
        res.append(res[-1]*i)
    return res[-1]
print(fact(9))
print(res)


#
def fact_optim(n):
    temp=1
    for i in range(1,n+1):
        temp*=i
    return temp
print(fact_optim(9))