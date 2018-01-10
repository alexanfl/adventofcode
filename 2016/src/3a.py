infile = open("../res/3.dat")

cnt = 0

for line in infile:
    a = [ int(x) for x in line.split() ]
    if max(a) < a[a.index(max(a))-1] + a[a.index(max(a))-2]:
        cnt += 1

print(cnt)
