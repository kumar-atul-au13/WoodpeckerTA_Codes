#Question-https://www.hackerrank.com/challenges/recursive-digit-sum/problem
#While solution also possible
#Video-https://drive.google.com/open?id=10lXLLEMFdR4y8qYO85YSfzM9c3yZ8PoC
import time
def superDigit(n, k):
    sm=0
    for ch in n:
        sm+=int(ch)
    return rec_super_digit(sm*k)
def rec_super_digit(n):
    # print(n)
    if n<10:
        return n
    sm=0
    n_str=str(n)
    for ch in n_str:
        sm+=int(ch)
    return rec_super_digit(sm)

def superDigit1(n, k):
    sm=0
    for ch in n:
        sm+=int(ch)
    num=sm*k
    while num>=10:
        sm=0
        n_str=str(num)
        for ch in n_str:
            sm+=int(ch)
        num=sm
    return sm
start_time=time.time()
print(superDigit('9875'*100000, 4))
print(time.time()-start_time)
start_time=time.time()
print(superDigit1('9875'*100000, 4))
print(time.time()-start_time)
