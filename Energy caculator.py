standard_rate = 0.28
eco_saver = 0.22 
flat_fee = 12.50 

while True:
    name = (input("Enter you name: "))
    if name == "":
        print("Name is empty ")
        continue 
    elif name.isalpha() :
        break 
    else:
        print("Name must not contain numeric input")
        
        
while True:
        acct_num = input("Enter Your 8 digit account number: ")
        if len(acct_num) == 8 and acct_num.isdigit() :
            break 
        else:
            print("Acct doesnt exist ")
            
        
while True:
    try:
        usage = int(input("Enter your energy usage in KWH: "))
        if usage <= 500:
            bill = usage * standard_rate
            break
        else:
            standard_cost  = 500 * standard_rate 
            eco_cost =  (usage - 500) * eco_saver 
            bill = standard_cost + eco_saver 
            break
    except ValueError:
        print("Enter a valid input")
                            
vat = 0.05 * bill
total_cost = bill + vat + flat_fee       
    
print(f"Total energy cost: £{bill:.2f}")
print(f"VAT (5%): £{vat:.2f}")
print(f"Flat fee: {flat_fee}")
print(f"Final bill: £{total_cost:.2f}")
