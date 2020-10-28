difficulty=str(input("Please choose a difficulty: Easy, Medium or Hard"))
if difficulty == "Easy":
    import random
    x=(random.choice(open('easywords.txt').readline().split()).strip())
    print(x)
    print(x)