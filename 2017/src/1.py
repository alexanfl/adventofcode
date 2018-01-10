file_name = "../res/1.dat"

with open(file_name) as file:
    file_content = file.readlines()[0][:-1]

sum1 = 0 
previous_digit = int(file_content[-1])

for digit in file_content:
    digit = int(digit)
    sum1 += digit if digit == previous_digit else 0
    previous_digit = digit

print(sum1)

sum2 = 0
N = len(file_content)

for i in range(N):
    digit = int(file_content[i])
    next_digit = int(file_content[int(i-N/2)])
    sum2 += digit if digit == next_digit else 0

print(sum2)
