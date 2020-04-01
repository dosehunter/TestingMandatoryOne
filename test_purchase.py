import pytest
from Purchase import Purchase

# How to run pytest:
# In console/terminal:
# py.test --junitxml test_results/results.xml test_purchase.py
# CREATE SOME FALSE POSITIVES

class Test:

    #@pytest.fixture()
    #def resource(self):
    #    yield Purchase()

    def test_internetPackage(self):
        p = Purchase()        # Make to a fixture! Or something cooler
        assert p.internetPackage(True) == 200
        assert p.internetPackage(False) == 0

    def test_incTotalPhoneLines(self):
        p = Purchase()
        assert p.incTotalPhoneLines() == 150
        assert p.incTotalPhoneLines() == 300

        for i in range(4):
            p.incTotalPhoneLines()
        assert p.incTotalPhoneLines() == 1050
        assert p.incTotalPhoneLines() == 1200
        assert p.incTotalPhoneLines() == 1200  # Trying to add 9 phonelines

    def test_decTotalPhoneLines(self):
        p = Purchase()
        for i in range(8):
            p.incTotalPhoneLines()
        assert p.phoneLines == 8
        assert p.totalPrice == 1200

        assert p.decTotalPhoneLines() == 1050
        assert p.decTotalPhoneLines() == 900

        for i in range(4):
            p.decTotalPhoneLines()
        assert p.decTotalPhoneLines() == 150
        assert p.decTotalPhoneLines() == 0
        assert p.decTotalPhoneLines() == 0  # Trying to remove to under 0 phonelines

    @pytest.mark.parametrize("model, expected_price", [
        ("Motorola G99", 800),
        ("iPhone 99", 6000),
        ("Samsung Galaxy 99", 1000),
        ("Sony Xperia 99", 900),
        ("Huawei 99", 900),
        ("oyuiafk", 0)
    ])
    def test_selectCellphone(self, model, expected_price):
        p = Purchase()
        assert p.selectCellphone(model) == expected_price

    @pytest.mark.parametrize("model, expected_price", [
        ("Motorola G99", 9200),
        ("iPhone 99", 4000),
        ("Samsung Galaxy 99", 9000),
        ("Sony Xperia 99", 9100),
        ("Huawei 99", 9100)
    ])
    def test_unselectCellphone(self, model, expected_price):
        p = Purchase()
        p.totalPrice = 10000
        assert p.totalPrice == 10000

        assert p.unselectCellphone(model) == expected_price

    def test_buyMessage(self):
        p = Purchase()
        assert p.buyMessage() == "Dear user, your cart is empty. You need to purchase one or more items listed in the shop."


    '''@pytest.fixture()
    def resource(self):
        print("setup")
        yield "resource"
        print("teardown")
'''