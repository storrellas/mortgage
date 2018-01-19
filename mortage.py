

''' 
mortgage_loan_calc1.py
calculate the monthly payment on a mortgage loan
tested with Python27 and Python33
'''
import math,csv
class Lender:
	name = ""
	interest = 0.0
	available = 0


	def __init__(self, name, interest, available):
		self.name = name
		self.interest = interest
		self.available = available
	def __str__(self):
		return "name=" + self.name + \
			";interest=" + str(self.interest) + \
			";capital=" + str(self.available)
	def __repr__(self):
		return "name=" + self.name + \
			";interest=" + str(self.interest) + \
			";capital="  + str(self.available)

class LoanCalculator:
	# total number of payments		
	n_payment = 36
	lender_list = []
	
	# Ouput
	payment_combined = 0.0
	average_interest = 0.0

	def __init__(self, lender_list):
		self.lender_list = lender_list
		
	# total number of payments (fixed to 36 months)
	n_payment = 36
	def calculate_repayment_per_lender(self, principal, interest):
		'''
		given mortgage loan principal, interest(%) and years to pay
		calculate and return monthly payment amount
		'''
		
		# monthly rate from annual percentage rate
		interest_rate = interest/12
		
		# calculate monthly payment
		payment = principal * \
		    (interest_rate/(1-math.pow((1+interest_rate), (-self.n_payment))))
		return payment


	def calculate_repayment(self):
		self.payment_combined = 0.0
		self.average_interest = 0.0
		for lender in self.lender_list:
			payment = self.calculate_repayment_per_lender(lender.available, lender.interest)
			print "payment for " + lender.name +"; payment=" + str(payment)
			self.payment_combined += payment
			self.average_interest += lender.interest
		self.average_interest = self.average_interest / len(self.lender_list)

	def get_average_interest():
		return self.average_interest

	def get_repayment():
		return self.payment_combined

if __name__ == "__main__":

	# Read CSV
	lender_list = []
	with open('market_data.csv') as csvfile:
	    readCSV = csv.reader(csvfile, delimiter=',')
	    data_list = iter(readCSV)
	    next(data_list)
	    for row in data_list:
		lender_list.append( Lender(row[0], float(row[1]), int(row[2]) ) )

		print(row)
		#print(row[0])
		#print(row[0],row[1],row[2],)

	# Sort lender_list by interest
	lender_list.sort(key=lambda x: x.interest)
	print lender_list


	
	principal = 1000

	print "++++++++++++++++"		
	selected_lender_list = []
	principal_local = principal
	for lender in lender_list:
		if principal_local <= lender.available:
			lender = Lender(lender.name, lender.interest, principal_local)
			selected_lender_list.append ( lender )
			break;
		# Substract for next iteration
		principal_local = principal_local - lender.available
		selected_lender_list.append( lender )

	print selected_lender_list
	print len(selected_lender_list)
	print "++++++++++++++++"


	print "-- Summary --"
	loan_calculator = LoanCalculator(selected_lender_list)
	loan_calculator.calculate_repayment()
	print "Requested amount: " + str(principal)
	print "Rate: " + str(loan_calculator.average_interest*100) + "%"
	print "Monthly repayment: " + str(loan_calculator.payment_combined)
	print "Total repayment: " + str(loan_calculator.total_payment * loan_calculator.n_payment)
	






