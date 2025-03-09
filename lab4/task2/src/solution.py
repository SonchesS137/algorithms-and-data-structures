list = []
result = []
with open("input.txt", 'r') as file:
    first_line = int(file.readline().rstrip('\n'))
    c = 0
    while c!= first_line:
        s = file.readline().rstrip()
        if s[0]=='+':
            list.append(s[2:])
        else:
            a = list.pop(0)
            result.append(a)
        c+=1

with open("output.txt", 'w') as file:
    file.writelines(f"{i}\n" for i in result)