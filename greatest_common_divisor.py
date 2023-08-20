def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 84
num2 = 18
result = compute_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
