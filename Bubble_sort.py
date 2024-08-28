def bubble_sort(sorted_array):
    for compare in range(0,len(sorted_array),1):
        for iter in range(compare+1,len(sorted_array),1):
            if sorted_array[compare] > sorted_array[iter]:
                sorted_array[compare],sorted_array[iter] = sorted_array[iter],sorted_array[compare]
    return sorted_array
print(bubble_sort([7,3,2,1,4]))