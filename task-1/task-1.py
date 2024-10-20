def caching_fibonacci():
    cache = {}

    def fibonacci(n: int):
        try:
            fibo = [0]

            if n in cache.keys(): return cache[n]
            elif n == 0: return fibo
            else: fibo.append(1)


            while len(fibo) < n:
                fibo.append(fibo[-1] + fibo[-2])
            cache[n] = fibo
            print(cache)
            return cache[n]
        except Exception as e:
            return e
    return fibonacci

fib = caching_fibonacci()

print(fib(11))
print(fib(12))
print(fib(10))
print(fib(11))





