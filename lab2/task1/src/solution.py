import time
t_start = time.perf_counter()

def merge_sort(A):
  if len(A) <= 1:
    return A
  left = A[:len(A)//2]
  right = A[len(A)//2:]
  l = merge_sort(left)
  r = merge_sort(right)
  return merge(l, r)

def merge(left, right):
  result = []
  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)
  if left:
    result += left
  if right:
    result += right
  return result

with open("input.txt", 'r') as file:
  first_line = int(file.readline().rstrip('\n'))
  second_line = file.readline()
  second_line = second_line.split()
  A = [int(x) for x in second_line]

with open("output.txt", 'w') as file:
  a = merge_sort(A)
  a = [str(s) for s in a]
  file.write(' '.join(a))

print("Время работы: %s секунд" % (time.perf_counter()-t_start))

