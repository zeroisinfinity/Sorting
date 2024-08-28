"""arr = [4,7,8,9,5,2,4,62,0]
r = [22,333,4555,22222222,77777,999999,67886556,995667,5764]
arr[2:6] = r[3:6]
print(arr)"""
def insertion_sort(array):

    if len(array) != 1 and len(array) != 0:

        for test_sub in range(1,len(array),1):
            sample = array[test_sub]
            compare = test_sub - 1
            while compare >= 0 and sample < array[compare]:
                compare -= 1
            array[compare+2:test_sub+1] = array[compare+1:test_sub]
            array[compare + 1] = sample
        return array

    else:
        if len(array)==1:
            return 'Array already sorted'
        else:
            return 'Array has no elements'

ins_array = [9,8,7,6,5,4,3,2,1,0]
#ins_array = [9]
#ins_array = []
print(insertion_sort(ins_array))






