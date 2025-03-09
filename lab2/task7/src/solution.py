A = [1, 4, 5, 2, 8, 0, 2]
a = A
A = A[0:-1]
maximum = []
for i in range(0, len(A)):
    for j in range(i+1, len(A)):
        if sum(maximum)<sum(A[i:j]):
            maximum = A[i:j]
if sum(maximum)<(sum(a)):
    maximum = a
print(maximum)