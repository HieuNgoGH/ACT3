import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        test_input = "less8"
        expected = False
        self.assertFalse(check_pwd(test_input), expected)

    def test2(self):
        test_input = "morethantwentycharacters"
        expected = False
        self.assertFalse(check_pwd(test_input), expected)

    def test3(self):
        test_input = "CHECKFORLOWERCASE"
        expected = False
        self.assertFalse(check_pwd(test_input), expected)

    def test4(self):
        test_input = "checkforuppercase"
        expected = False
        self.assertFalse(check_pwd(test_input), expected)

    def test5(self):
        test_input = "123456789"
        expected = False
        self.assertFalse(check_pwd(test_input), expected)

    def test6(self):
        test_input = "passwordNosymbol"
        expected = False
        self.assertFalse(check_pwd(test_input), expected)


if __name__ == '__main__':
    unittest.main()

