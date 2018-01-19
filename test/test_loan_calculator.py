import unittest


from lender import Lender
from loan_calculator import LoanCalculator

class TestLoanCalculator(unittest.TestCase):

    lender_list = []
    def setUp(self):
        self.lender_list = []
        self.lender_list.append( Lender("Bob", 0.075, 640) )
        self.lender_list.append( Lender("Jane", 0.069, 480) )
        self.lender_list.append( Lender("Mary", 0.104, 170) )

    def test_loan_calculator(self):
        
        principal = 1000
        loan_calculator = LoanCalculator( self.lender_list )
        result = loan_calculator.calculate_repayment( principal )
        self.assertTrue(result)

    def test_loan_calculator_below(self):
        try:
            principal = 100
            loan_calculator = LoanCalculator( self.lender_list )
            loan_calculator.calculate_repayment( principal )
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
    
    def test_loan_calculator_exceed(self):
        try:
            principal = 20000
            loan_calculator = LoanCalculator( self.lender_list )
            loan_calculator.calculate_repayment( principal )
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_loan_calculator_not_funds(self):
        try:
            principal = 5000
            loan_calculator = LoanCalculator( self.lender_list )
            loan_calculator.calculate_repayment( principal )
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()