numbers = [10, 20, 30, 40]

print("Original List:", numbers)

# Add elements
numbers.append(50)
numbers.insert(1, 15)

# Update element
numbers[0] = 5

# Remove element
numbers.remove(30)

print("Updated List:", numbers)
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

# Loop through list
for n in numbers:
    print(n)
