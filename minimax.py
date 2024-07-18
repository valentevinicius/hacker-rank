"""
    Given five positive integers, find the minimum and maximum values
    that can be calculated by summing exactly four of the five integers.
    Then print the respective minimum and maximum values as a single line of two space-separated long integers.

    Example:
    arr = [1,3,5,7,9]

    The minimum sum is 1+3+5+7=16
    The maximum sum is 3+5+7+9=24

    The function prints 16 24
"""

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
