def fibs():
    if n =1:
        fibs(1) = 0
    fibs(n) = fib(n-1)+fibs(n-2)
print(fibs(10))
