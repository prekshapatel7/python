#Create two dictionaries – one containing grocery items
#and their prices and another containing grocery items and quantity purchased.
#By using the values from these two dictionaries compute the total bill.
# Dictionary of item prices
prices = {
    'rice': 50,
    'milk': 30,
    'bread': 20,
    'eggs': 6
}

# Dictionary of quantities purchased
quantities = {
    'rice': 2,     # 2 kg
    'milk': 3,     # 3 liters
    'bread': 1,    # 1 loaf
    'eggs': 12     # 12 eggs
}

# Calculate the total bill
total_bill = 0

print("Item-wise Bill:\n")
for item in prices:
    if item in quantities:
        item_total = prices[item] * quantities[item]
        total_bill += item_total
        print(f"{item.capitalize()}: {quantities[item]} × {prices[item]} = ₹{item_total}")

print("\nTotal Bill: ₹", total_bill)
