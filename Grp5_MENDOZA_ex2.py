def perform_operations(num1, num2):
    
    # Addition
    addition = num1 + num2
    print(f"Addition: {addition}")
    
    # Subtraction
    subtraction = num1 - num2
    print(f"Subtraction: {subtraction}")
    
    # Multiplication
    multiplication = num1 * num2
    print(f"Multiplication: {multiplication}")
    
    # Division
    division = num1 / num2 if num2 != 0 else "Division by zero is undefined"
    print(f"Division: {division}")
    
    # Modulus (only applicable for real numbers)
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        modulus = num1 % num2 if num2 != 0 else "Modulus by zero is undefined"
        print(f"Modulus: {modulus}")
    
    # Exponentiation
    exponent = num1 ** num2
    print(f"Exponentiation: {exponent}")
    
    print()

# Test with integer numbers
print("Integer\n")
num1 = 21
num2 = 3
perform_operations(num1, num2)

# Test with floating point numbers
print("Float\n")
num1= 3.14
num2 = 3.2
perform_operations(num1, num2)

# Test with complex numbers
print("Complex\n")
num1 = complex(2, 3)
num2 = complex(1, 2)
perform_operations(num1, num2)


# Write a program that creates two variables, num1 and num2. Both num1 and num2 should be assigned the integer literal 25000000, one written with underscores and one without. Print num1 and num2 on two separate lines.

num1 = 25000000 
num2 = 25_000_000

print("Number 1: ",num1)
print("Number 2: ",num2,"\n")

#Creating int,float and complex variable then check the type using the Python Code

num1 = 1            
num2 = 6.28            
num3 = 5 + 9j   

print(f"num1 is of type: {type(num1)}")
print(f"num2 is of type: {type(num2)}")
print(f"num3 is of type: {type(num3)}")