def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    current_sum = 0
    for i in range(mid, left - 1, -1):
        current_sum += arr[i]
        left_sum = max(left_sum, current_sum)

    right_sum = float('-inf')
    current_sum = 0
    for i in range(mid + 1, right + 1):
        current_sum += arr[i]
        right_sum = max(right_sum, current_sum)

    return left_sum + right_sum

def max_subarray_sum(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_max = max_subarray_sum(arr, left, mid)
    right_max = max_subarray_sum(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    return max(left_max, right_max, cross_max)


# Beolvasás
subarray_length = int(input())
array = list(map(int, input().split()))

# Eredmény kiírása
print(max_subarray_sum(array, 0, subarray_length-1))