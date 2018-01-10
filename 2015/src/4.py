import hashlib
# from mpi4py import MPI
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
    print "Rank:", rank, "Lead:", leading_zeros, "Int:", integer, "Time:", time.time()-start
    return integer

hexa_finder(rank, "00000")
hexa_finder(rank, "000000")
hexa_finder(rank, "0000000")
