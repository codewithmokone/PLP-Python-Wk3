# Function to calculte the discount price
def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        calc_discount = discount_percent / 100 * price
        new_price = price - int(calc_discount)
        print(f"The final price after applying the discount is: ${new_price}")
    else:
        print(f"No discount applied. The price is: ${price}")

# Promt user for input
price = int(input("Enter the item price: "))
discount_percent = int(input("Enter the discount percentage: "))

# Print the results
print(calculate_discount(price, discount_percent))