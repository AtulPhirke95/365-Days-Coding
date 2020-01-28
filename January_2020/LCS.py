def longest_increasing_subsequence(arr):
    lis = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis) #5


arr = [ 1, 12, 2, 22, 5, 30, 31, 14, 17, 11 ]
print(longest_increasing_subsequence(arr))
