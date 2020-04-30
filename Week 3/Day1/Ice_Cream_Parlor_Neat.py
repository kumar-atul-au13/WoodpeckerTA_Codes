def icecreamParlor(total,arr):
    visited=set()
    for indx,curr_elem in enumerate(arr):
        if total-curr_elem in visited:
            return arr.index(total-curr_elem)+1,indx+1 #added 1 to make one based index
        visited.add(curr_elem)