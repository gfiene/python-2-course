# 5. Дано число rowIndex, верните rowIndexth (0-indexed) строку паскаль треугольника
## В Паскаль треугольнике, каждое числов это сумма двух предыдущих над ним.

rowIndex = int(input())
row = [1]
for _ in range(rowIndex):
    row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
print(row)