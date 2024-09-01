import sys
import random
import math
sys.setrecursionlimit(3000)

def quick_sort(array, start_pos, end_pos):

    if start_pos < end_pos:
            left_pivot , right_pivot = shuffle(array, start_pos, end_pos)
            quick_sort(array, start_pos, left_pivot) 
            quick_sort(array, right_pivot + 1, end_pos)

def shuffle(array,start_pos,end_pos):
    sh_pivot = random.randint(start_pos,end_pos)
    array[sh_pivot] , array[start_pos] = array[start_pos] , array[sh_pivot]
    return partition(array,start_pos,end_pos)

def partition(array, start_pos, end_pos):

    pivot = array[start_pos]
    low_dyn = start_pos
    inc = start_pos
    high_dyn = end_pos

    while inc <= high_dyn:

        if array[inc] < pivot:
                array[inc], array[low_dyn] = array[low_dyn], array[inc]
                inc += 1
                low_dyn+=1

        elif array[inc] == pivot :
                inc+=1

        else:
                array[inc], array[high_dyn] = array[high_dyn], array[inc]
                high_dyn-=1

    return low_dyn , high_dyn

arr = [8]*600 + [67384]*500 + list(range(90000,0,-8)) #print(array)
print(len(arr))
quick_sort(arr, 0, len(arr) - 1)
print(arr)
print(len(arr))
