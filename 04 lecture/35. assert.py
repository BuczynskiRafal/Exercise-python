# Pytanie 34 - napisz fragment kodu, w którym zobrazujesz użycie słowa kluczowego assert.
# Wyjaśnij jaka jest rola testów jednostkowych i czym charakteryzuje się dobry test jednostkowy.


def mul(x, y):
    return x * y
#
#
# def test_mul_witch_int():
#     assert mul(2, 3) == 5
#
#
# def test_mul_witch_str():
#     assert mul('abc', 'zyx') == TypeError
#
#
# test_mul_witch_int()
# test_mul_witch_str()

import unittest


class TestMul(unittest.TestCase):

    def test_mul_witch_int(self):
        self.assertEqual(mul(2, 3), 6)

    def test_mul_witch_str(self):
        self.assertEqual(mul('abc', 'zyx'), TypeError)

if __name__ == '__main__':
    unittest.main(verbosity=2)