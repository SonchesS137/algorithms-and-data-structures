import time
t_start = time.perf_counter()

with open("input.txt", 'r') as file:
  first_line = int(file.readline().rstrip('\n'))
  second_line = file.readline()
  second_line = second_line.split()
  A = [int(x) for x in second_line]
c = 1
k = 1
A = sorted(A)
l = A[:len(A)//2:]
r = A[len(A)//2::]
for i in range(len(l)-1, -1, -1):
    if l[i]==l[i-1]:
        c+=1
    else:
        break
for j in range(1, len(r)):
    if r[j]==r[j-1]:
        k+=1
    else:
        break
if k+c > len(A)//2:
    with open("output.txt", 'w') as file:
        file.write('1')
else:
    with open("output.txt", 'w') as file:
        file.write('0')
print("Время работы: %s секунд" % (time.perf_counter()-t_start))