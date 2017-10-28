#!/usr/bin/python
from functools import partial
from time import sleep
from random import random
from multiprocessing import Pool, Manager

def sleep_sort(sort, num):
    """ Function to multiprocess """
    sleep(num)
    print("Slept %s" % (num))
    sort.append(num)
    return num

def main():
    """ Generates numbers and sorts """
    manager = Manager()
    sort = manager.list()
    unsorted = []
       
    for i in range(10):
        unsorted.append(int(random()*10+1))
    print("Unsorted: %s\n" % (unsorted))
    
    func = partial(sleep_sort, sort)
    p = Pool(len(unsorted))
    p.map(func, unsorted)
    print("\nSorted: %s\n" % (sort))
    
if __name__ == "__main__":
main()