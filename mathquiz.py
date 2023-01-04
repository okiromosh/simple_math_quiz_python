print("Welcome to My Math Quiz")
playing = input("Do you want to try? ")
if playing.lower() != "yes":
    quit()
print("Okay let's start")

# playing.lower changes all user input to lowercase #
score = 0

answer = input("10 + 12 ")

if answer == "22":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("70 - 20 ")
if answer == "50":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("4 * 3 ")
if answer == "12":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("25 / 5 ")
if answer == "5":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("75 + 25 ")
if answer == "100":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("50 - 30 ")
if answer == "20":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("20 * 6 ")
if answer == "120":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("50 / 5 ")
if answer == "10":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct")
print("You got " + str((score / 8) * 100) + "%")
