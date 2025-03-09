n = int(input())
array = []
s = []
for i in range(n):
    array.append(i)
    s.append(i)

for i in range(0, n):
    s[array[(n - 1 + i) // 2]] = i + 1
    q = array[i]
    array[i] = array[(n - 1 + i) // 2]
    array[(n - 1 + i) // 2] = q
print(s)