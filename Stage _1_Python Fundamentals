'''
Task 1 : Creating Variables for future use
'''

def intro ():
    name = input("Enter your name: ")
    if type(name) is not str :
        print("Please enter a valid name")
        name = input("Enter your name: ")


    age = int(input("Enter your age: "))
    height = float(input("Enter your height in cm: "))
    print(f"Hi {name} !, How are you ? You are {age} years old and your height is {height} cm.")
    print()

'''
Task 2 : Operators: Playing with Numbers

'''

def calc ():
    count = "y"  
    while (count =="y"):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("-----------CALCULATOR-------------")
        print("===================================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        ch = int (input ("Enter your choice (1-4): "))

        if ch>4 or ch<1 : 
            print("Plese enter a valid choice")
            print("-----------CALCULATOR-------------")
            print("===================================")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            ch = int(input("Enter your choice (1-4): "))
            
        if (ch == 1) :
            print(f"{num1} + {num2} = {num1+num2}")
        elif (ch == 2) :
            print(f"{num1} - {num2} = {num1-num2}")
            
        elif (ch == 3) :
            print(f"{num1} * {num2} = {num1*num2}")
            
        elif (ch == 4 ):
            if (num2 == 0) :
                print("Division by zero is not allowed")
            else :
                print(f"{num1} / {num2} = {num1/num2}")
        else :
            print("Something went wrong")
        count = input("Do you want to continue? (y/n): ")
        
        
'''
    Task 3 : Number checker : 
    takes a number from the user and tells them whether it’s positive, negative, or zero.
'''

def number_checker():
    
    print("-----------NUMBER CHECKER-------------")
    print("======================================")
    
    num = int(input ("Enter a number of your Choice : "))
    
    if (num > 0):
        print(f"{num} : This number is positive. Awesome!")
    elif (num == 0):
        print(f"{num}:  Zero it is. A perfect balance")
    else :
        print(f"{num}:  This number is negative. Better luck next time!")

def main ():
    intro()
    calc()
    number_checker()

if __name__ == "__main__":
    main()
        



