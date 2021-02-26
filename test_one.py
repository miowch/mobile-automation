# content of test_one.py

class MainClass:
    __class_number = 20
    __class_string = "Hello, world"

    def get_local_number(self):
        return 14

    def get_class_number(self):
        return MainClass.__class_number

    def get_class_string(self):
        return MainClass.__class_string


class TestMainClass:
    def test_get_local_number(self):
        assert MainClass.get_local_number(MainClass) == 14, "Local number does not equal 14"

    def test_get_class_number(self):
        assert MainClass.get_class_number(MainClass) > 45, "Class number is less than 45"

    def test_get_class_string(self):
        assert \
            "hello" in MainClass.get_class_string(MainClass) or \
            "Hello" in MainClass.get_class_string(MainClass), \
            "Class string does not contain 'hello' or 'Hello'"
