#!/usr/bin/python
""" Selection sort divides the array into two parts, unsorted and sorted. It then finds
    the largest element in the unsorted sublist swapping it with the leftmost unsorted element
    (putting it in sorted order), and moving the sublist boundaries one element to the left. """

from random import random

LIST_LENGTH = 100  # Length of the list
NUM_VARIETY = 20   # Range of numbers that can be generated

def biggest(array, index):
    """ Find the biggest number (as index) in the unsorted list """
    big = 0
    for i in range(index+1):
        if array[i] > array[big]:
            big = i
    return big

def swap(array, num1, num2):
    """ Swaps num1 and num2 (as indexes) in an array """
    tmp = array[num1]
    array[num1] = array[num2]
    array[num2] = tmp
    return array

def check_sort(numbers, index):
    """ Checks if the list is sorted """
    for i in range(index+1):
        if numbers[i] > numbers[i+1]:  # For ascending order
            return True  # Means it's unsorted
    return False

def selection_sort(array):
    passes = 0
    index = len(array) - 1
    while check_sort(array, index):
        num = biggest(array, index)
        array = swap(array, index, num)
        index -= 1
        passes += 1
        print("List: %s, Passes: %s" % (array, passes))
    
    return array

def main():
    to_sort = []

    for i in range(LIST_LENGTH):
        to_sort.append(int(random()*NUM_VARIETY+1))
    print("Unsorted: %s\n" % (to_sort))

    sort = selection_sort(to_sort)
    print("\nSorted: %s" % (sort))



if __name__ == "__main__":
    main()