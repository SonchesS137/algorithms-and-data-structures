s = input().split()
a = int(s[0])
b = int(s[1])
if (a or b) <= 10**9 and (a or b) >= -10**9:
    print(a + b**2)
