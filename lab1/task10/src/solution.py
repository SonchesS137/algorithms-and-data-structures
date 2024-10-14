import time
t_start = time.perf_counter()

def palindrom_count (dict):
    count_l = {}
    for i in dict:
        if i in count_l:
            count_l[i] +=1
        else:
            count_l[i] = 1
    return count_l

def build_palindrom (dict):
    half = []
    middle = None
    for letter, count in dict.items():
        if count % 2 == 0:
            half.append(letter * (count // 2))
        else:
            half.append(letter * (count // 2))
            if middle is None:
                middle = letter
    half = ''.join(half)
    right_half = half[::-1]

    if middle:
        return half + middle + right_half
    else:
        return half + right_half

with open("input.txt", 'r') as file:
    first_line = file.readline().rstrip('\n')
    second_line = file.readline()
    second_line = sorted(second_line, key=lambda x: x.lower())
    dict = ''.join(second_line)

with open("output.txt", 'w') as file:
    a = palindrom_count(second_line)
    dict = palindrom_count(second_line)
    file.write(build_palindrom(dict))

print(build_palindrom(dict))
print("Время работы: %s секунд" % (time.perf_counter()-t_start))