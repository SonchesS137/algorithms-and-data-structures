def dist(x1, y1, x2, y2):
    distance = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    return distance
def sort(s):
    s = sorted(s)
    mid = len(s)//2
    left = s[0:mid]
    right = s[mid:len(s)]
    min_dist_left = min_dist_right = 100
    print(left)
    print(right)
    for i in range(len(left)-2):
        for j in range(i+1, len(left)):
            a = dist(left[i][0], left[i][1], left[j][0], left[j][0])
            print(a)
            if a < min_dist_left:
                min_dist_left = a
    for i in range(len(right)-2):
        for j in range(i+1, len(right)):
            b = dist(right[i][0], right[i][1], right[j][0], right[j][0])
            if b < min_dist_right:
                min_dist_right = b
    mid_dist = dist(left[-1][0], left[-1][1], right[0][0], right[0][0])
    return min_dist_left, min_dist_right, mid_dist

s = []
with open("input.txt", 'r') as file:
    first_line = int(file.readline().rstrip('\n'))
    while True:
        line = file.readline()
        if not line:
            break
        s.append(line.strip().split())
for i in range(len(s)):
    for j in range(0, 2):
        s[i][j] = int(s[i][j])

print(sorted(s))
print(min(sort(s)))