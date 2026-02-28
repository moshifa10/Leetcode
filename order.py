
def order(sentence):
  
  # code here
    s = {
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None
    }
    sentence = sentence.split()
    for i in s: 
        for k in sentence:
            if str(i) in k:
                s[i] = k
                break
    
    return " ".join(list(filter(lambda x: x is not None, list(s.values()))))
    # print(s)

print(order("is2 Thi1s T4est 3a"))