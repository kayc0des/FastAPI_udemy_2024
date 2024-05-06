''' Python Variables '''

wallet = 50
item_price = 15

# write a function to return the tax amount for an item
def tax_amount(price):
    if not isinstance(price, int):
        return 0
    return 0.03 * price

# calculate amount to be paid plus taxes
amount_paid =  item_price + tax_amount(item_price)

# calculate balance
balance = wallet - amount_paid

print(f'Your new balance is ${balance}')