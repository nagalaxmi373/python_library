import numpy as np

print("Enter marks of 3 Students for 3 Subjects")

marks = np.zeros((3,3))

for i in range(3):
    print(f"\nEnter marks for Student {i+1}")
    for j in range(3):
        marks[i][j] = int(input(f"Subject {j+1} : "))

print("\nOriginal Marks Matrix:")
print(marks)

print("\nSingle Row Format (Before Bonus):")
print(marks.flatten())

subject = int(input("\nEnter subject number to double (1, 2 or 3): "))

marks[:, subject-1] = marks[:, subject-1] * 2

print("\nMarks After Bonus:")
print(marks)

total = np.sum(marks, axis=1)
average = np.mean(marks, axis=1)

grades = []

for avg in average:
    if avg >= 85:
        grades.append("A")
    elif avg >= 70:
        grades.append("B")
    elif avg >= 50:
        grades.append("C")
    else:
        grades.append("Fail")

print("\n----- STUDENT REPORT -----")

for i in range(3):
    print(f"\nStudent {i+1}")
    print("Marks :", marks[i])
    print("Total :", total[i])
    print("Average :", round(average[i],2))
    print("Grade :", grades[i])

print("\nFinal Report (Single Row After Bonus):")
print(marks.flatten())

print("\nAll Processing Completed Successfully")
