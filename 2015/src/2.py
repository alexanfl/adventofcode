infile = open("../res/2.dat")

def calculate_area(dim):
    l, w, h = dim
    return 2*l*w + 2*w*h + 2*h*l

def calculate_volume(dim):
    l, w, h = dim
    return l*w*h

def calculate_remainder(dim):
    return dim[dim.index(max(dim)) - 1]*dim[dim.index(max(dim)) - 2]

def calculate_smallest_perimeter(dim):
    return 2*dim[dim.index(max(dim)) - 1] + 2*dim[dim.index(max(dim)) - 2]

area = 0
length = 0

for line in infile:
    dimensions = [ int(i) for i in line.split("x") ]
    area += calculate_area(dimensions) + calculate_remainder(dimensions)
    length += calculate_smallest_perimeter(dimensions) + calculate_volume(dimensions)

print("Area of packing paper is", area, "square feet.")
print("Length of ribbon is", length, "feet.")
