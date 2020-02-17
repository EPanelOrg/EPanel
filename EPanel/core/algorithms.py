# not complete
class ProfitAndAmountBased:
    def start(self):
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


class ProfitBased:

    def start(self, homes):
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
        # print("sellers")
        # print(sellers)
        # print("buyers")
        # print(buyers)
        # print("_____________________________________________\n")

        result = {}
        for i in range(0, len(sellers) + len(buyers)):
            if len(buyers) == 0 or len(sellers) == 0:
                break
            trading_price = (sellers[0]["price"] + buyers[0]["price"]) / 2
            result[str(i)] = [str(i), str(trading_price), str(abs(sellers[0]["amount"] - buyers[0]["amount"]))]
            # print("seller sold power to buyer at price = " + str(trading_price))
            sellers.remove(sellers[0])
            buyers.remove(buyers[0])
        print(result)
        # print("_____________________________________________\n")

        # print("remains:\n")
        # print("sellers")
        # print(sellers)
        # print("buyers")
        # print(buyers)


# homes = {"home1": {"type": "seller", "price": 100, "amount": 3},
#          "home2": {"type": "seller", "price": 25, "amount": 5},
#          "home4": {"type": "seller", "price": 30, "amount": 10},
#          "home5": {"type": "seller", "price": 9, "amount": 2},
#          "home6": {"type": "buyer", "price": 15, "amount": 7},
#          "home7": {"type": "buyer", "price": 14, "amount": 4},
#          "home9": {"type": "buyer", "price": 20, "amount": 6}
#          }
# pb = ProfitBased()
# pb.start(homes=homes)
