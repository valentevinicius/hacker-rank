def miniMaxSum(arr):
    index = 0
    result = list()
    min_val = int()
    max_val = int()
    
    for num in arr:
        temp_v = num
        arr.remove(temp_v)
        result.append(sum(arr))
        arr.insert(index, temp_v)
        index += 1
        
        min_val = min(result)
        max_val = max(result)
            
    print(min_val, max_val)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
