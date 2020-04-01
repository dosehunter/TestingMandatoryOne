import pytest
from Purchase import Purchase

class Test:
    @pytest.fixture()
    def resource(self):
        print("setup")
        yield "resource"
        print("teardown")

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