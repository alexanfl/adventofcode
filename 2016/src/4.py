import string, re
alphabet = [ x for x in string.ascii_lowercase ]

infile = open("../res/4.dat")

sec_sum = 0
words = []
sec_ids = []
for line in infile:
    vals = []
    chars = []
    stop = line.index("[")
    end = line.index("]")
    checksum = line[stop+1:end]
    sec_id = int(line[stop-3:stop])
    for letter in line[:stop]:
        if letter not in chars and letter in alphabet:
            chars.append(letter)
    for char in sorted(chars):
        vals.append([char, line[:stop].count(char)])
    word = ""
    cur_val = 0
    cnt = 1
    while cnt:
        for i in vals:
            if i[1] > cur_val:
                cur_val = i[1]
                w = i[0]
        
        del vals[vals.index([w,cur_val])]
        cur_val = 0
        cnt = 0 if not vals else 1
        word += w

    if word[:5] == checksum:
        words.append(line[:stop-4])
        sec_ids.append(sec_id)
        sec_sum += sec_id

print(sec_sum)

new_words = []

for i in range(len(words)):
    new_word = ""
    for letter in words[i]:
        if letter == "-":
            new_word += " "
        else:
            new_word += alphabet[alphabet.index(letter) \
                     - (26-sec_ids[i]%26)]
    if "north" in new_word:
        print (new_word, sec_ids[i])



