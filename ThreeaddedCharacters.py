


def added_char(s1, s2):  
    
    for i in s2:
        if i not in s1:
            return i
        
        elif s2.count(i) != s1.count(i):
            return i




string1 = "aabbcc"
string2 = "aacccbbcc"
# // => 'c'


'''test.assert_equals(added_char("hello","checlclo"),'c')
test.assert_equals(added_char("aabbcc","aacccbbcc"),'c')
test.assert_equals(added_char("abcde","2db2a2ec"),'2')'''

print(added_char("abcde","2db2a2ec"))