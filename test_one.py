# content of test_one.py

class MainClass:
    __class_number = 20

    def get_local_number(self):
        return 14

    def get_class_number(self):
        return MainClass.__class_number


class TestMainClass:
    def test_get_local_number(self):
        assert MainClass.get_local_number(MainClass) == 14, "Local number does not equal 14"

    def test_get_class_number(self):
        assert MainClass.get_class_number(MainClass) > 45, "Class number is less than 45"

