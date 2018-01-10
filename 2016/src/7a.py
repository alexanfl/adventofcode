
infile = open("../res/7.dat")

def is_ABBA(string):
    assert len(string) == 4

    if string[:2] == string[3] + string[2] and string[:2] != string[2:]:
        return 1
    else:
        return 0

def exists_ABBA(string):
    for i in range(len(string)-3):
        word = string[i:i+4]
        if is_ABBA(word):
            return 1
        else:
            continue

    return 0

def split_IP(string):
    split_str = []
    tmp_str = ""
    for char in string:

        if char == "[" or char == "]" or char == "\n":
            split_str.append(tmp_str)
            tmp_str = ""
        else:
            tmp_str += char

    return split_str

ABBAs = 0

for line in infile:
    l = split_IP(line)
    ABBA_in_IP = 0
    ABBA_in_hypseq = 0
    for i in range(len(l)):
        if i%2:
            ABBA_in_hypseq += exists_ABBA(l[i])
        else:
            ABBA_in_IP += exists_ABBA(l[i])
    if ABBA_in_IP and not ABBA_in_hypseq:
        ABBAs += 1

print(ABBAs)
