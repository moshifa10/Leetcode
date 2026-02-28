def fibonacci_gen(n):
    fibs= []

    for i in range(n):
        if len(fibs) < 2:
            fibs.append(i)

        else:
            fibs.append(fibs[-2] + fibs[-1])

    
    if n == 1:
        return
    
    fibonacci_gen(n-1)

    return fibs

print(fibonacci_gen(7))