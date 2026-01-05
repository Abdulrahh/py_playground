rate = {"USD": 1.40,
        "EUR": 1.14,
        "BRL": 4.77,
        "JPY": 151.05,
        "TRY": 5.68}

exchange = 0 

print("Avaliable chocice")
for _ in rate: # print out the key values meaning the currecy users can covert to 
    print(_)
    
while True:
    try:
        GBP = float(input("Enter Amount in pounds you wish to convert: "))
        if GBP > 2500: # validate to keep looping until user enters the appropriate amount 
            print("AMOUNT EXCEEDED THE LIMIT (2500)")
        else:
            break 
    except(ValueError):
        print("Error please enter a value in pounds")

while True: #exhange rate calculation and validation check if user input is same as in the disctionary 
    currency  = input("Enter a currency to convert: ").upper() # help make user input in upper case 
    if currency  in rate:
       exchange = GBP * rate[currency]
       break 
    else:
        print("INVALID CURRENCY TRY AGAIN")
        
# transaction fees 
if GBP <= 300:
    transaction_fee = GBP * 0.035
elif GBP > 300 and GBP <= 750:
    transaction_fee = GBP * 0.03
elif GBP > 750 and GBP <= 1000:
    transaction_fee = GBP * 0.025
elif GBP > 1000 and GBP <= 2000:
    transaction_fee = GBP * 0.02
else:
    transaction_fee = GBP * 0.015

total_fee = GBP + transaction_fee

while True: 
    employee = input("Are you a member of staff?(Y/N): ").upper()
    if employee in ["YES", "Y"]:
        discount_fee =  total_fee * 0.05
        discount = total_fee - discount_fee
        break
    elif employee in ["NO", "N"]:
        discount_fee = 0
        discount = total_fee
        break 
    else:
        print("Invalid input!!!")

print("-------------------reciept--------------------")
print(f"You will recieve {exchange:.2f} in {currency} ")
print(f"Trasaction fee for the exchange is £{transaction_fee:.2f}")
print(f"Your total fee is £{total_fee:.2f}")
print(f"You are applicable for discount £{discount_fee:.2f}, this bring your total fee to £{discount:.2f}")
print("------------------------------------------------")
        
    

    
    


