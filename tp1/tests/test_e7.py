import unittest
from p1.e7 import convert


class TestCaseE7(unittest.TestCase):
    def test_e7(self):
        convert("MOCK_DATA.csv", "MOCK_DATA_r.csv")
        with open("MOCK_DATA_r.csv", "r") as f, open("MOCK_DATA_RESULT.csv", "r") as f2:
            content_file1 = f.readlines()
            content_file2 = f2.readlines()
            self.assertEqual(len(content_file1), len(content_file2))
            for i in range(len(content_file1)):
                with self.subTest(i):
                    self.assertEqual(content_file1[i], content_file2[i])


if __name__ == '__main__':
    unittest.main()
