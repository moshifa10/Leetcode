def find_it(seq):
    m = {key: seq.count(key) for key in seq}
    
    return [d for d,c in m.items() if not c%2==0][0]



print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))