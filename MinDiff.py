def sumMinAbsDiff(arr, n):
    arr.sort()
    sum = 0
    sum += abs(arr[0] - arr[1])
    sum += abs(arr[n-1] - arr[n - 2])
    for i in range(1, n-1):
        sum += min(abs(arr[i] - arr[i - 1]), abs(arr[i] - arr[i+1]))
    return sum

t = int(input())
j = input()
arr = list(map(int, j.split(" ")))
# for i in range(t):
#     j = int(input())
#     arr.append(j)

print(sumMinAbsDiff(arr, t))