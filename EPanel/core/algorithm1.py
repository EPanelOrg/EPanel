# profit(price) + amount based algorithm
homes = {"home1": {"type": "seller", "price": 100, "amount": 3},
         "home2": {"type": "seller", "price": 20, "amount": 2},
         "home3": {"type": "seller", "price": 28, "amount": 3},
         "home4": {"type": "seller", "price": 30, "amount": 10},
         "home5": {"type": "seller", "price": 9, "amount": 2},
         "home6": {"type": "buyer", "price": 15, "amount": 7},
         "home7": {"type": "buyer", "price": 14, "amount": 3},
         "home8": {"type": "buyer", "price": 20, "amount": 6},
         "home9": {"type": "buyer", "price": 27, "amount": 10}
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
print("____________________")

sellers_sum = 0
buyers_sum = 0

for i, s in enumerate(sellers):

    sellers_sum += s["amount"]
    print("seller amount")
    print(sellers_sum)
    buyers_sum = 0

    for j, b in enumerate(buyers):

        if j <= i:
            buyers_sum += b["amount"]

        else:
            break

    print("buyer amount")
    print(buyers_sum)

    if buyers_sum == sellers_sum:
        break


print("++++++++++++")
print(sellers_sum)
print(buyers_sum)
