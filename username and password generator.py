import random
import string 

print("-------------Welcome--------------")
while True:
    first_name = input("Enter your firstname: ").strip()
    if first_name == "":
        print("Enter a valid name")
    else:
        break 
while True :
    last_name = input("Enter your last name: ").strip()
    if last_name == "":
        print("Enter a valid last name")
    else:
        break 

while True:
    dob = input("Enter date of birth in dd/mm/yyyy formart: ").strip() 

    if len(dob) != 10 or dob[2] != "/" or dob[5] != "/":
        print(f"Invalid date formate {dob}")
        continue 
    
    year_part = dob[6:10] # checks the last four digit which is the year ,uses indexing to take the first 4 string
    if not year_part.isdigit(): # checks if year is numeric 
        print("Year must be numeric")
        continue 
    
    
    birth_year = int(year_part) # convert to int just incase not needed
    current_year = 2026 
    
    if current_year - birth_year < 18:
        print("You must be atlest 18 years old to use this program")
    
    break 

def format_name(name):
    return (name[:3] + "XXX")[:3] # check if name is less than 3 add x and limit it to 3 charaters 

user_id = format_name(first_name.lower()) + format_name(last_name.lower()) + str(year_part) 


def password():
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)

    # fill the remaining 5
    Char = string.ascii_letters + string.digits
    remains = ''.join(random.choices(Char, k= 5))
    
    password_list = list(upper + lower + digit + remains)
    random.shuffle(password_list)
    
    return ''.join(password_list)

temporary_password = password()

print("-----Registration Succesfful-----")
print(f"Your full name is {first_name}, {last_name}")
print(f"Your username is {user_id}")
print(f"Your temporary password is {temporary_password}")