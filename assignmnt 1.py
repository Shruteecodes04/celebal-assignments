n = 5  # Number of rows

# 1. Lower Triangular
print("Lower Triangular:")
for i in range(1, n + 1):
    print("*" * i)

# 2. Upper Triangular
print("\nUpper Triangular:")
for i in range(n, 0, -1):
    print("*" * i)

# 3. Pyramid
print("\nPyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
