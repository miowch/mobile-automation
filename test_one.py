# content of test_one.py

class MainClass:
    def get_local_number(self):
        return 14


class TestMainClass:
    def test_get_local_number(self):
        assert MainClass.get_local_number(MainClass) == 14, "Local number does not equal 14"


if __name__ =="__main__":
    TestMainClass.test_get_local_number(TestMainClass)
