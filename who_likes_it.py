def likes(names):
    # your code here
    main = "likes this"
    if len(names) == 0:
        return f"no one {main}"
    
    if len(names) == 1:
        return f"{''.join(names)} {main}"
    
    if len(names) == 2:
        last = names[-1]
        return f"{', '.join(names[:len(names)])} {main}"
    
    else:
        first_2 = names[:3]
        after = names[3:]
        print(names)
        return f"{','.join(first_2) and {len(after)}}"
    


print(likes(['Jacob', 'Alex']))