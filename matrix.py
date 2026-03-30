
'''

Check if every row and column contains all numbers

An nxn matrix is valid if every row and every column contains all the intergers from 1 to n inclusive
return True or False if the matrix is invalid

Example 1 :
    input matrix =  [[1,2,3], [3,1,2], [2,3,1]]
    Output = True

    Explanation: In this case n=3 and every row and column contains the numbers 1,2 and 3 hence we return True
'''


def matrix(m: list[list[int]]) -> bool:

    valid = [i for i in range(1, len(m)+1 )]
    
    for i in range(len(m)):
        if sorted(m[i]) != valid:
            return False
        save = []
        for j in range(len(m[i])):
            save.append(m[j][i])

        if sorted(save) != valid:
            return False
        
    return True



print(matrix([[1,2,3], 
        [4,1,2], 
        [2,3,1]])
)
