import time
t_start = time.perf_counter()

def sel_sort(second_line, first_line):
    n = int(first_line)
    k = 0
    while k!= n-1:
        m = min(second_line[k::])
        ind = second_line.index(m)
        second_line[k], second_line[ind] = second_line[ind], second_line[k]
        k+=1
    return second_line

with open("input.txt", 'r') as file:
    first_line = file.readline().rstrip('\n')
    second_line = file.readline().split()
    second_line = [int(x) for x in second_line]

with open("output.txt", 'w') as file:
    a = sel_sort(second_line, first_line)
    a = [str(s) for s in a]
    file.write(' '.join(a))

print("Время работы: %s секунд" % (time.perf_counter()-t_start))