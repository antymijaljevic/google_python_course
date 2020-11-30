#!/home/amijaljevic/anaconda3/bin/python3

from rex import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    #pass
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    #fail
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()