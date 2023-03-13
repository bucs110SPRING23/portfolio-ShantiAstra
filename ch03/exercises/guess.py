import random
my_number = random.randrange(1,11)
print("I have chosen a number between 1 and 10. You have three chances to guess the number or you will fall into an enchanted sleep forever.")
def guess(order):
    message = str("What is your " + str(order) + " guess?")
    user_guess = int(input(message))
    if  user_guess == my_number:
        print("Correct. I suppose you will live for now")
        return True
    elif user_guess < my_number:
        print("Too Low")
        return False
    elif user_guess > my_number:
        print("Too high")
        return False

if guess("first") == False:
    if guess("second") == False:
        if guess("third") == False:
            print("The number was " + str(my_number) + ". Have a good night!")