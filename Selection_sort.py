def selection_sort(array):
    for index in range(0, len(array) - 1, 1):
        current_min = array[index]
        for cf in range(index + 1, len(array), 1):
            if current_min > array[cf]:
                current_min = array[cf]
                array[cf], array[index] = array[index], current_min
    return array

def selection_sort_python_touch(array):
    for index in range(0, len(array) - 1, 1):
        for cf in range(index + 1, len(array), 1):
            if array[index] > array[cf]:
                array[index], array[cf] = array[cf], array[index]
    return array


print(selection_sort([7, 3, 2, 1, 4]))
sel_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# sel_array = [9]
# sel_array = []

print(selection_sort_python_touch(sel_array))

