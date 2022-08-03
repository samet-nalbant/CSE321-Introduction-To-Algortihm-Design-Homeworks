def find_max_profit(array):
    solution = [len(array) + 1]

    solution.append(0)
    for i in range(1, len(array)):
        result = max(solution[i - 1] + array[i - 1], array[i - 1])
        solution.append(result)

    return max(solution)


print(find_max_profit([3,-5,2,11,-8,9,-5]))