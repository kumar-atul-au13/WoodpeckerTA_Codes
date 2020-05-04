#Question-https://www.hackerrank.com/challenges/recursive-digit-sum/problem
#While solution also possible
def superDigit(n, k):
    sm=0
    for ch in n:
        sm+=int(ch)
    return rec_super_digit(sm*k)
def rec_super_digit(n):
    if n<10:
        return n
    sm=0
    n_str=str(n)
    for ch in n_str:
        sm+=int(ch)
    return rec_super_digit(sm)

print(superDigit('9875', 4))