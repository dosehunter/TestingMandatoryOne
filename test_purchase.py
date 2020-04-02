import pytest
from Purchase import Purchase

# How to run pytest:
# py.test --junitxml test_results/results.xml test_purchase.py -v


class TestPurchase:

    # Fixture with empty Purchase test
    # yield is preferred as we will still get to tear down anything afterwards, like an open file
    @pytest.fixture()
    def purchase(self):
        p = Purchase()
        yield p

    # Fixture with total price=10000 and internet selected
    @pytest.fixture()
    def purchase_internet(self):
        p = Purchase(10000, [], 0, True)
        yield p

    # Fixture with cart money and phones
    @pytest.fixture()
    def purchase_with(self):
        p = Purchase(10000, [
            "Motorola G99",
            "iPhone 99",
            "Samsung Galaxy 99",
            "Sony Xperia 99",
            "Huawei 99"
        ], 8)

        yield p

    # input = test method parameter, result = total price, expected = whether result was indeed expected
    @pytest.mark.parametrize("input, result, expected", [
        (True, 10200, True),        # Valid, price should increase with 200
        (True, 10000, False),       # Invalid, price should increase
    ])
    # Test toggling internet package on or off, purchase = fixture
    def test_internet_package(self, purchase_with, input, result, expected):
        assert (purchase_with.internet_package(input) == result) == expected

    # input = test method parameter, result = total price, expected = whether result was indeed expected
    @pytest.mark.parametrize("input, result, expected", [
        (False, 9800, True),        # Valid, price should decrease with 200
        (False, 10000, False),      # Invalid, price should decrease
    ])
    # Test toggling internet package on or off, purchase = fixture
    def test_internet_package(self, purchase_internet, input, result, expected):
        assert (purchase_internet.internet_package(input) == result) == expected

    # Testing Incrementing phone lines, purchase = fixture
    def test_inc_total_phone_lines(self, purchase):
        assert purchase.inc_total_phone_lines() == 150  # Test case => 1 phone line added
        assert purchase.inc_total_phone_lines() == 300  # Test case => 2 phone line added

        # Skips 4 steps
        for i in range(4):
            purchase.inc_total_phone_lines()

        assert purchase.inc_total_phone_lines() == 1050  # Test case => 7 phone line added
        assert purchase.inc_total_phone_lines() == 1200  # Test case => 8 phone line added
        assert purchase.inc_total_phone_lines() == 1200  # Test case => 9 phone line added

    # Checks decrementing phone lines, purchase = fixture
    def test_dec_total_phone_lines(self, purchase):
        # Adds 8 phone lines
        for i in range(8):
            purchase.inc_total_phone_lines()

        assert purchase.phone_lines == 8  # Test case => Whether 8 phone lines are added
        assert purchase.total_price == 1200  # Test case => 1 phone line added

        assert purchase.dec_total_phone_lines() == 1050  # Test case => 7 phone line added
        assert purchase.dec_total_phone_lines() == 900  # Test case => 6 phone line added

        # Removes 4 phone lines
        for i in range(4):
            purchase.dec_total_phone_lines()

        assert purchase.dec_total_phone_lines() == 150  # Test case => 1 phone line added
        assert purchase.dec_total_phone_lines() == 0  # Test case => 0 phone line added
        assert purchase.dec_total_phone_lines() == 0  # Trying to remove to under 0 phonelines

    # model = Phone model (String)  result = expected total price   expected = added to list
    @pytest.mark.parametrize("model, result, expected", [
        ("Motorola G99", 800, True),                    # Test correct phone models * 5
        ("iPhone 99", 6000, True),
        ("Samsung Galaxy 99", 1000, True),
        ("Sony Xperia 99", 900, True),
        ("Huawei 99", 900, True),
        ("G99", 0, False),                              # Test subpart of string
        ("", 0, False),                                 # Test an empty string
        ("Huawei 99 Sony Xperia 99", 0, False),         # Test to strings concatenated
        ("æøå-.,+0&/(!\"#%¤&?`)=âàáä*`|", 0, False),    # Test uncommon characters
        (None, 0, False),                               # Test None
    ])
    # Testing selecting a phone, as well as list status, purchase = fixture
    def test_select_cellphone(self, model, result, purchase, expected):
        # Checks whether the total price is what we expect it to be
        assert purchase.select_cellphone(model) == result

        # Checks if the phone_list has added our model and if it should!
        assert ([model] == purchase.chosen_phones) == expected

    # model = Phone model (String)  result = expected total price   expected = Whether the combination is correct or not
    @pytest.mark.parametrize("model, result, expected", [
        ("Motorola G99", 9200, True),                   # Test correct phone models * 5
        ("iPhone 99", 4000, True),
        ("Samsung Galaxy 99", 9000, True),
        ("Sony Xperia 99", 9100, True),
        ("Huawei 99", 9100, True),
        ("huawei 98", 9100, False),                     # Test a similar string
        ("iPhone 99 Samsung Galaxy 99", 4000, False),   # Test to strings concatenated
        ("æøå-.,+0&/(!\"#%¤&?`)=âàáä*`|", 0, False),  # Test uncommon characters
        ("", 0, False),                                 # Test an empty string
        (None, 0, False),                               # Test None
    ])
    # Testing unselecting a phone, as well as list status, purchase_with = fixture
    def test_unselect_cellphone(self, model, result, expected, purchase_with):
        # Making a copy so we can check if the product has been removed from the list
        phone_list = purchase_with.chosen_phones.copy()

        # Checks whether the total price is what's expected
        assert (purchase_with.unselect_cellphone(model) == result) == expected

        # Phone list is not the same as before test ran!
        assert (purchase_with.chosen_phones != phone_list) == expected

    # purchase_cases = Purchase class test case, expected = if allowed to buy or not
    # Purchase class constructor: (total_price=0, chosen_phones=None, phone_lines=0, internet_connection=False)
    @pytest.mark.parametrize("purchase_cases, expected", [
        (Purchase(), False),                                    # Invalid, empty purchase
        (Purchase(10000), False),                               # Invalid, empty purchase with a total price > 0
        (Purchase(10000, ["Motorola G99"]), True),              # Valid, price = 10000, and 1 phone chosen
        (Purchase(1, [], 5), True),                             # Valid, price > 0 and 5 phone lines
        (Purchase(50000, [], 0, True), True),                   # Valid, price > 0 and internet package chosen
        (Purchase(382.89, ["Motorola G99"], 8, True), True),    # Valid, price = float > 0, phone chosen, phone lines chosen and internet chosen
        (Purchase(-1, ["Motorola G99"], 8, True), False),       # Invalid, price < 0
        (Purchase(0, ["Sad dog"], 8, True), False),             # Invalid, price == 0
        (Purchase(0.01, [None, None], -1), True),               # Valid, price > 0, "phones chosen"
        (Purchase(42, [], -1, 0), False),                       # Invalid, nothing in cart (phone lines < 0)
    ])
    # Testing when user wants to buy a phone
    def test_buy_message(self, purchase_cases, expected):
        # If we get an alert, we're not alowed to buy anything
        # Match test case vs alert and check if it was expected or not
        assert (purchase_cases.buy_message() != purchase_cases.alert_string) == expected

