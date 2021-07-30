import unittest

from power import power, times


# 基本的には一つの関数に対して一つのテストメソッドを作る
class TestMyMethod(unittest.TestCase):
    def test_power(self):
        base = 2
        exp = 3
        # assert power(base, exp) == 8, "This should be 8"
        self.assertEqual(power(base, exp), 8)

        # context manager
        # 例外（ここでは　TypeError）が起きるかをチェックする
        # 例外を起こすコードを書く必要がある
        with self.assertRaises(TypeError):
            power("3", "2")


    def test_times(self):
        num1 = 2
        num2 = 3
        # assert times(num1, num2) == 6, "This should be 6"
        self.assertEqual(times(num1, num2), 6)


if __name__ == "__main__":
    unittest.main()