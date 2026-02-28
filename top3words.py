
def top_3_words(text):
    text = text.lower().split()
    unwanted_word = "@#$%&*()\/!~ "
    combine = [i for i in text if i not in unwanted_word]
    # print(combine)
    g = [(i , combine.count(i)) for i in combine]
    g = sorted(list(set(g)) ,key=lambda x: x[-1], reverse=True)
    # print(g)
    so = [g[i][0] for i in range(3)]
    # print(so, "ok")
    for i in g[3:]:
        # print(i[-1])
        print(g[2])
        if g[2][-1] == i[-1]:
            so.append(i[])

        else:
            break

    print(so)
    return so
    
    
# top_3_words()


# print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
'''
top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
test.assert_equals(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
test.assert_equals(top_3_words("  //wont won't won't "), ["won't", "wont"])
(top_3_words("  ...  "), [])
test.assert_equals(top_3_words("  , e   .. "), ["e"])
'''