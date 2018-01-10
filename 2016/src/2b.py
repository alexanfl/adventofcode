infile = open("../res/2.dat")

numPad = [
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ','1',' ',' ',' '], 
         [' ',' ','2','3','4',' ',' '], 
         [' ','5','6','7','8','9',' '],
         [' ',' ','A','B','C',' ',' '],
         [' ',' ',' ','D',' ',' ',' '], 
         [' ',' ',' ',' ',' ',' ',' ']
         ]

curPos = [3,1]
curNum = numPad[curPos[0]][curPos[1]]
pineapple = []

for line in infile:
    for inst in line:
        if inst == "U" and numPad[curPos[0]-1][curPos[1]] != ' ':
            curPos[0] -= 1
        if inst == "R" and numPad[curPos[0]][curPos[1]+1] != ' ':
            curPos[1] += 1
        if inst == "L" and numPad[curPos[0]][curPos[1]-1] != ' ':
            curPos[1] -= 1
        if inst == "D" and numPad[curPos[0]+1][curPos[1]] != ' ':
            curPos[0] += 1
        if inst == '\n':
            pineapple.append(numPad[curPos[0]][curPos[1]])
            break

print(pineapple)
