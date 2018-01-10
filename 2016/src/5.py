import hashlib
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

puzzle_input = "abbhdwsy"

def hexa_finder(start_int, leading_zeros):
    hexa_hash = hashlib.md5(puzzle_input).hexdigest()
    integer = start_int
    start = time.time()
    while hexa_hash[0:len(leading_zeros)] != leading_zeros:
        integer += size
        hexa_hash = hashlib.md5(puzzle_input+str(integer)).hexdigest()
    # print "Hash:", hexa_hash, "Lead:", leading_zeros, "Int:", integer, "Time:", time.time()-start
    return integer, hexa_hash[5:7]

def legitimate(index):
    index = int(index) if index.isdigit() else 9
    return 1 if index in range(8) else 0



cnt = 0
password = ["","","","","","","",""]
new_int, hexa_hash = hexa_finder(rank, "00000")

while cnt < 8:
    password[cnt] = hexa_hash[0]
    cnt += 1
    new_int, hexa_hash = hexa_finder(rank+new_int, "00000")

print "Password for part 1 is", "".join(password)

cnt = 0
password = ["","","","","","","",""]
new_int, hexa_hash = hexa_finder(rank, "00000")

while cnt < 8:
    if legitimate(hexa_hash[0]):
        if not password[int(hexa_hash[0])]:
            password[int(hexa_hash[0])] = hexa_hash[1]
            cnt += 1
    new_int, hexa_hash = hexa_finder(rank+new_int, "00000")

print "Password for part 2 is", "".join(password)
