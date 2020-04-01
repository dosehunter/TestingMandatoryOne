import pytest
from Purchase import Purchase

# How to run pytest:
# In console/terminal:
# py.test --junitxml test_results/results.xml test_purchase.py

class Test:
    @pytest.fixture()
    def resource(self):
        print("setup")
        yield "resource"
        print("teardown")

    # How to do dataproviders:
    @pytest.mark.parametrize("number, expected", [
        (2, True),
        (3, False),
        (4, True),
        (5, False)
    ])

    def test_is_even(self, number, expected):
        self.p = Purchase()
        assert self.p.is_even(number) == expected

    def test_more_is_even(self):
        self.p = Purchase()
        assert self.p.is_even(123) == False
        assert self.p.is_even(120) == True


    def test_internetPackage(self):
        pass

    def test_incTotalPhoneLines(self):
        pass

    def test_decTotalPhoneLines(self):
        pass

    def test_selectCellphone(self):
        pass

    def test_unselectCellphone(self):
        pass

    def test_buyMessage(self):
        pass