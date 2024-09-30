with open("input.txt", 'r') as file:
    data = file.read().replace('\n', '')
a = data.split()
num1 = int(a[0])
num2 = int(a[1])
result = num1 + num2
with open("output.txt", 'w') as file:
    file.write(str(result))
