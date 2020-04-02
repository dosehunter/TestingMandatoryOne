import pytest
from Purchase import Purchase

# How to run pytest:
# py.test --junitxml test_results/results.xml test_purchase.py -v


class TestPurchase:
    # <editor-fold desc=" Start of setting up test classes">
    # yield is preferred as we will still get to tear down anything afterwards, e.g an open file

    # Fixture with empty Purchase test
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

    # </editor-fold>

    # input = test method parameter
    # result = total price returned
    # expected = whether result was indeed expected
    @pytest.mark.parametrize("input, result, expected", [
        (True,      10200,  True),                  # Valid, price should increase with 200
        (True,      10000,  False),                 # Invalid, price should increase
    ])
    def test_internet_package_on(self, purchase_with, input, result, expected):
        assert (purchase_with.internet_package(input) == result) == expected

    # input = test method parameter
    # result = total price returned
    # expected = whether result was indeed expected
    @pytest.mark.parametrize("input, result, expected", [
        (False,     9800,   True),                  # Valid, price should decrease with 200
        (False,     10000,  False),                 # Invalid, price should decrease
    ])
    def test_internet_package_off(self, purchase_internet, input, result, expected):
        assert (purchase_internet.internet_package(input) == result) == expected

    def test_inc_total_phone_lines(self, purchase):
        assert purchase.inc_total_phone_lines() == 150           # => 1 phone line added
        assert purchase.inc_total_phone_lines() == 300           # => 2 phone line added

        # Skips 4 steps
        for i in range(4):
            purchase.inc_total_phone_lines()

        assert purchase.inc_total_phone_lines() == 1050           # => 7 phone line added
        assert purchase.inc_total_phone_lines() == 1200           # => 8 phone line added
        assert purchase.inc_total_phone_lines() == 1200           # => 9 phone line added

    def test_dec_total_phone_lines(self, purchase):
        # Adds 8 phone lines
        for i in range(8):
            purchase.inc_total_phone_lines()

        assert purchase.phone_lines == 8  # Test case => Whether 8 phone lines are added
        assert purchase.total_price == 1200  # Test case => 1 phone line added

        assert purchase.dec_total_phone_lines() == 1050             # => 7 phone line added
        assert purchase.dec_total_phone_lines() == 900              # => 6 phone line added

        # Removes 4 phone lines
        for i in range(4):
            purchase.dec_total_phone_lines()

        assert purchase.dec_total_phone_lines() == 150              # => 1 phone line added
        assert purchase.dec_total_phone_lines() == 0                # => 0 phone line added
        assert purchase.dec_total_phone_lines() == 0                # Trying to remove to under 0 phonelines

    # model = Phone model (String)
    # result = total price (number)
    # expected = If combination is correct
    @pytest.mark.parametrize("model, result, expected", [
        ("Motorola G99",                    800,    True),      # Test correct phone models * 5
        ("iPhone 99",                       6000,   True),
        ("Samsung Galaxy 99",               1000,   True),
        ("Sony Xperia 99",                  900,    True),
        ("Huawei 99",                       900,    True),
        ("G99",                             0,      False),     # Test subpart of string
        ("",                                0,      False),     # Test an empty string
        ("Huawei 99 Sony Xperia 99",        0,      False),     # Test to strings concatenated
        ("æøå-.,+0&/(!\"#%¤&?`)=âàáä*`|",   0,      False),     # Test uncommon characters
        (None,                              0,      False),     # Test None
    ])
    def test_select_cellphone(self, model, result, purchase, expected):
        # If total price == expected
        assert purchase.select_cellphone(model) == result

        # If phone list is updated
        assert ([model] == purchase.chosen_phones) == expected

    # model = Phone model (String)
    # result = total price (number)
    # expected = If combination is correct
    @pytest.mark.parametrize("model, result, expected", [
        ("Motorola G99",                    9200,   True),     # Test correct phone models * 5
        ("iPhone 99",                       4000,   True),
        ("Samsung Galaxy 99",               9000,   True),
        ("Sony Xperia 99",                  9100,   True),
        ("Huawei 99",                       9100,   True),
        ("huawei 99",                       9100,   False),    # Test case sensitivity
        ("iPhone 99 Samsung Galaxy 99",     4000,   False),    # Test to strings concatenated
        ("æøå-.,+0&/(!\"#%¤&?`)=âàáä*`|",   0,      False),    # Test uncommon characters
        ("",                                0,      False),    # Test an empty string
        (None,                              0,      False),    # Test None
    ])
    def test_unselect_cellphone(self, model, result, expected, purchase_with):
        # List Before vs After
        phone_list = purchase_with.chosen_phones.copy()

        # Checks if "total price == reuslt" is expected
        assert (purchase_with.unselect_cellphone(model) == result) == expected

        # Phone list is not the same as before test ran!
        assert (purchase_with.chosen_phones != phone_list) == expected

    # purchase_cases = Purchase class test case
    # expected = if allowed to buy or not
    @pytest.mark.parametrize("purchase_cases, expected", [
        (Purchase(),                                  False),      # Invalid, empty purchase
        (Purchase(10000),                             False),      # Invalid, empty purchase, total price > 0
        (Purchase(10000, ["Motorola G99"]),           True),       # Valid, price = 10000, and 1 phone chosen
        (Purchase(1, [], 5),                          True),       # Valid, price > 0 and 5 phone lines
        (Purchase(50000, [], 0, True),                True),       # Valid, price > 0 with internet package
        (Purchase(382.89, ["Motorola G99"], 8, True), True),       # Valid, price = float > 0, phone chosen, phone lines chosen and internet chosen
        (Purchase(0.01, [None, None], -1),            True),       # Valid, price > 0, "phones chosen"
        (Purchase(-1, ["Motorola G99"], 8, True),     False),      # Invalid, price < 0
        (Purchase(0, ["Sad dog"], 8, True),           False),      # Invalid, price == 0
        (Purchase(42, [], -1, 0),                     False)       # Invalid, nothing in cart (phone lines < 0)
    ])
    def test_buy_message(self, purchase_cases, expected):
        assert (purchase_cases.buy_message() != purchase_cases.alert_string) == expected



''' # Alternative 
    @pytest.mark.parametrize("purchase, input, result, expected", [
        (Purchase(10000, [], 0 ,False), True, 10200, True),        # Valid, price should increase with 200
        (Purchase(10000, [], 0 ,False), True, 10000, False),       # Invalid, price should increase
        (Purchase(10000, [], 0 ,True), False, 9800, True),        # Valid, price should decrease with 200
        (Purchase(10000, [], 0 ,True), False, 10000, False),      # Invalid, price should decrease
    ])
    def test_internet_package(self, purchase, input, result, expected):
        assert (purchase.internet_package(input) == result) == expected
'''