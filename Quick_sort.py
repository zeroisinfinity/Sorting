def quick_sort(array,start_pos,end_pos):
	if start_pos < end_pos:
		curren_pivot = partition(array,start_pos,end_pos)
		quick_sort(array,start_pos,curren_pivot - 1)
		quick_sort(array,curren_pivot + 1,end_pos)
		
def partition(array,start_pos,end_pos):
	pivot = array[end_pos]
	
	min = start_pos - 1
	for iter in range(0,end_pos):
		if array[iter] < pivot :
			min+=1
			array[min] , array[iter+1] = array[iter+1] , array[min]
	array[min+1] , array[end_pos] = array[end_pos] , array[min+1]
	return min+1
arr = [9,8,1,0,11,12,10]
quick_sort(arr,0,len(arr)-1)
print(arr)

	
