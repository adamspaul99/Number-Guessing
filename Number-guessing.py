import random as rd
randNumber = rd.randint(1, 100)
# print(randNumber)
userguess = None
guesses = 0
print("Some rule for number guesses :-\n"
      "* You have to guess number between 1 tp 100\n")
while userguess != randNumber:
    userguess = int(input("Enter your guess:- \n"))
    guesses += 1
    if userguess == randNumber:
        print("You guessed it Right!")
        print(f"You guessed the number in {guesses} guesses")
    else:
        if userguess < randNumber:
            print("You guessed it Wrong! Please try with greater number")
        else:
            print("You guessed it Wrong! Please try with smaller number")

with open("highscore.txt", "r") as a:
    highscore = int(a.read())

if guesses < highscore:
    print("You have just broken the high score, Congratulations!")
    with open("highscore.txt", "w") as a:
        a.write(str(guesses))
