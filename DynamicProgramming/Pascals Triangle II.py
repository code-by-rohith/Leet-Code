def getRow(rowIndex):
    row = [1]
    for i in range(1, rowIndex + 1):
        row.append(1)
        for j in range(i - 1, 0, -1):
            row[j] = row[j] + row[j - 1]
    return row

rowIndex = 3
print(getRow(rowIndex))


