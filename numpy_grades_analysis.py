numpy_grades_analysis.py

# NUMPY PROJECT - Student Grades Analysis
import numpy as np

# Generate random grades between 80-100 for 5 students and 5 subjects
grades = np.random.randint(80, 100, size=(5, 5))
print("Grades Matrix:")
print(grades)
print()

# Calculate maximum grades
student_max = np.max(grades, axis=0)
subject_max = np.max(grades, axis=1)
print("Student-wise Maximum:", student_max)
print('Subject-wise Maximum:', subject_max)
print()

# Calculate minimum grades
student_min = np.min(grades, axis=0)
subject_min = np.min(grades, axis=1)
print('Student-wise Minimum:', student_min)
print('Subject-wise Minimum:', subject_min)
print()

# Calculate average grades
student_avg = np.mean(grades, axis=0)
subject_avg = np.mean(grades, axis=1)
print('Student-wise Average:', student_avg)
print('Subject-wise Average:', subject_avg)