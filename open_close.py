
def is_balanced(source: str, caps: str) -> bool:
    # print(source, caps)
    # count = [1 for i in source if i in caps]
    # if len(count) != len(caps) and len(count) != 0:
    #     return False
    
    stack = []
    for i in source:
        if i in caps:
            if caps.index(i) % 2 == 0:
                stack.append(i)
                
            else:
                if caps[(caps.index(i) -1)] == stack[-1]:
                    stack.pop(-1)
            
                else: return False

    return True


# // In this case '(' opens a section, and ')' closes a section
# print(is_balanced("(Sensei says yes!)", "()"))       #=> true
# print(is_balanced("(Sensei says no!", "()"))         #=> false

# # // In this case '(' and '[' open a section, while ')' and ']' close a section
# print(is_balanced("(Sensei [says] yes!)", "()[]"))   #=> true
# print(is_balanced("(Sensei [says) no!]", "()[]"))    #=> false

# # // In this case a single quote (') both opens and closes a section
# print(is_balanced("Sensei says 'yes'!", "''") )      #=> true
# print(is_balanced("Sensei say's no!", "''"))         #=> falseis_balanced

print(is_balanced("(Hello Mother can you hear me?)[Monkeys, in my pockets!!](Gosh!!)", "()[]"))