#!/usr/bin/python
""" Sleep sort starts a separate task for each item to be sorted, where each task 
    sleeps for an interval corresponding to the item's sort key, then emits the item. 
    Items are then collected sequentially in time. """

from functools import partial
from time import sleep
from random import random
from multiprocessing import Pool, Manager

LIST_LENGTH = 10   # Length of the list
NUM_VARIETY = 10   # Range of numbers that can be generated

def bed_time(sort, num):
    """ Function to multiprocess """
    sleep(num)
    print("Slept %s" % (num))
    sort.append(num)
    return num

def main():
    manager = Manager()
    sort = manager.list()
    unsorted = []
       
    for i in range(LIST_LENGTH):
        unsorted.append(int(random()*NUM_VARIETY+1))
    print("Unsorted: %s\n" % (unsorted))
    
    func = partial(bed_time, sort)
    p = Pool(len(unsorted))
    p.map(func, unsorted)
    print("\nSorted: %s\n" % (sort))
    
if __name__ == "__main__":
    main()