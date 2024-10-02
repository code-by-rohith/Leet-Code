def coun(grid):
    a = '-'
    count = 0
    for i in grid:
        for j in i:
            if a in str(j):
                count += 1
    return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(coun(grid))