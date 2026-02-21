def count_smileys(arr):
    #pass #the number of valid smiley faces in array/list

    # c = False
    # n = False # Optional nose
    # f = False

    count = 0

    for i in arr:
        got = False
        if (":" in i or  ";" in i) and (")" in i or "D" in i):
            for j in i:
                if j not in [":",";",")","D","-","~"]:
                    got = True
                    break

            if not got:
                count +=1

    return count

print(count_smileys( [';-(', ':-(', ';oD', ':(', ':D', ':-D', ';D', ';D', ':D', ':o(', ':(', ';-(', ':D', ';(', ':oD']))
            



'''test.assert_equals(count_smileys([]), 0)
test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)'''