#https://www.geeksforgeeks.org/construct-all-possible-bsts-for-keys-1-to-n/
#Video: https://drive.google.com/file/d/1LdECD6ZcXG0HlKyY_p_NbkGx2udkM-DE/view?usp=sharing

def all_possible_bst(start,end):
    if start>end:
        return [[]]
    ans=[]
    for root in range(start,end+1):#root-2
        larr=all_possible_bst(start,root-1)#-- 3
        rarr=all_possible_bst(root+1,end)#-- 4
        for lcomb in larr:
            lcomb.insert(0,root)
            for rcomb in rarr:
                ans.extend([lcomb+rcomb])# lcomb and rcomb are arrays
    return ans
print(all_possible_bst(1,4))

