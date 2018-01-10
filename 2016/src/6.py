import string
from numpy import array

infile = open("../res/6.dat")

alphabet = [ x for x in string.ascii_lowercase]

letter_cnt = {}

for char in alphabet:
    letter_cnt[char] = 0

# num_lines = sum(1 for line in infile)

rows = []

cnt = 0
for line in infile:
    rows.append([])
    for letter in line[:-1]:
        rows[cnt].append(letter)
    cnt += 1

rows = array([ array(x) for x in rows ])

word1 = []

for i in range(len(rows[0])):
    top_char = ""
    cnt = 0
    for letter in alphabet:
        letter_cnt = rows[:,i].tolist().count(letter)
        if letter_cnt > cnt and letter_cnt != 0:
            top_char = letter
            cnt = letter_cnt

    word1.append(top_char)

print("".join(word1))

word2 = []

for i in range(len(rows[0])):
    top_char = ""
    cnt = 90
    for letter in alphabet:
        letter_cnt = rows[:,i].tolist().count(letter)
        if letter_cnt < cnt and letter_cnt != 0:
            top_char = letter
            cnt = letter_cnt

    word2.append(top_char)

print("".join(word2))
