def partition(array, l, r):
    x = array[r]
    i = l
    
    for j in range(l, r):
        
        if array[j] <= x:
            array[i], array[j] = array[j], array[i]
            i += 1
            
    array[i], array[r] = array[r], array[i]
    return i
 
def divide(array, l, r, k):
 
    if (k > 0 and k <= r - l + 1):
        index = partition(array, l, r)
        
        if (index - l == k - 1):
            return array[index]
        
        elif (index - l > k - 1):
            return divide(array, l, index - 1, k)
        
        return divide(array, index + 1, r, k - index + l - 1)
    
def find_meaningful(array, k):
    return divide(array,0,len(array)-1,k)


if __name__ == "__main__":
    results = [10,25,8,92,51]
    print("Rate of kth element: {}".format(find_meaningful(results, 3)))