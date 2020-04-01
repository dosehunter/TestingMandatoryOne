class Purchase:
    alert_string = "Dear user, your cart is empty. You need to purchase one or more items listed in the shop."
    cell_phones = ["Motorola G99", "iPhone 99", "Samsung Galaxy 99", "Sony Xperia 99", "Huawei 99"]

    def __init__ (self, total_price=0, chosen_phones=None, phone_lines=0, internet_connection=False):
        self.total_price = total_price
        if chosen_phones is None:
            chosen_phones = []
        self.chosen_phones = chosen_phones
        self.phone_lines = phone_lines
        self.internet_connection = internet_connection


    def internet_package(self, package_deal):
        if package_deal == True:
            self.total_price += 200
        else:
            self.total_price -= 200

        self.internet_connection = package_deal

        return self.total_price
    
    def inc_total_phone_lines(self):
        if self.phone_lines >= 8:
            return self.total_price

        self.phone_lines += 1
        self.total_price += 150
        return self.total_price

    def dec_total_phone_lines(self):
        if self.phone_lines == 0:
            return self.total_price

        self.phone_lines -= 1
        self.total_price -= 150
        return self.total_price

    def select_cellphone(self, phone_model):
        
        if phone_model == self.cell_phones[0]:
            self.total_price += 800
        
        elif phone_model == self.cell_phones[1]:
            self.total_price += 6000

        elif phone_model == self.cell_phones[2]:
            self.total_price += 1000

        elif phone_model == self.cell_phones[3] or phone_model == self.cell_phones[4]:
            self.total_price += 900
        else:
            print("Phone model not found!")
            return self.total_price

        self.chosen_phones.append(phone_model)

        return self.total_price

    def unselect_cellphone(self, phone_model):
        if phone_model == self.cell_phones[0]:
            self.total_price -= 800
        
        elif phone_model == self.cell_phones[1]:
            self.total_price -= 6000

        elif phone_model == self.cell_phones[2]:
            self.total_price -= 1000

        elif phone_model == self.cell_phones[3] or phone_model == self.cell_phones[4]:
            self.total_price -= 900
        else:
            print("Phone model not found!")
            return self.total_price

        self.chosen_phones.remove(phone_model)

        return self.total_price

    def buy_message(self):

        if (self.chosen_phones is None or len(self.chosen_phones) == 0) \
                and self.internet_connection == False \
                and self.phone_lines <= 0 or self.total_price <= 0:

            return self.alert_string

        if self.total_price <= 0:
            return self.alert_string

        print("Your purchase have been confirmed")
