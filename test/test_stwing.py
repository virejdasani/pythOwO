import unittest

import pythowo


class TestStringOperators(unittest.TestCase):
    def test_lt_gt(self):
        value, err = pythowo.run("<test>", '"b" < "a"')
        result = value.elements[0].value
        self.assertEqual(result, 0)
        self.assertEqual(err, None)

    def test_lt_eq(self):
        value, err = pythowo.run("<test>", '"b" < "b"')
        result = value.elements[0].value
        self.assertEqual(result, 0)
        self.assertEqual(err, None)

    def test_lt_lt(self):
        value, err = pythowo.run("<test>", '"a" < "b"')
        result = value.elements[0].value
        self.assertEqual(result, 1)
        self.assertEqual(err, None)

    def test_le_gt(self):
        value, err = pythowo.run("<test>", '"b" <= "a"')
        result = value.elements[0].value
        self.assertEqual(result, 0)
        self.assertEqual(err, None)

    def test_le_eq(self):
        value, err = pythowo.run("<test>", '"b" <= "b"')
        result = value.elements[0].value
        self.assertEqual(result, 1)
        self.assertEqual(err, None)

    def test_le_lt(self):
        value, err = pythowo.run("<test>", '"a" <= "b"')
        result = value.elements[0].value
        self.assertEqual(result, 1)
        self.assertEqual(err, None)

    def test_gt_gt(self):
        value, err = pythowo.run("<test>", '"b" > "a"')
        result = value.elements[0].value
        self.assertEqual(result, 1)
        self.assertEqual(err, None)

    def test_gt_eq(self):
        value, err = pythowo.run("<test>", '"b" > "b"')
        result = value.elements[0].value
        self.assertEqual(result, 0)
        self.assertEqual(err, None)

    def test_gt_lt(self):
        value, err = pythowo.run("<test>", '"a" > "b"')
        result = value.elements[0].value
        self.assertEqual(result, 0)
        self.assertEqual(err, None)

    def test_ge_gt(self):
        value, err = pythowo.run("<test>", '"b" >= "a"')
        result = value.elements[0].value
        self.assertEqual(result, 1)
        self.assertEqual(err, None)

    def test_ge_eq(self):
        value, err = pythowo.run("<test>", '"b" >= "b"')
        result = value.elements[0].value
        self.assertEqual(result, 1)
        self.assertEqual(err, None)

    def test_ge_lt(self):
        value, err = pythowo.run("<test>", '"a" >= "b"')
        result = value.elements[0].value
        self.assertEqual(result, 0)
        self.assertEqual(err, None)

    def test_eq_gt(self):
        value, err = pythowo.run("<test>", '"b" == "a"')
        result = value.elements[0].value
        self.assertEqual(result, 0)
        self.assertEqual(err, None)

    def test_eq_eq(self):
        value, err = pythowo.run("<test>", '"b" == "b"')
        result = value.elements[0].value
        self.assertEqual(result, 1)
        self.assertEqual(err, None)

    def test_eq_lt(self):
        value, err = pythowo.run("<test>", '"a" == "b"')
        result = value.elements[0].value
        self.assertEqual(result, 0)
        self.assertEqual(err, None)

    def test_ne_gt(self):
        value, err = pythowo.run("<test>", '"b" != "a"')
        result = value.elements[0].value
        self.assertEqual(result, 1)
        self.assertEqual(err, None)

    def test_ne_eq(self):
        value, err = pythowo.run("<test>", '"b" != "b"')
        result = value.elements[0].value
        self.assertEqual(result, 0)
        self.assertEqual(err, None)

    def test_ne_lt(self):
        value, err = pythowo.run("<test>", '"a" != "b"')
        result = value.elements[0].value
        self.assertEqual(result, 1)
        self.assertEqual(err, None)


if __name__ == "__main__":
    unittest.main()
