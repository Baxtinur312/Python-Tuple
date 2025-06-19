orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]
filtered = [order for order in orders if order[0] % 2 == 0]
print(filtered)
