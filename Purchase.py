class Purchase:

    totalPrice = 0
    phoneLines = 0
    cellPhones = ["Motorola G99", "iPhone 99", "Samsung Galaxy 99", "Sony Xperia 99", "Huawei 99"]

    def __init__ (self):
        pass

    def is_even(self, number):
        return number % 2 == 0

    def internetPackage(self, packageDeal):
        
        if packageDeal == True:
            self.totalPrice += 200
    
    def incTotalPhoneLines(self):
        self.totalPrice += self.phoneLines * 150

    def decTotalPhoneLines(self):
        
        self.totalPrice -= self.phoneLines * 150

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

    def buyMessage(self):

        if self.totalPrice == 0:
            "Dear user, your cart is empty. You need to purchase one or more items listed in the shop."
        
        elif self.totalPrice > 0:
            "Your purchase has been confirmed"

