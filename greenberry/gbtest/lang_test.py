#
# language tests
#

import sys
sys.path.append("..")

import unittest
from greenBerry import greenBerry_eval
from utils import capture_gb_eval_print

class GBLangTests(unittest.TestCase):

    def test_printd(self):
        pass

    def test_null(self):
        # check null input
        x = ''
        try:
            greenBerry_eval(x)
        except:
            error = True
        self.assertTrue(error)

    def test_eval_add(self):
        x = 'print eval 1+2'
        output = capture_gb_eval_print(x)
        self.assertEqual(output, '3')

    def test_eval_minus(self):
        x = 'print eval 3-2'
        output = capture_gb_eval_print(x)
        self.assertEqual(output, '1')

    def test_eval_times(self):
        x = 'print eval 3*2'
        output = capture_gb_eval_print(x)
        self.assertEqual(output, '6')

    def test_eval_divide(self):
        x = 'print eval 10/2'
        output = capture_gb_eval_print(x)
        self.assertEqual(output, '5.0')

    def test_eval_mixed_ops(self):
        x = 'print eval 1*3+10+3-2/2'
        output = capture_gb_eval_print(x)
        self.assertEqual(output, '15.0')

    def test_eval_mixed_ops(self):
        x = 'print eval 1*3+10+3-2/2+(3+2)'
        output = capture_gb_eval_print(x)
        self.assertEqual(output, '20.0')

if __name__ == '__main__':
    unittest.main(exit=False)
