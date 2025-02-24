def factorial(n): 
    fact = 1 
    for i in range(2, n + 1): 
        fact *= i
    return fact

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")