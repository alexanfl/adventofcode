from math import sqrt, ceil
from numpy import array, zeros

input_number = 361527

def get_layer(position):
    layer = ceil((sqrt(position)+1)/2)
    square = layer*2-1
    step = square - 1

    return step, square, layer

step, square, layer = get_layer(input_number)


row_col_centers = [square**2 -(layer - 1 + i*step) for i in range(4)]

dist = [abs(input_number - center) for center in row_col_centers]

distance_to_centre = layer - 1 + min(dist)

print("square:", square, "layer:", layer, "distance to centre:", distance_to_centre)

   
def update_corners(position):
    step, square, layer = get_layer(position)
    corners = [square**2 - i*step for i in range(4)]
    corners.sort()
    return corners


def find_next_square(indices, velocity):
    indices = (indices[0] + velocity[0], indices[1] + velocity[1])
    return indices

def update_direction(velocity, index, corners):
    if index == corners[0]:
        velocity = [0,-1]
    elif index == corners[1]:
        velocity = [1,0]
    elif index == corners[2]:
        velocity = [0,1]
    elif index == corners[3]+1:
        velocity = [-1,0]
        corners = update_corners(index)

    return velocity,corners

def overwrite_square(indices, grid):
    sum_of_squares = 0
    for i in range(-1,2):
        for j in range(-1,2):
            sum_of_squares += grid[indices[0]+i,indices[1]+j]
    return sum_of_squares

def set_up_grid(x, y):
    return zeros((x, y))

grid = set_up_grid(square+1, square+1)

current_indices = (layer-1,layer-1)

grid[current_indices] = 1

current_indices = (layer-1,layer)
grid[current_indices] = 1

current_velocity = [-1,0]

current_corners = update_corners(2)


for i in range(3, input_number+1):
    current_indices = find_next_square(current_indices, current_velocity)
    grid[current_indices] =  overwrite_square(current_indices, grid)
    current_velocity, current_corners = update_direction(current_velocity, i, current_corners)
    
    if grid[current_indices] > input_number:
        print(grid[current_indices])
        break

