import time
t_start = time.perf_counter()

def len_search(second_line, first_line):
    ind = []
    count = 0
    for i in range(len(first_line)):
        if first_line[i] == second_line:
            ind.append(i)
            count+=1
    if count == 0:
        return('1')
    return(ind, count)

with open("input.txt", 'r') as file:
    first_line = file.readline().rstrip('\n')
    second_line = file.readline()
    first_line = first_line.split()

with open("output.txt", 'w') as file:
    a = len_search(second_line, first_line)
    a = [str(s) for s in a]
    file.write(' '.join(a))
print("Время работы: %s секунд" % (time.perf_counter()-t_start))