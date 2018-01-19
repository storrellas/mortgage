import unittest


from lender import Lender
from loan_calculator import LoanCalculator

class TestLoanCalculator(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_loan_calculator(self):
        lender_list = []
        lender_list.append( Lender("Bob", 0.075, 640) )
        loan_calculator = LoanCalculator( lender_list )

if __name__ == '__main__':
    unittest.main()