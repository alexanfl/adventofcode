file_name = "../res/2.dat"

check_sum1 = 0
check_sum2 = 0
with open(file_name) as file:
    for line in file:
        line = line[:-1].split("\t")
        line = list(map(int,line))
        check_sum1 += max(line) - min(line)

        line.sort(reverse=True)

        for digit in line:
            for digit2 in line[line.index(digit)+1:]:
                check_sum2 += digit/digit2 if not digit%digit2 else 0

print(check_sum1)
print(check_sum2)
