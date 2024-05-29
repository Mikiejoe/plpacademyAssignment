def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price

price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percent: "))

print(f"The final price is: {calculate_discount(price,discount_percent)}")