# Input values
a = 10
b = 20
c = 15

# 1. Simple if statement
if a < b:
    print("1. a is less than b")

# 2. if-else statement
if a > b:
    print("2. a is greater than b")
else:
    print("2. a is NOT greater than b")

# 3. if-elif-else statement
if a > b:
    print("3. a is the largest")
elif b > c:
    print("3. b is the largest")
else:
    print("3. c is the largest")

# 4. Nested if statement
if a < b:
    if a < c:
        print("4. a is the smallest")
    else:
        print("4. c is the smallest")

# 5. Logical operators
if a < b and a < c:
    print("5. a is smaller than both b and c")

if a < b or a > c:
    print("6. At least one condition is true")

if not(a > b):
    print("7. a is NOT greater than b")

# 6. Comparison operators
if a == 10:
    print("8. a is equal to 10")

if b != 15:
    print("9. b is not equal to 15")

if c >= 15:
    print("10. c is greater than or equal to 15")

if a <= 10:
    print("11. a is less than or equal to 10")

# 7. Even or Odd check
number = 7
if number % 2 == 0:
    print("12. Number is Even")
else:
    print("12. Number is Odd")

# 8. Positive, Negative or Zero
num = -5
if num > 0:
    print("13. Positive Number")
elif num < 0:
    print("13. Negative Number")
else:
    print("13. Zero")
