import time
t_start = time.perf_counter()
def bubble_sort(second_line, first_line):
    n = first_line
    st = []
    for i in range(0, n-1):
        for j in range (n-1-i):
            while second_line[j]>second_line[j+1]:
                second_line[j], second_line[j+1] = second_line[j+1], second_line[j]
                data = ["Swap elements at indices", j, "and", j+1]
                string = ''
                for el in data:
                    string += str(el)
                    string += ' '
                st.append(string)
                st = [str(s) for s in st]
                with open("output.txt", 'w') as file:
                    file.write('\n'.join(st))
    return second_line


data = []
with open("input.txt", 'r') as file:
    first_line = int(file.readline().rstrip('\n'))
    second_line = file.readline()
    second_line = second_line.split()
    second_line = [int(x) for x in second_line]

print('No more swaps needed')
print("Время работы: %s секунд" % (time.perf_counter()-t_start))