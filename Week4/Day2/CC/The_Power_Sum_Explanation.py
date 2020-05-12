class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# print(powerSum(100,2,1))
#Mistake?sm
#Three parameter, In question there are2. What to do?
# res=[]
# def power_sum_print(x, n, start=1,pdata=0,select=0):
#     print((" "*7*pdata+str(x)+" born "+str(select)).rjust(7))
#     if x<0:
#         return 0
#     if x==0:
#         # print(res)
#         return 1
#     sm=0
#     x_root=round(x**(1/n))
#     for possible in range(start,x_root+1):
#         # res.append(possible)
#         sm+=power_sum_print(x-possible**n,n,possible+1,pdata+1,possible)
#         # res.pop()
#     print((" "*7*pdata+str(x)+" Dead "+str(select)).rjust(7))
#     return sm
# print(power_sum_print(100,3))

res=[]
def prnt_util(res,space=6):
    if len(res)==0:
        return ""
    ans=(" "*space).join(res)
    ans=" "*(space//2)+ans+" "*(space//2)
    ans=bcolors.OKGREEN+ans+bcolors.ENDC
    return ans
def power_sum_print(x, n, start=1,pdata=0,select=0):
    global res
    print((prnt_util(res)+str(x)+" born ").rjust(7))
    if x<0:
        print("Fail")
        return 0
    if x==0:
        print("Sucess-returning")
        return 1
    sm=0
    x_root=round(x**(1/n))
    # print(list(range(start,x_root+1)))
    for possible in range(start,x_root+1):
        res.append(str(possible))
        sm+=power_sum_print(x-possible**n,n,possible+1,pdata+1,possible)
        res.pop()
    print((prnt_util(res)+str(x)+" Dead ").rjust(7))
    return sm
# print(power_sum_print(100,3))
print(power_sum_print(100,2))



