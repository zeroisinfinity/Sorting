def selection_sort(array):

    for iter in range(0,len(array),1):
        current_min = array[iter]
        for compare in range(iter+1,len(array),1):
            if current_min > array[compare]:
                current_min = array[compare]
                array[compare], array[iter] = array[iter] , current_min
    return array

sel_array = [9,8,7,6,5,4,3,2,1,0]
#sel_array = [9]
#sel_array = []

print(selection_sort(sel_array))

