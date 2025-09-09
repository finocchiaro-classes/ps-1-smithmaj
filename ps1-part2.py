# Write a function that takes two variables and does all the computations asked
def number_fun(a,b):
    sumnum = a + b
    productnum = a * b
    powernum = a ** b
    modnum = a % b

    print(f"{a} + {b} = {sumnum}")
    print(f"{a} * {b} = {productnum}")
    print(f"{a} ** {b} = {powernum}")
    print(f"{a} % {b} = {modnum}")
    
# Ask the user for the first number, store the value in a variable
firstnum = int(input("Enter an integer between 10 and 100: "))

# Ask the user for the second number, store the value in a variable
secondnum = int(input("Enter a second ineger that is less than 4: "))

# Repeat back the numbers
print(f"Your two numbers are {firstnum} and {secondnum}")

# Perform calculations. Be careful about string formatting for autograders.

number_fun(firstnum, secondnum)


