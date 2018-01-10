from numpy import array, zeros
infile = open("../res/3.dat")

cnt = 0
tmp = 0
a = zeros([3,3])

for line in infile:
    a[tmp, :] = array([ int(x) for x in line.split() ])
    if tmp == 2:
        for i in range(3):
            if max(a[:,i]) < a[a[:,i].tolist().index(max(a[:, i]))-1, i] \
                    + a[a[:,i].tolist().index(max(a[:, i]))-2, i]:
                cnt += 1
        tmp = 0
        a = zeros([3,3])
    else:
        tmp += 1

print(cnt)
