def main():
    print("----------Welcome!!-------------")
    while True:
        try:
            weight = float(input("Enter your weight in kilograms (KG): "))
            if weight < 30 or weight > 250:
                print("Error Weight must be between 30 and 250kg")
            else:
                break
        except(ValueError):
            print("Enter a valid weight ")
            
    while True:
        try:
            height = float(input("Enter your hieght in meters(m): "))
            if height < 1.0 or height > 2.5 :
                print("Error height must be between 1.0m and 2.5m")
            else:
                break
        except(ValueError):
            print("Enter a valid height ")
            
    while True:
        try:
            age = float(input("Enter your age: "))
            if age < 1 or age > 200:
                print("Error user age is above or below the livable limit!!😂 ")
            else:
                break
        except(ValueError):
            print("Enter a valid age ")
            
    BMI = weight /(height ** 2)
    BMR = (10 * weight) + (6.25 * height * 100) - (5 * age) + 5 
    if BMI < 18.5:
        print(f"Underweight, your BMI is {BMI:.2f}")
    elif BMI <= 24.9:
        print(f"Healthy Weight, your BMI is {BMI:.2f}")
    else:
        print(F"Overweight, your BMI is  {BMI:.2f}")
    print(F"Your BMR or Daily Calorie Needs is {BMR:.2f}")

    
def fitness_tracker():
    while True:
        main()
        choice = input("Do you want to go back or Calculate for a friend (Y/N): ").upper()
        if choice in ["N", "NO"]:
            print("Thank You for using Fitness Goal Tracker")
            break 
        elif choice not in ["Y", "YES"]:
            print("Invalid choice ")
fitness_tracker()

           
    