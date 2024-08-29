def insertion_sort(array):
    for test_sub in range(1,len(array),1):
            sample = array[test_sub]
            compare = test_sub - 1
            while compare >= 0 and sample < array[compare]:
                array[compare + 1] = array[compare]
                compare -= 1
            array[compare+1] = sample
        return array

ins_array = [9,8,7,6,5,4,3,2,1,0]
#ins_array = [9]
#ins_array = []
print(insertion_sort(ins_array))






