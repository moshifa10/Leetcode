
def find_even_index(arr):
    
    for i in range(len(arr)):
        # if i == 0 or i == len(arr)-1:
        #     continue
            
        arr1, arr2 = arr[:i], arr[i+1:]
        
        if sum(arr1) == sum(arr2):
            return i


    return -1

print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([1,100,50,-51,1,1]))
print(find_even_index([1,2,3,4,5,6]))
print(find_even_index([20,10,30,10,10,15,35]))
print(find_even_index([20,10,-80,10,10,15,35]))



# test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
#         test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
#         test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
#         test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
#         test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
#         test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
#         test.assert_equals(find_even_index(list(range(1,100))),-1)
#         test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
#         test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
#         test.assert_equals(find_even_index(list(range(-100,-1))),-1)
#         test.assert_equals(find_even_index([8,8]),-1)
#         test.assert_equals(find_even_index([8,0]),0)
#         test.assert_equals(find_even_index([0,8]),1)
#         test.assert_equals(find_even_index([7,3,-3]),0)
#         test.assert_equals(find_even_index([8]),0)
#         test.assert_equals(find_even_index([10,-10]),-1)
#         test.assert_equals(find_even_index([-3,2,1,0]),3)
#         test.assert_equals(find_even_index([-15,5,11,17,19,-17,20,-6,17,-17,19,16,-15,-6,20,17]),8)