#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------
import time
#Builds the cache of size cache_size
cache_size = 650000
cycle_table = [0] * cache_size

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    
    v = 1
    # Allows the format i, j and j, i (ex: 1 10 and 10 1)
    beg = i
    end = j
    if(i > j):
	beg = j
	end = i

    for num in range(beg, end+1):
	
	cycle = collatz_cycle(num)
	if(num < cache_size and cycle_table[num] == 0):
	    cycle_table[num] = cycle
	if(cycle > v):
	    v = cycle

    
    assert v > 0
    return v

def collatz_cycle(n):
    """
    n is the number that the user wants the collatz to run
    returns cycle length
    """
    cycles = 1
    assert n > 0
    while(n > 1):
	if n < cache_size and cycle_table[n] != 0:
	    cycles = cycles + cycle_table[n] - 1
	    break
	if n % 2 == 0:
	    n = n / 2
	    cycles+= 1
	else:
	    n = n + (n >> 1) + 1
	    cycles+=2
    assert cycles > 0
    return cycles
# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
