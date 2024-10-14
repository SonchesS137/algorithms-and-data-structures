import time
t_start = time.perf_counter()

def swap(second_line, first_line):
    for i in range(1, first_line):
        n = second_line[i]
        j = i - 1
        while (j >= 0 and n > second_line[j]):
            second_line[j + 1] = second_line[j]
            j = j - 1
        second_line[j + 1] = n

    return second_line

with open("input.txt", 'r') as file:
    first_line = int(file.readline().rstrip('\n'))
    second_line = (file.readline())
    second_line = second_line.split()
    second_line = [int(x) for x in second_line]
with open("output.txt", 'w') as file:
    a = swap(second_line, first_line)
    a = [str(s) for s in a]
    file.write(' '.join(a))

print("Время работы: %s секунд" % (time.perf_counter()-t_start))