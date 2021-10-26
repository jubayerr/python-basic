# build a guessing game

secret_word = "Monkey"
guess = ""
guessed = 0
guessed_limit = 3
out_of_guessed = False

print("Hint: It is a human like animal")

while guess != secret_word and not out_of_guessed:
    if guessed < guessed_limit:
        guess = input("Enter a name: ")
        guessed += 1
    else:
        out_of_guessed = True

if out_of_guessed:
    print("You lose!")
else:
    print("Congratulation! You Win.")

