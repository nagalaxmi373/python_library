import numpy as np

sales = np.array([[200, 300, 250],
                  [150, 220, 210],
                  [300, 350, 400]])

print("Sales Matrix:")
print(sales)

# Doubling 2nd column (Bonus Day Sales)
sales[:, 1] = sales[:, 1] * 2

print("\nAfter Bonus Day Sales:")
print(sales)

print("\nIn Single Row Format:")
print(sales.flatten())
