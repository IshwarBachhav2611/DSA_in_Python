print("----- STRING -----")
name = "PythonDSA"
print("Original String:", name)
print("Length:", len(name))
print("Upper:", name.upper())
print("Lower:", name.lower())
print("Slice [0:6]:", name[0:6])
print("Reverse:", name[::-1])

print("\n----- LIST -----")
numbers = [10, 20, 30, 40]
print("Original List:", numbers)

numbers.append(50)          # Add
numbers.insert(1, 15)       # Insert
numbers.remove(30)          # Remove
numbers[0] = 5              # Update

print("Updated List:", numbers)
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

print("\nLoop through List:")
for n in numbers:
    print(n)

print("\n----- TUPLE -----")
points = (10, 20, 30)
print("Tuple:", points)
print("Index 1:", points[1])
print("Count of 20:", points.count(20))
print("Length:", len(points))

print("\n----- SET -----")
unique_nums = {1, 2, 3, 3, 4}
print("Original Set:", unique_nums)

unique_nums.add(5)          # Add
unique_nums.remove(2)       # Remove

print("Updated Set:", unique_nums)

print("\nLoop through Set:")
for x in unique_nums:
    print(x)

print("\n----- DICTIONARY -----")
student = {
    "name": "Ishwar",
    "age": 21,
    "course": "DSA"
}

print("Original Dictionary:", student)

student["age"] = 22              # Update
student["college"] = "ABC"       # Add
student.pop("course")            # Remove

print("Updated Dictionary:", student)

print("\nKeys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

print("\n----- END OF STAGE 1 -----")
