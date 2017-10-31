#!/usr/bin/python
""" Bubble sort iterates through the list where pairs of adjacent items
    are compared in turn. If they are out of order, they are swapped, repeating 
    until the list is sorted. """

from random import random

LIST_LENGTH = 100  # Length of the list
NUM_VARIETY = 20   # Range of numbers that can be generated

def swap(array, num1, num2):
    """ Swaps num1 and num2 (as indexes) in an array """
    tmp = array[num1]
    array[num1] = array[num2]
    array[num2] = tmp
    return array

def bubble_sort(unsorted):
    swapped = True
    passes = 0
    while swapped:
        swapped = False
        passes += 1
        for i in range(len(unsorted)-1):
            if unsorted[i] > unsorted[i+1]:  # For ascending order
                unsorted = swap(unsorted, i, i+1)
                swapped = True
        print("List: %s, Passes: %s" % (unsorted, passes))
    return unsorted 

def main():
    unsorted = []
    
    for i in range(LIST_LENGTH):
        unsorted.append(int(random()*NUM_VARIETY+1))
    print("Unsorted: %s" % (unsorted))

    sort = bubble_sort(unsorted)
    print("\nSorted: %s" % (sort))


if __name__ == "__main__":
    main()