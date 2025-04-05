# shopping cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: £"))
        foods.append(food)
        prices.append(price)

print("------Your Cart -------")

for food in foods:
    print(food, end= " ")

for price in prices:
    total = total + price
print()
print(f"Your total is {total}")