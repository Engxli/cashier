def get_number_to_string(number):
    counter=0
    for i in str(number):
        counter+=1
        if(i == "."):
            break
    if "." in str(number):
        return str(str(round(number, 3))+"000000")[:(5+counter-1)]
    else:
        return str(str(round(number, 3))+".000000")[:(5+counter-1)]

def get_invoice_items(items):
    # Items is a dictionary with a quantity and price key, and a name key
    # Return a list of all the invoice line items in the following format:
    # quantity name subtotal currency
    # For example, if we had the following:
    # [
    #   {'name': 'Apple', 'quantity': 1, 'price': 0.2 },
    #   {'name': 'Orange', 'quantity': 4, 'price': 0.3 },
    # ]
    # We should return the following:
    # ['1 Apple 0.200KD', '4 Orange 1.200KD']
    # ---
    # Write your code here
    invoice_items = []
    for item in items:
        invoice_items.append(str(item["quantity"])+" "+ str(item["name"])+ " "+ get_number_to_string((item["price"]*item["quantity"])) +"KD" )
    return(invoice_items)

def get_total(items):
    # Items is a dictionary with a quantity and price key
    # Calculate the total of all items in the cart
    # Write your code here
    total = 0
    for price in [item["quantity"]*item["price"] for item in items]:
        total += price
    return total


def print_receipt(invoice_items, total):
    # invoice_items will be the list of formatted items received from
    # `get_invoice_items`, and total will be a float. Print out a nice receipt
    # displaying a title, all the invoice items on separate lines, and the
    # total at the end.
    # ---
    # Write your code here
    # -------------------
    # receipt
    # -------------------
    # 4 apples 0.800KD
    # 1 carrot 0.100KD
    # 2 flour 2.600KD
    # 10 water bottles 0.500KD
    # -------------------
    # Total Price: 4.000KD

    print("-------------------\n"+"RECEIPT\n"+"-------------------")
    for item in invoice_items:
        print(item)
    print("-------------------\n"+"Total Price: "+ get_number_to_string(total)+"KD")
    


def main():
    # Write your main logic here
    items = []
    while True:
        item_name = input("Item name(enter 'done' when finished): ")
        if(item_name.lower() == "done"):
            break
        item_price = input("Price: ")
        item_quantity = input("Quantity: ")
        items.append({"name":item_name, "price":float(item_price), "quantity": int(item_quantity)})

    invoice_items = get_invoice_items(items)
    total = get_total(items)
    print_receipt(invoice_items, total)



if __name__ == "__main__":
    main()
