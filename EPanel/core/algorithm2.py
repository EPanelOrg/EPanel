# profit(price) + amount based algorithm
homes = {"home1": {"type": "seller", "price": 100, "amount": 3},
         "home2": {"type": "seller", "price": 25, "amount": 5},
         "home4": {"type": "seller", "price": 30, "amount": 10},
         "home5": {"type": "seller", "price": 9, "amount": 2},
         "home6": {"type": "buyer", "price": 15, "amount": 7},
         "home7": {"type": "buyer", "price": 14, "amount": 4},
         "home9": {"type": "buyer", "price": 20, "amount": 6}
         }

sellers = []
buyers = []

for key, v in homes.items():
    if v["type"] == "seller":
        s = {"price": v["price"], "amount": v["amount"]}
        sellers.append(s)
    if v["type"] == "buyer":
        b = {"price": v["price"], "amount": v["amount"]}
        buyers.append(b)

sellers = sorted(sellers, key=lambda k: k['price'])
buyers = sorted(buyers, key=lambda k: k['price'], reverse=True)
print("sellers")
print(sellers)
print("buyers")
print(buyers)
print("_____________________________________________\n")

for i in range(0, len(sellers) + len(buyers)):
    if len(buyers) == 0 or len(sellers) == 0:
        break
    trading_price = (sellers[0]["price"] + buyers[0]["price"]) / 2
    print("seller sold power to buyer at price = " + str(trading_price))
    sellers.remove(sellers[0])
    buyers.remove(buyers[0])
print("_____________________________________________\n")

print("remains:\n")
print("sellers")
print(sellers)
print("buyers")
print(buyers)
