# Author:Da pan

age_of_oldboy = 56

count = 0

while count < 3:
    guess_age = int(input("guess_age:"))
    if guess_age == age_of_oldboy:
        print("yes, you got it")
        break
    elif guess_age > age_of_oldboy:
        print("thinks bigger")
    else:
        print("thinks smaller")

    count += 1
else:
    print("you have tried too many times.. fuck off")