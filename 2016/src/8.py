import numpy as np

infile = open("../res/8.dat")

screen_size = [6,50]

screen = np.zeros(screen_size, dtype=str)
screen[:,:] = " "

def oper(string, screen):
    string = string.split()
    if string[0] == "rect":
        x,y = string[1].split("x")
        x, y = int(x), int(y)
        screen[:y,:x] = "#"
    else:
        assert string[0] == "rotate"
        assert string[1] == "row" or string[1] == "column"

        rotation = int(string[4])
        if string[2][0] == "x":
            x = int(string[2][2:])
            screen[:,x] = np.roll(screen[:,x], rotation)
        else:
            y = int(string[2][2:])
            screen[y,:] = np.roll(screen[y,:], rotation)

    for i in screen:
        for j in i:
            print(j, end="")
        print("")
    print("\n")

    return screen

for line in infile:
    oper(line, screen)

cnt = 0
for i in screen:
    for j in i:
        if j == "#":
            cnt += 1

print(cnt)
