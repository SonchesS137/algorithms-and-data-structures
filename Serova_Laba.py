s = input().split()
a = int(s[0])
b = int(s[1])
if (a or b) <= 10**9 and (a or b) >= -10**(9):
    print(a + b)

s = input().split()
a = int(s[0])
b = int(s[1])
if (a or b) <= 10**9 and (a or b) >= 10**(-9):
    print(a + b**2)


file_in = open("input.txt", 'r')
file_out = open("output.txt", 'w')
with open("input.txt", 'r') as file:
    data = file.read().replace('\n', '')
a = data.split()
num1 = int(a[0])
num2 = int(a[1])
print(num1+num2)









import time
t_start = time.perf_counter()
def calc_fib(n, fib={}):
    if n in fib :
        return fib[n]
    if n <=1:
        return n
    fib[n] = calc_fib(n - 1, fib) + calc_fib(n - 2, fib)
    return fib[n]


n = int(input())
print(calc_fib(n))
print("Время работы: %s секунд" % (time.perf_counter()-t_start))



