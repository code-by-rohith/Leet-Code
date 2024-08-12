arr = [[2, 5],[3,4] ]
count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j:
            if arr[i][0] >= arr[j][0] and arr[i][1] <= arr[j][1]:
                count += 1
                break

print(count)
