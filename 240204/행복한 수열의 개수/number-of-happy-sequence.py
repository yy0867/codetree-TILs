m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

sequences = []

for i in range(m): # 0, 1, 2
    row, col = [], []
    for j in range(m): # 0, 1, 2
        row.append(grid[i][j])
        col.append(grid[j][i])
    sequences.append(row)
    sequences.append(col)

result = 0
for sequence in sequences:
    cont = set()

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            cont.add(i)
            cont.add(i - 1)
    
    result += (1 if len(cont) >= n else 0)

print(result)