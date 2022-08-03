def partition(start, end, rates):
	
	pivot_index = start
	pivot = rates[pivot_index]

	while start < end:
		while start < len(rates) and rates[start] <= pivot:
			start += 1

		while rates[end] > pivot:
			end -= 1
            
		if(start < end):
			rates[start], rates[end] = rates[end], rates[start]
            
	rates[end], rates[pivot_index] = rates[pivot_index], rates[end]
    
	return end
	

def quick_sort(start, end, rates):
    
	if (start < end):
		p = partition(start, end, rates)
		quick_sort(start, p - 1, rates)
		quick_sort(p + 1, end, rates)
        
def find_best_worst(rates):
    quick_sort(0, len(rates) - 1, rates)
    print("Worst rate: {}".format(rates[0]))
    print("Best rate: {}".format(rates[len(rates)-1]))

if __name__ == "__main__":
    rates = [10,25,8,92,51]
    find_best_worst(rates)



