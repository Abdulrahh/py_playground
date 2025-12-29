score = 0
special_character = ["!", "%", "&","*","+","="]


while True:
    password = input("Enter your password to grade: ")
    if len(password) >= 8 and len(password) <= 15:
        break
    else:
        print("Invalid password")
    
if len(password) >= 10:
    score += 20
    
# deduction 
if password.islower(): # check if password is lower case only and removes 3 points per charater 
    score -= 3 * len(password)
elif password.isupper(): # does the same thing 
    score -= 3 * len(password)
elif password.isdigit(): # does the same thing but deduct 5 points per charater 
    score -= 5 * len(password)


for char in password:
    if char in special_character: # check for ecah special charater and adds 10 points 
        score += 10
    elif char.islower() : # check for each lower case letter and adds 5 points 
        score += 5
    elif char.isupper(): # does the same thing 
        score += 5
    elif char.isdigit(): #checks for num
        score += 10 


# password rating 
if score <= 20:
    print(f"your score is {score}, Wow Your rating is very low!!")
elif score >= 21 and score <= 40:
    print(f"your score is {score}, Low password rating!! ")
elif score >= 41 and score <= 70:
    print(f"your score is {score}, medium password rating, could have tried harder")
elif score >= 71 and score <= 80:
    print(f"your score is {score}, your password rating is high")
elif score >= 81:
    print(f"your score is {score}, nice password!!")

        
        


