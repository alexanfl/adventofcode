
infile = open("../res/7.dat")

def is_ABA(string):
    assert len(string) == 3

    if string[0] == string[2] and string[1] != string[0]:
        return 1
    else:
        return 0

def exists_ABA(string):
    print(string)
    words = []
    for i in range(len(string)-2):
        word = string[i:i+3]
        print(word)
        if is_ABA(word):
            words.append(word)
        else:
            continue

    return words

def create_BAB(word):
    return word[1]+word[0]+word[1]

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

supports_SSL = 0

for line in infile:
    cnt = 0
    l = split_IP(line)
    ABA_in_supseq = []
    BAB_in_hypseq = []
    for i in range(len(l)):
        if i%2:
            if exists_ABA(l[i]):
                for elem in exists_ABA(l[i]):
                    BAB_in_hypseq.append(elem)
        else:
            if exists_ABA(l[i]):
                for elem in exists_ABA(l[i]):
                    ABA_in_supseq.append(elem)
            
    for ABA in ABA_in_supseq:
        if ABA[1]+ABA[0]+ABA[1] in BAB_in_hypseq:
            cnt = 1

    supports_SSL += cnt
    print(ABA_in_supseq, BAB_in_hypseq)
    print(cnt)

print("\n",supports_SSL)
