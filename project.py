

VAT = 0.20 

def main():
    print("******** Welcome *********")

    while True:
        name = input("Enter your name:")
        if name == "":
            print("enter a valid name")
        
        else:
            break
            
    
    while True:
        vehicle = input("Enter Your vehicle registration number: ")
        if vehicle.isdigit() and len(vehicle) == 6:
            break
        else:
            print("Please enter a valid number")
    
    
    while True:
        number = input("Enter your number: ")
        if number.isdigit() and len(number) == 11:
            break
        else:
            print("Please enter a valid number")


    while True: 
        print("basic = 6.00£, standard = 9.00£, premium = 14.00£")
        wash = input("Select wash type; Basic-, standard and premium: ").lower()
        if wash == "basic" :
            wash_price = 6.00
            break
        elif wash == "standard":
            wash_price = 9.00
            break 
        elif wash == "premium":
            wash_price = 14.00
        else:
            print("Enter a valid Wash please!!")

    while True: 
        print("wax polish: 3.00")
        add_polish = input("Do you want wax polish? (yes/no): ").lower() 
        if add_polish == "yes" or "y":
            wax_polish = 3.00
            break 
        elif add_polish == "no" or "n":
            wax_polish = 0 
            break 
        else:
            print("Enter a valid input")

    while True:
        print("interior_vacuum: 4.00£")
        add_vacuum = input("Do you want interior vacuum?(yes/no)").lower()
        if add_vacuum == "yes" or "y":
            interior_vacuum = 4.00
            break
        elif add_vacuum == "no" or "n":
            interior_vacuum = 0
            break 
        else:
            print("enter a valid input ")
        

    while True:
        print("tyre_shrine: 2.50£")
        add_tyre = input("Do you want tyre shine?(yes/no):").lower()
        if add_tyre == "yes" or "y":
            tyre_shine = 2.50
            break
        elif add_tyre == "no" or "n":
            tyre_shine = 0
            break 
        else:
            print("enter a valid choice ")

# calculation 
    total_price_exc_VAT = wash_price + wax_polish + interior_vacuum + tyre_shine
    total_VAT = total_price_exc_VAT * VAT
    total_price_inc_VAT = total_price_exc_VAT + total_VAT

    print("*******CAR WASH RECEIPT*****")
    print(f"Customer Name: {name}")
    print(f"Vehicle Reg No: {vehicle}")
    print(f"Phone Number: {number}")
    print(f"Wash Type: {wash.capitalize()} - £{wash_price:.2f}")
    print(f"Wax Polish: £{wax_polish:.2f}")
    print(f"Interior Vacuum: £{interior_vacuum:.2f}")
    print(f"Tyre Shine: £{tyre_shine:.2f}")
    print(f"\nTotal (Excl. VAT): £{total_price_exc_VAT:.2f}")
    print(f"VAT (20%): £{total_VAT:.2f}")
    print(f"Total (Incl. VAT): £{total_price_inc_VAT:.2f}")

main()

