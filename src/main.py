import math,csv,sys

from lender import Lender
from loan_calculator import LoanCalculator
from lender_csv_loader import LenderCSVLoader
	
if __name__ == "__main__":

	principal = 1000
	filename = ""
	# Grab command-line results
	if len(sys.argv) >= 2:
		filename = sys.argv[1]
	if len(sys.argv) >= 3:
		principal = float(sys.argv[2])

	# Load Lender CSV 
	lender_loader = LenderCSVLoader( filename )
	loan_calculator = LoanCalculator(lender_loader.get_lender_list())
	loan_calculator.calculate_repayment( principal )
	
	print "-- Results --"
	print "Requested amount: " + str(loan_calculator.get_principal())
	print "Rate: " + str(loan_calculator.get_interest()*100) + "%"
	print "Monthly repayment: " + str(loan_calculator.get_repayment())
	print "Total repayment: " + str(loan_calculator.get_total_repayment())
	






