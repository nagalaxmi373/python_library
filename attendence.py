import numpy as np

attendance = np.array([[1, 1, 0],
                       [1, 0, 1],
                       [1, 1, 1]])

print("Attendance Matrix:")
print(attendance)

row_format = attendance.flatten()

print("\nSingle Row Format:")
print(row_format)

total_attendance = np.sum(attendance, axis=1)

print("\nTotal attendance of each student:")
print(total_attendance)
