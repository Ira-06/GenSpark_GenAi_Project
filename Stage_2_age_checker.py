def age_checker():
    age = int (intput("Enter your age: "))
    if(age>16):
        print("Congratulations! You are eligible to vote. Go make a difference!")
    elif(age <= 16):
        print("Sorry, you are not eligible to vote yet. But don't worry, the future is yours!")
    else :
        print("Invalid age was entered")
        

def main ():
    age_checker()

if __name__ == "__main__":
    main()
        
