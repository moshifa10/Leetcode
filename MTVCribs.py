# '''     /\
#        /  \
#       /    \
#      /______\  number of floors 3
#      |      |
#      |      |
#      |______|
# '''


# '''     /\
#     /  \
#    /    \
#   /______\  number of floors 3
#   |      |
#   |      |
#   |______|

#      /\
#     /  \
#    /____\
#    |    |   2 floors
#    |____|

#      /\
#     /__\    1 floor
#     |__|
# '''
# '''
#      /\
#     /__\    1 floor
#     |__|'''

# test.assert_equals(my_crib(1), " /\\ \n/__\\\n|__|")
# test.assert_equals(my_crib(2), "  /\\  \n /  \\ \n/____\\\n|    |\n|____|")
# test.assert_equals(my_crib(3), "   /\\   \n  /  \\  \n /    \\ \n/______\\\n|      |\n|      |\n|______|")

# print("   /\\   \n  /  \\  \n /    \\ \n/______\\\n|      |\n|      |\n|______|")
# print(" /\\ \n/__\\\n|__|")

# def my_crib(n):
    
#     space = n
#     d = n+n
#     ticks = n+1
#     inside_space = 0

#     down_ticks = n
    
#     for i in range(1, n+1):
#         print(f"{" "*space}{"/"}{" "*inside_space}{"\\"}")
#         if space == 1:
#             # print(f"{" "* space}{"/"}{"-"*inside_space}{"\\"}")
#             break
#         space-=1
#         inside_space +=2
    
#     print(f"{" "* space}{"/"}{"-"*inside_space}{"\\"}")

#     for i in range(1,n+1):
#         if i == n:
#             print(f"{" "*space}{"|"}{"_"*inside_space}{"|"}")
#         else:
#             print(f"{" "*space}{"|"}{" "*inside_space}{"|"}")
# def my_crib(n):
    
#     space = n+1
#     d = n+n
#     ticks = n+1
#     inside_space = 0

#     down_ticks = n
    
#     for i in range(1, n+1):
#         print(f"{" "*space}{"/"}{" "*inside_space}{"\\"}")
#         if space == 1:
#             break
#         space-=1
#         inside_space +=2
    
#     print(f"{" "* space}{"/"}{"_"*inside_space}{"\\"}")

#     for i in range(1,n+1):
#         if i == n:
#             print(f"{" "*space}{"|"}{"_"*inside_space}{"|"}")
#         else:
#             print(f"{" "*space}{"|"}{" "*inside_space}{"|"}")
# my_crib(3)

def my_crib(n):
    
    space = n+1
    d = n+n
    ticks = n+1
    inside_space = 0
    
    down_ticks = n
    house = ""
    
    for i in range(1, n+1):
        house +=f'{" "*space}/{" "*inside_space}\\ \n'
        if space == 1:
            break
        space-=1
        inside_space +=2
    
    house +=f'{" "* space}/{"_"*inside_space}\\ \n'

    for i in range(1,n+1):
        if i == n:
            house += f'{" "*space}|{"_"*inside_space}| \n'
        else:
            house += f'{" "*space}|{" "*inside_space}| \n'
            
    return house
print(my_crib(3))