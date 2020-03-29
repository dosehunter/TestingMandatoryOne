class Purchase:
    totalPrice = 0

    phoneLines = 0

    cellphones = {"Motorola G99": 800, "iPhone 99": 6000, "Samsung Galaxy 99": 1000, "Sony Xperia 99": 900,
                  "Huawei 99": 900}

    def internetPackage(self, packageDeal):

        if packageDeal == True:
            totalPrice += 200

    def incTotalPhoneLines(self):

        totalPrice += phoneLines * 150

    def decTotalPhoneLines(self):

        totalPrice -= phoneLines * 150

    def selectCellphone(self, phoneModel):

        if phoneModel == "Motorola G99":

            totalPrice += get("Motorola G99")



        elif phoneModel == "iPhone 99":

            totalPrice += get("iPhone 99")



        elif phoneModel == "Samsung Galaxy 99":

            totalPrice += get("Samsung Galaxy 99")



        elif phoneModel == "Sony Xperia 99" or phoneModel == "Huawei 99":

            totalPrice += 900

    def unselectCellphone(self, phoneModel):

        if phoneModel == "Motorola G99":

            totalPrice -= get("Motorola G99")



        elif phoneModel == "iPhone 99":

            totalPrice -= get("iPhone 99")



        elif phoneModel == "Samsung Galaxy 99":

            totalPrice -= get("Samsung Galaxy 99")



        elif phoneModel == "Sony Xperia 99" or phoneModel == "Huawei 99":

            totalPrice -= 900

    def buyMessage(self):

        if totalPrice == 0:

            "Dear user, your cart is empty. You need to purchase one or more items listed in the shop."



        elif totalPrice > 0:

            "Your purchase has been confirmed"




