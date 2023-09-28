# Read input values
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
result = ""

for col in range(m):
    prev_alphanumeric = False
    for row in range(n):
        char = matrix[row][col]
        if char.isalnum():
            result += char
            prev_alphanumeric = True
        elif prev_alphanumeric:
            result += ' '
            prev_alphanumeric = False
    if col < m - 1:
        result += ' '
print(result)
