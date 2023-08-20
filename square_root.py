import math
number = float(input("Enter a number: "))
if number < 0:
    raise ValueError("Square root is not defined for negative numbers.")

result = math.sqrt(number)
print(f"The square root of {number} is: {result:.2f}")