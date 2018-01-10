import string

def required(char1, char2):
    req = [ x + x for x in set(string.ascii_lowercase) ]
    char = char1 + char2
    return 1 if char in req else 0
    
def disallowed(char1, char2):
    dis = ["ab", "cd", "pq", "xy"]
    char = char1 + char2
    return 1 if char in dis else 0

def is_vowel(char):
    vowels = "aeiou"
    return 1 if char in vowels else 0

def has_pair(char1, char2, pair_list):
    tmp = 0
    tmp_eq = 0
    prev = ""
    prevprev = ""
    three_in_a_row = 0
    for elem in pair_list:
        if elem == char1+char2 and char1 == char2:
            tmp_eq += 1
            if not prev and not prevprev:
                prev = elem
            elif prev == elem:
                prevprev = elem
                prev = ""
                tmp_eq -= 1
            elif prevprev == elem:
                three_in_a_row = 1
                prevprev = ""
                prev = ""
            
            tmp_eq = 2 if three_in_a_row else tmp_eq

        elif elem == char1+char2 and char1 != char2:
            tmp += 1
        else:
            prev = ""
            prevprev = ""

    print(tmp, tmp_eq)
    return 1 if tmp > 1 or tmp_eq > 1 else 0

def has_repeat(rep_list):
    for elem in rep_list:
        if elem[0] == elem[2]:
            return 1
    return 0

def is_nice1(string):
    vow_cnt = is_vowel(string[-1])
    requirement = 0

    for i in range(len(string)-1):
        vow_cnt += is_vowel(string[i])
        if disallowed(string[i],string[i+1]):
            return 0
        requirement = 1 if required(string[i],string[i+1]) else requirement
    if requirement and vow_cnt >= 3:
        return 1
    else:
        return 0

def is_nice2(string):
    pair_list = [ string[i]+string[i+1] for i in range(len(string)-1) ]
    rep_list = [ string[i]+string[i+1]+string[i+2] for i in range(len(string)-2) ]
    print(rep_list)

    req1 = has_pair(string[-2], string[-1], pair_list)
    req2 = has_repeat(rep_list)

    for i in range(len(string)-2):
        req1 += has_pair(string[i],string[i+1], pair_list)
        req2 += has_repeat(rep_list)

    print ("pair req:", req1)
    print ("rep req:", req2)
    return 1 if req1 and req2 else 0
    

infile = open("../res/5.dat")

cnt1 = 0
cnt2 = 0

# infile = ["xyfxy\n"]

for line in infile:
    print (line)
    if is_nice1(line[:-1]):
        cnt1 += 1
    if is_nice2(line[:-1]):
        cnt2 += 1

print("ex. a:", cnt1)
print("ex. b:", cnt2)
