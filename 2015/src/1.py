infile = open("../res/1.dat")

level = 0
cnt = 0

line = infile.readlines()[0]

for i in line[:-1]:
    cnt += 1
    level = level + 1 if i == "(" else level - 1
    if level == -1:
        print(cnt)

print(level)
