# Ask the user for the first number, store the value in a variable
firstnum = input("Enter an integer between 10 and 100: ")
                    
# Ask the user for the second number, store the value in a variable
secondnum = input("Enter a second ineger that is less than 4: ")

# Repeat back the numbers
firstnum = int(firstnum)
secondnum = int(secondnum)
print(f"Your two numbers are {firstnum} and {secondnum}")

# Perform calculations. Be careful about string formatting for autograders.
sumnum = firstnum + secondnum
productnum = firstnum * secondnum
powernum = firstnum ** secondnum
modnum = firstnum % secondnum

print(f"{firstnum} + {secondnum} = {sumnum}")
print(f"{firstnum} * {secondnum} = {productnum}")
print(f"{firstnum} ** {secondnum} = {powernum}")
print(f"{firstnum} % {secondnum} = {modnum}")
