from numpy import zeros

infile = open("../res/6.dat")

N = 1000
grid = zeros([N,N])

def toggle(x1,y1,x2,y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            grid[i,j] += 2

def off(x1,y1,x2,y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            grid[i,j] = grid[i,j] - 1 if grid[i,j] != 0 else grid[i,j] 

def on(x1,y1,x2,y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            grid[i,j] += 1

for line in infile:
    if len(line) == 60:
        line = line[:30]
    line = line.split()

    if len(line) >= 5:
        del line[0]

    action = line[0]
    x1,y1 = [ int(x) for x in line[1].split(",") ]
    x2,y2 = [ int(x) for x in line[3].split(",") ]
    eval(action+"(%d,%d,%d,%d)" % (x1,y1,x2,y2))

infile.close()

cnt = 0
for i in grid:
    for j in i:
        cnt = cnt + j

print(cnt)
