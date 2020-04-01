class Purchase:

    totalPrice = 0
    phoneLines = 0
    chosenPhones = []
    cellPhones = ["Motorola G99", "iPhone 99", "Samsung Galaxy 99", "Sony Xperia 99", "Huawei 99"]

    def __init__ (self):
        pass


    def internetPackage(self, packageDeal):
        if packageDeal == True:
            self.totalPrice += 200
        else:
            self.totalPrice -= 200

        return self.totalPrice
    
    def incTotalPhoneLines(self):
        if self.phoneLines >= 8:
            return self.totalPrice

        self.phoneLines += 1
        self.totalPrice += 150
        return self.totalPrice

    def decTotalPhoneLines(self):
        if self.phoneLines == 0:
            return self.totalPrice

        self.phoneLines -= 1
        self.totalPrice -= 150
        return self.totalPrice

    def selectCellphone(self, phoneModel):
        
        if phoneModel == self.cellPhones[0]:
            self.totalPrice += 800
        
        elif phoneModel == self.cellPhones[1]:
            self.totalPrice += 6000

        elif phoneModel == self.cellPhones[2]:
            self.totalPrice += 1000

        elif phoneModel == self.cellPhones[3] or phoneModel == self.cellPhones[4]:
            self.totalPrice += 900
        else:
            print("Phone model not found!")
            return self.totalPrice

        self.chosenPhones.append(phoneModel)

        return self.totalPrice

    def unselectCellphone(self, phoneModel):
        
        if phoneModel == self.cellPhones[0]:
            self.totalPrice -= 800
        
        elif phoneModel == self.cellPhones[1]:
            self.totalPrice -= 6000

        elif phoneModel == self.cellPhones[2]:
            self.totalPrice -= 1000

        elif phoneModel == self.cellPhones[3] or phoneModel == self.cellPhones[4]:
            self.totalPrice -= 900
        else:
            print("Phone model not found!")
            return self.totalPrice

        self.chosenPhones.remove(phoneModel)

        return self.totalPrice

    def buyMessage(self):

        if self.totalPrice == 0:
            return "Dear user, your cart is empty. You need to purchase one or more items listed in the shop."
        
        print("Your purchase has been confirmed")

