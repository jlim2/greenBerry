#
# utils test
#

import sys
sys.path.append("..")

import unittest
from utils import capture_infix_eval_print

class GBUtilsTests(unittest.TestCase):
    def test_infix_eval_plus(self):
        x = '3+2+1'
        output = capture_infix_eval_print(x)
        self.assertEqual(output, '6')
    def test_infix_eval_minus(self):
        x = '3+2-1'
        output = capture_infix_eval_print(x)
        self.assertEqual(output, '4')
    def test_infix_eval_brackets(self):
        x = '(3 + 2) + 1'
        output = capture_infix_eval_print(x)
        self.assertEqual(output, '6')

if __name__ == '__main__':
    unittest.main(exit=False)
