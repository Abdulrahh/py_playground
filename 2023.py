customer_name =str(input("Customer name: "))
customer_address = str(input("Enter your address: "))

VAT = 0.20

# a validation technique to make sure customer number is digit
while True:
    customer_number = str(input("Enter your phone number:")).strip()
    if customer_number.isdigit() and len(customer_number) == 11:
        break
    else:
        print("Number must be an integer and a valid number ")

# validation to loop back customer if lawn width and lenght is passed a certain value 
while True:
    lawn_width = float(input("Enter Lawn Width:"))
    if lawn_width < 2 or  lawn_width > 30:
        print("Lawn Width must be between 2 and 30")
    
    else:
        break 
    
while True:
    lawn_lenght = float(input("Enter Lawn Width:"))
    if lawn_lenght < 2 or  lawn_lenght > 50:
        print("Lawn Width must be between 2 and 30")
    
    else:
        break 

lawn_area = lawn_width * lawn_lenght

while True:
    add_lawn_care = input("Do you want lawn_care(Y/N): ").upper()
    if add_lawn_care == "Y":
        while True:
            lawn_care = input("Enter Lawn Care Type (Economy, Standard, Luxury): ").lower()
            if lawn_care == "economy":
                care_cost = lawn_area * 0.45
                break 
            elif lawn_care == "standard":
                care_cost = lawn_area * 0.80
                break 
            elif lawn_care == "luxury":
                care_cost = lawn_area * 1.15
                break
            else:
                print(" Enter a valid lawn care type ")
        break 

    elif add_lawn_care == "n":
        lawn_care = "None"
        care_cost = 0
        break
    else:
        print("Please enter y or n.")


labour_cost = lawn_area * 0.5
total_cost = labour_cost + care_cost
total_cost_VAT = total_cost * 1.2 / VAT


print("*********SUMMARRY*********")
print(f"Customare Name:{customer_name}")
print(f"Customare Address:{customer_address}")
print(f"Customare Phone number :{customer_number}")
print(f"lawn width: {lawn_width}m², lawn lenght: {lawn_lenght}m²")
print(f"lawn care type {lawn_care}£")
print(F"labour cost: {labour_cost}£")
print(f"lawn care cost {care_cost}£")
print(f"total cost {total_cost}£, Exculding VAT: {VAT}")
print(f"total cost including VAT {total_cost_VAT}£, VAT: {VAT}")