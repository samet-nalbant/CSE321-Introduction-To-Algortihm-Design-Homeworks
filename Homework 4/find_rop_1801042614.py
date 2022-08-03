import math

def find_rop(array, n):
	temp_array = [0]*n
	return mergeSort(array, temp_array,0, n - 1)

def mergeSort(array, temp_array, left, right):
	count = 0
    
	if left < right:
		mid = math.floor((left + right)/2)
		count += mergeSort(array, temp_array, left, mid)
		count += mergeSort(array, temp_array, mid + 1, right)
		count += merge(array, temp_array, left, mid, right)
        
	return count

def merge(array, temp_array, left, mid, right):
    i,j,k,count = left,mid+1,left,0
    
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            k += 1
            i += 1
            
        else:
            temp_array[k] = array[j]
            count += (mid-i + 1)
            k += 1
            j += 1
            
    while i <= mid:
    	temp_array[k] = array[i]
    	k += 1
    	i += 1

    while j <= right:
    	temp_array[k] = array[j]
    	k += 1
    	j += 1

    for m in range(left, right + 1):
    	array[m] = temp_array[m]	
        
    return count


if __name__ == "__main__":
    message = [10,25,8,92,51]
    print("The number of reverse-ordered pairs: {}".format(find_rop(message,5)))