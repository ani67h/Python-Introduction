actual_cost = float(input(" Please enter the actual product price : "))
sale_amount = float(input(" Please enter the sales amount : "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total profit = {0}".format(amount))
if (sale_amount < actual_cost):
    amount1 = actual_cost - sale_amount
    print("Total loss = {0}".format(amount1))
if (sale_amount == actual_cost):
    amount2 = sale_amount - actual_cost
    print("No profit and no loss")