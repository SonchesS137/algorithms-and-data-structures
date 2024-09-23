
import sys
sys.setrecursionlimit(400000)
import time
t_start = time.perf_counter()
def calc_fib(n, fib={}):
    if n in fib :
        return fib[n]
    if n <=1:
        return n
    fib[n] = (calc_fib(n - 1, fib) + calc_fib(n - 2, fib))%10
    return fib[n]


n = int(input())
print(calc_fib(n))
print("Время работы: %s секунд" % (time.perf_counter()-t_start))
