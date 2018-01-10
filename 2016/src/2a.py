infile = open("../res/2.dat")

numPad = [[1,2,3], [4,5,6], [7,8,9]]
curPos = [1,1]
curNum = numPad[curPos[0]][curPos[1]]
pineapple = []


for line in infile:
    for inst in line:
        if inst == "U" and curPos[0] != 0:
            curPos[0] -= 1
        if inst == "R" and curPos[1] != 2:
            curPos[1] += 1
        if inst == "L" and curPos[1] != 0:
            curPos[1] -= 1
        if inst == "D" and curPos[0] != 2:
            curPos[0] += 1
        if inst == '\n':
            pineapple.append(numPad[curPos[0]][curPos[1]])
            break

print(pineapple)
