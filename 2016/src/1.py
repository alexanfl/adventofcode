from numpy import genfromtxt, matmul
inst = genfromtxt("../res/1.dat", dtype='str', delimiter=', ')
r = [0,0]
v = [0,1]
rot = [[ 0, 1],
       [-1, 0]]
R = [r]
S = []

for i in inst:
    v = matmul(rot,v) if i[0] == 'R' else -matmul(rot,v)

    for steps in range(1,int(i[1:])+1):
        for j in R:
            if (r + v*steps).tolist() == j:
                S.append(j)
        R.append((r + v*steps).tolist())

    r += v*int(i[1:])

print(r, '\n',sum(abs(i) for i in r))
print(S[0], '\n',sum(abs(i) for i in S[0]))
