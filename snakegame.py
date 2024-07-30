import random
print(" welcome to snake game")
print(" g for gun\n s for snake\n w for water")
compter=random.choice([1, 2, 3])
yoursr=(input("Please chose g, s and w:-"))
yourDict={"s":1, "w":2,"g":3}
reverseDict = {1: "Snake",2: "Water", 3: "Gun"}
you =yourDict[yoursr]
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[compter]}")

if(compter==you):
    print("it is draw")
else:
    if(compter ==2 and you == 1): 
        print("You win!")

    elif(compter ==2 and you == 3):
        print("You Lose!")

    elif(compter == 1 and you == 2):
        print("You lose!")

    elif(compter ==1 and you == 3):
        print("You Win!")

    elif(compter ==3 and you == 2):
        print("You Win!")

    elif(compter == 3 and you == 1):
        print("You Lose!")
   
    else:
        print("Something went wrong!")