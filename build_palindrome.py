

def build_palindrome(st: str):
    l = st[-1]

    idx = st.index(l)


    # if st+ (st[: idx][::-1]) == (st+ (st[: idx][::-1]))[::-1]:
    #     return st+ (st[: idx][::-1])
    
    
    s = idx
    f = s
    current = st+ (st[: f][::-1])
    modified = current[::-1]

    while current != modified:
        current = st+ (st[: f][::-1])
        modified = current[::-1]

        f = st.index(l,s)
        s += 1
    print(current)
    return current




# print(build_palindrome("abcdc"))
# test.assert_equals(build_palindrome("abcdc"),"abcdcba")
# test.assert_equals(build_palindrome("ababab"),"abababa")

print(build_palindrome("ccgaaegeg"))



# ccgaaegegcc ccgaaegeg -> ccgaaegegeaagcc