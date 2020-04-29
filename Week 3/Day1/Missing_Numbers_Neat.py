# https://www.hackerrank.com/challenges/missing-numbers/problem
def missingNumbers(arr,brr):
    carr = [0]*101
    minb=min(brr)
    for b in brr:
        carr[b-minb] += 1

    for a in arr:
        carr[a-minb] -= 1

    return [indx+minb for indx,cnt in enumerate(carr) if cnt>0]

arr=[int(x) for x in "203 204 205 206 207 208 203 204 205 206".split()]
brr=[int(x) for x in "203 204 204 205 206 207 204 205 201 205 208 203 206 205 206 204".split()]
print(missingNumbers( arr,brr))
