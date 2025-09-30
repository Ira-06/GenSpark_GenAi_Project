def gussing_game():
    number_to_guess= random.randint(1,100)
    attempts=1
    while (attempts<11):
        
        
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Invalid entry! Please enter a number.")
            continue
        
        if (guess == number_to_guess):
            print(f"{guess} Congratulations! You guessed it in {attempts} attempts!")
            break
        
        elif (guess < number_to_guess):
            print("Too Low! Try again ")
           
        elif (guess > number_to_guess):
            print("Too High! Try again ")
            
        attempts+=1
 

def main ():
    gussing_game()
