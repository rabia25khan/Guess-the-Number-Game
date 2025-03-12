import random

def guess_the_number():
    print("Welcome to Guess the Number Game!")
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Guess the number: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

guess_the_number()
