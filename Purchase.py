class Purchase:
    alert_string = "Dear user, your cart is empty. You need to purchase one or more items listed in the shop."
    cellphones = {"Motorola G99": 800, "iPhone 99": 6000, "Samsung Galaxy 99": 1000, "Sony Xperia 99": 900,
                  "Huawei 99": 900}

    def __init__(self, total_price=0, chosen_phones=None, phone_lines=0, internet_connection=False):
        self.total_price = total_price
        if chosen_phones is None:
            chosen_phones = []
        self.chosen_phones = chosen_phones
        self.phone_lines = phone_lines
        self.internet_connection = internet_connection

    def internet_package(self, package_deal):
        if self.internet_connection == package_deal:
            return self.total_price

        if package_deal:
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
        if phone_model in self.cellphones:
            self.total_price += self.cellphones.get(phone_model)
        else:
            print("Phone model not found!")
            return self.total_price

        self.chosen_phones.append(phone_model)

        return self.total_price

    def unselect_cellphone(self, phone_model):
        if phone_model in self.cellphones:
            self.total_price -= self.cellphones.get(phone_model)
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
        print("Phones: " + str(self.chosen_phones))
        print("Phone lines: " + str(self.phone_lines))
        print("Internet package: " + str(self.internet_connection))
        print("Total price is: " + str(self.total_price))