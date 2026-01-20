import random 

score = 0 
while True:
    name = input("Enter your name: ")
    if name == "":
        print("Enter a valid name")
        continue 
    elif name.isalpha():
        break
    else:
        print("Name must not be numeric ")

while True:
    try:
        age = int(input("Enter Your age: "))
        break
    except ValueError:
        print("Enter a valid number")


if age < 6 or age > 10:
    print("You are too old or for this test")
    exit()


for i in range (5):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    if num1 < num2:
        num1, num2 = num2, num1

    choice = input("What type of test do you want addition or subtraction: ").capitalize()
    if choice in ["Add", "Addition"]:
        guess = int(input(F"Q{i+1} What is {num1} + {num2}: "))
        answer = num1 + num2

    elif choice in ["Sub", "Subtract"]:
        guess = int(input(F"Q{i+1} What is {num1} - {num2}: "))
        answer = num1 - num2
    
    else:
        print("Invalid Choice")

    if guess == answer:
        score += 10 
        print("Correct plus 10 points")     
    else:
        print(f"Wrong, your answer is {answer}")



print(f"Name: {name}")
print(f"score: {score}")
                   
            

