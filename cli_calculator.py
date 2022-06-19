print("Welcome to Pycal, an integrated python calculator. ")

print("""
    **********Help**********
    select "a" for addition 
    select "s" for subtraction
    select "m" for multiplication
    select "d" for division

""")
#Accepting users input
user_input = input("What would you like to do? ")

#accept the numbers to be used for the operations
numone = int(input("Please input the first number... "))
numtwo = int(input("Please input the second number... "))

#If statement to execute the operation chosen by the user
if user_input == "a":
        sum = numone + numtwo
        print("The sum is ",sum)
elif user_input == "s":
    if numone > numtwo:
        sub = numone - numtwo
    else:
        sub = numtwo - numone
    print("The positive difference is ", sub)
elif user_input == "m":
    mult = numone * numtwo
    print("The product is ", mult)
elif user_input == "d":
    div = numone / numtwo
    print("The quotient is ", div)
else:
    print("You have not selected a valid option. Check 'Help' and try again. ")

