arr = [[1, 2], [6, 11], [1, 3], [2, 4],[8,9],[9,10]]
count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j:
            if arr[i][0] >= arr[j][0] and arr[i][1] <= arr[j][1]:
                count += 1
                break

print(count)
