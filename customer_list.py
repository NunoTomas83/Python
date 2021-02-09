""" Creates a list of consumers """

customers = []
while True:
    create_entry = input("Enter Customer (Yes/No) ")
    create_entry = create_entry[0].lower()
    if create_entry == "n":
        break
    else:
        f_name, l_name = input("Enter customer name : ").split()
        customers.append({"f_name": f_name, "l_name": l_name})
for cust in customers:
    print("This is the customers name : {} {}".format(cust["f_name"], cust["l_name"]))


