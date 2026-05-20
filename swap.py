
'''

    Check if one string swap can make strings equal

        You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarrily different ) and swap  the charaactors  at these indices 
        Return True if it is possinle to make both stri gs equal by performing at most  one string swap on exactly one og the strings. Otherwise  return False

        Example 2:
        Input s1 = "bank", s2 = "kanb"
        Output= True
        Swap first with last

'''

def swap(s1: str, s2: str) -> bool:
    if s1 == s2:return True
    if len(s1) != len(s2): return False
    for i in range(len(s2)):
        for j in range(i+1,len(s2)):
            save =  list(s2)
            save[i] = s2[j]
            save[j] = s2[i]

            if "".join(save) == s1:
                return True
            
    return False
 

print(swap("ab", "ba"))

            

