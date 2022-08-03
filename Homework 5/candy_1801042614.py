def find_maximum(prices, length):
    values = [0 for x in range(length+1)]
    values[0] = 0
    for i in range(1, length+1):
        max_val = 0
        for j in range(i):
             max_val = max(max_val, prices[j] + values[i-j-1])
        values[i] = max_val

    return values[length]

prices = [1,5,8,9,10,17,17,20]

print("Maximum obtainable value: {}".format(find_maximum(prices, 8)))    