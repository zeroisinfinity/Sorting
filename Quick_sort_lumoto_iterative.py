import random
import math

def shuffle(array,start_pos,end_pos):
    sh_pivot = random.randint(start_pos,end_pos)
    array[sh_pivot] , array[start_pos] = array[start_pos] , array[sh_pivot]
    return partition(array,start_pos,end_pos)

def partition(array,start_pos,end_pos):

    inc = start_pos - 1
    pivot = array[end_pos]

    for cf in range(start_pos,end_pos,1):
        if array[cf] <= pivot:
            inc+=1
            array[inc] , array[cf] = array[cf] , array[inc]

    array[inc + 1] ,array[end_pos] = array[end_pos] , array[inc + 1]
    return inc + 1

def quick_sort_iterative(array,start_pos,end_pos):

    records = end_pos - start_pos + 1
    stack = [0] * records

    top = start_pos - 1

    top+=1
    stack[top] = start_pos
    top+=1
    stack[top] = end_pos

    while top >= 0:

        end_pos = stack[top]
        top-=1
        start_pos = stack[top]
        top-=1

        new_pivot = partition(array,start_pos,end_pos)
        if new_pivot - start_pos > math.ceil(records//2):
            shuffle(array, start_pos, new_pivot - 1)
        elif end_pos - new_pivot > math.ceil(records//2):
            shuffle(array, new_pivot + 1, end_pos)

        if start_pos < new_pivot - 1:
            top += 1
            stack[top] = start_pos
            top+=1
            stack[top] = new_pivot - 1

        if end_pos > new_pivot + 1:
            top+=1
            stack[top] = new_pivot + 1
            top+=1
            stack[top] = end_pos

# Driver code to test above
arr = list(range(80,6,-4)) + [90]*7 + [34]*8
n = len(arr)
quick_sort_iterative(arr, 0, n-1)
print(arr)





