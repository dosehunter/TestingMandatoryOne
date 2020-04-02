from Purchase import Purchase


class Splitter:
    def split_request(self, post_body):
        print(post_body)
        catagories = post_body.decode("utf-8").split("&")
        phones = catagories[0].replace('+', ' ')[catagories[0].index("=") + 1:].split("%2C")
        phone_lines = catagories[1][catagories[1].index("=") + 1:]
        inter_connections = False if catagories[2][catagories[2].index("=") + 1:] == "false" else True

        self.create_purchase(phones, phone_lines, inter_connections)

        return phones, phone_lines, inter_connections

    def create_purchase(self, phones, phone_lines, inter_connections):
        purchase = Purchase()

        for phone in phones:
            purchase.select_cellphone(phone)

        for phone_line in range(int(phone_lines)):
            purchase.inc_total_phone_lines()

        purchase.internet_package(inter_connections)

        purchase.buy_message()