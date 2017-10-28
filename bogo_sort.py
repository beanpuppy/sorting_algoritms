#!/usr/bin/python
""" Bogo sort randomises the list until it is sorted """

from random import random, shuffle

def check_sort(numbers):
    """ Checks if the list is sorted """
    notsorted = False
    for i in range(len(numbers)-1):
        if i >= numbers[i+1]:    # For ascending order
            notsorted = True
    return notsorted

def main():
    to_sort = []

    for i in range(10):
        to_sort.append(int(random()*10+1))
    print("Unsorted: %s\n" % (to_sort))
    
    loops = 0
    while check_sort(to_sort):
        loops += 1
        shuffle(to_sort)
        print("List: %s, Loops: %s" % (to_sort, loops))
    
    print("\nSorted!")
    
if __name__ == "__main__":
    main()
