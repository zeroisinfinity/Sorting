def selection_sort(array):

    for iter in range(0,len(array),1):
        current_min = array[iter]
        for compare in range(iter+1,len(array),1):
            if current_min > array[compare]:
                current_min = array[compare]
                array[compare], array[iter] = array[iter] , current_min
    return array
    
def selection_sort_python_touch(sorted_array):
    for compare in range(0,len(sorted_array),1):
        for iter in range(compare+1,len(sorted_array),1):
            if sorted_array[compare] > sorted_array[iter]:
                sorted_array[compare],sorted_array[iter] = sorted_array[iter],sorted_array[compare]
    return sorted_array
print(selection_sort([7,3,2,1,4]))
sel_array = [9,8,7,6,5,4,3,2,1,0]
#sel_array = [9]
#sel_array = []

print(selection_sort(sel_array))

