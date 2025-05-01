students = [
    ("Alice", 85), ("Bob", 90), ("Charlie", 78), ("David", 92), ("Eve", 88)
    ]

# Sort the list of tuples by the second element (the score)
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted students by score:", sorted_students)

# Sort the list of tuples by the first element (the name)
sorted_students_by_name = sorted(students, key=lambda x: x[0])
print("Sorted students by name:", sorted_students_by_name)
