infile = open("../res/3.dat")

line = infile.readlines()[0][:-1]

def get_pos(x):
    if x == "^":
        return [0,1]
    if x == "<":
        return [-1,0]
    if x == ">":
        return [1,0]
    if x == "v":
        return [0,-1]

houses = {}
santa_pos = [0,0]
robo_pos = [0,0]

houses[str(santa_pos)] = 1
houses[str(robo_pos)] = 1

turn = 1

for move in line:
    if turn:
        santa_pos = [ x + y for x, y in zip(santa_pos, get_pos(move)) ]
        houses[str(santa_pos)] = houses[str(santa_pos)] + 1 if str(santa_pos) in houses else 1
        turn = 0
    else:
        robo_pos = [ x + y for x, y in zip(robo_pos, get_pos(move)) ]
        houses[str(robo_pos)] = houses[str(robo_pos)] + 1 if str(robo_pos) in houses else 1
        turn = 1


print(len(houses))
