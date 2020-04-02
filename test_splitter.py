import pytest
from Splitter_Class import Splitter

# Simple input validater
class TestSplitter:

    @pytest.fixture()
    def splitter(self):
        splitter = Splitter()
        yield splitter

    @pytest.mark.parametrize("input, expected_phone_lines, expected_phones, expected_internet", [
        (b'phones=Motorola+G99%2CHuawei+99&phoneLine=-1&internet=false'         , -1    , ["Motorola G99", "Huawei 99"]             , False),
        (b'phones=Motorola+G99&phoneLine=0&internet=false'                      , 0     , ["Motorola G99"]                          , False),
        (b'phones=iPhone+99%2CiPhone+99%2CiPhone+99&phoneLine=1&internet=true ' , 1     , ["iPhone 99","iPhone 99","iPhone 99"]     , True),
        (b'phones=&phoneLine=8&internet=true'                                   , 8     , ['']                                      , True),
        (b'phones=&phoneLine=9&internet=false'                                  , 9     , ['']                                      , False),
    ])
    def test_split_request(self, splitter, input, expected_phone_lines, expected_phones, expected_internet):
        phones, phone_lines, inter_connections = splitter.split_request(input)

        assert int(phone_lines) == expected_phone_lines
        assert phones == expected_phones
        assert inter_connections == expected_internet