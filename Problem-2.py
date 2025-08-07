a = int(input("Enter a: "))  # here we taking user input for a variable
num = 1     #initailzing num variable with 1
for i in range(a):     #looping  staring 0 to a-1 because range function does not take last value
    print(num, end=", " if i < a - 1 else "")
    num += 2    #updating num with 2 for next iteration 
                