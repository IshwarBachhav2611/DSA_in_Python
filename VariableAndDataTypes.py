# Program: Variables and Data Types in Python

# Integer
age = 21
print("Age:", age, "| Type:", type(age))

# Float
height = 5.8
print("Height:", height, "| Type:", type(height))

# String
name = "Ishwar"
print("Name:", name, "| Type:", type(name))

# Boolean
is_student = True
print("Is Student:", is_student, "| Type:", type(is_student))

# List (ordered, mutable)
marks = [85, 90, 78, 92]
print("Marks:", marks, "| Type:", type(marks))

# Tuple (ordered, immutable)
coordinates = (10, 20)
print("Coordinates:", coordinates, "| Type:", type(coordinates))

# Set (unordered, unique elements)
unique_numbers = {1, 2, 3, 3, 4}
print("Unique Numbers:", unique_numbers, "| Type:", type(unique_numbers))

# Dictionary (key-value pairs)
student = {
    "name": "Ishwar",
    "age": 21,
    "course": "DSA with Python"
}
print("Student Info:", student, "| Type:", type(student))

# NoneType
result = None
print("Result:", result, "| Type:", type(result))
