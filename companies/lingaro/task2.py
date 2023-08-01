from inverter import invert


# def test_invert():
#     inverted = invert(None)

#     assert False

class TestClass:
    def test_invert_correct(self):
        assert invert("abcd") == "dcba"

    def test_invert_incorrect(self):
        assert invert("abcd") != "dbca"

    def test_invert_single(self):
        assert invert("a") == "a"

    def test_invert_none(self):
        assert invert(None) == ""

    def test_invert_empty(self):
        assert invert("") == ""
