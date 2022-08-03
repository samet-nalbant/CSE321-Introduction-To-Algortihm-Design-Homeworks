def brute_force(a,b):
    result = 1
    for i in range(0,b):
        result *= a 
    return result

def divide_conquer(a,b):
    temp = 0 
    if int(b) == 0:
        return 1
    temp = divide_conquer(a, b/2)
    
    if(b%2 == 0):
        return temp*temp
    else:
        return a*temp*temp

if __name__ == "__main__":
    print("Calculated result using brute force algorithm: {}".format(brute_force(2,4)))
    print("Calculated result using divide and conquer algorithm: {}".format(divide_conquer(2,4)))