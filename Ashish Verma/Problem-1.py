def calculator(a, b, operation):   # here I created a function name calculator with 3 parameters a, b, and operation
    operation = operation.lower()  #convert operation to lowercase
    if operation == "add":       
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:       # here we are checking that b != be 0
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

a = float(input("Enter a: "))  # taking value from the user
b = float(input("Enter b: "))  # here also taking value from the user of b
operation = input("Enter operation (add, subtract, multiply, divide): ")

result = calculator(a, b, operation)  # here we calling the function caluclator and storing final result into result variable
print(result)   # final result here we get it
