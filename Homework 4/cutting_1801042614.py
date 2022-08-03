def cutting(n, count):
    if(n <= 1):
        return count
    else:
        return cutting(n/2,count+1)
        
if __name__ == "__main__":    
    print(cutting(2,0))