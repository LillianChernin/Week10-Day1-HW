def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibList = [0, 1]
        for i in range(n):
            fibList.append((fibList[i] + fibList[i + 1]))
        return(fibList[n])
