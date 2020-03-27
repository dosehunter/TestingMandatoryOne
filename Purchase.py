class Purchase:

    totalPrice = 0
    phoneLines = 0
    cellPhones = ["Motorola G99", "iPhone 99", "Samsung Galaxy 99", "Sony Xperia 99", "Huawei 99"]

    def internetPackage(self, packageDeal):
        
        totalPrice += 200
    
    def incTotalPhoneLines(self):
        
        totalPrice += phoneLines * 150

    def decTotalPhoneLines(self):
        
        totalPrice -= phoneLines * 150

    def selectCellphone(self, phoneModel):
        
        if phoneModel == cellPhones[0]:
            totalPrice += 800
        
        elif phoneModel == cellPhones[1]:
            totalPrice += 6000

        elif phoneModel == cellPhones[2]:
            totalPrice += 1000

        elif phoneModel == cellPhones[3] or phoneModel == cellPhones[4]:
            totalPrice += 900
    
    def unselectCellphone(self, phoneModel):
        
        if phoneModel == cellPhones[0]:
            totalPrice -= 800
        
        elif phoneModel == cellPhones[1]:
            totalPrice -= 6000

        elif phoneModel == cellPhones[2]:
            totalPrice -= 1000

        elif phoneModel == cellPhones[3] or phoneModel == cellPhones[4]:
            totalPrice -= 900

    def buyMessage(self):
        "Your purchase has been confirmed"
       


