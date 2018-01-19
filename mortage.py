import math,csv

class Lender:
	''' 
	Class containing Lender data
	'''
	
	name = ""       # Lender name
	interest = 0.0  # Interest rate
	available = 0.0 # Cash available   


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

class LenderCSVLoader:
	''' 
	Class Loading Lender Data from CSV file
	'''
	
	filename = ""
	lender_list = []
	
	def __init__(self, filename):
		self.filename = filename
		self.lender_list = []
		
		# Read CSV
		self.lender_list = []
		with open(self.filename) as csvfile:
		    readCSV = csv.reader(csvfile, delimiter=',')
		    data_list = iter(readCSV)
		    next(data_list)
		    for row in data_list:
			self.lender_list.append( Lender(row[0], float(row[1]), int(row[2]) ) )

	def get_lender_list(self):
		return self.lender_list
	

class LoanCalculator:
	''' 
	Calculates loan
	'''
	
	# total number of payments		
	n_payment = 36
	lender_list = []
	selected_lender_list = []
	
	# Input
	principal = 0.0
	
	# Ouput
	payment_combined = 0.0
	average_interest = 0.0

	def __init__(self, lender_list):
		self.lender_list = lender_list	
		# Sort lender_list by interest to facilitate selection of lenders
		self.lender_list.sort(key=lambda x: x.interest)
		
	def calculate_repayment_per_lender(self, principal, interest):
		'''
		given mortgage loan principal, interest(%) 
		calculate and return monthly payment amount per lender
		'''
		
		# monthly rate from annual percentage rate
		interest_rate = interest/12
		
		# calculate monthly payment (See: https://en.wikipedia.org/wiki/Mortgage_calculator)
		payment = principal * \
		    (interest_rate/(1-math.pow((1+interest_rate), (-self.n_payment))))
		return payment


	def calculate_selected_lenders(self, principal):
		'''
		calculate list of selected_lenders according to principal
		'''
		self.selected_lender_list = []
		for lender in self.lender_list:
			if self.principal <= lender.available:
				lender = Lender(lender.name, lender.interest, self.principal)
				self.selected_lender_list.append ( lender )
				break;
			# Substract for next iteration
			self.principal = self.principal - lender.available
			self.selected_lender_list.append( lender )
		return self.selected_lender_list
		

	def calculate_repayment(self, principal):
		'''
		calculate repayment for all lenders
		'''
		
		self.principal = principal
		# Calculate Selected Lender_list
		self.selected_lender_list = self.calculate_selected_lenders(principal)

		
		# Calculate repayment
		self.payment_combined = 0.0
		self.average_interest = 0.0
		for lender in self.selected_lender_list:
			payment = self.calculate_repayment_per_lender(lender.available, lender.interest)
			#print "payment for " + lender.name +"; payment=" + str(payment)
			self.payment_combined += payment
			self.average_interest += lender.interest
		self.average_interest = self.average_interest / len(self.selected_lender_list)

	def get_average_interest(self):
		return self.average_interest

	def get_repayment(self):
		return self.payment_combined

	def get_total_repayment(self):
		return self.payment_combined * self.n_payment

	def get_interest(self):
		return self.average_interest

	def get_principal(self):
		return self.principal

if __name__ == "__main__":

	principal = 1000
	filename = "market_data.csv"

	# Load Lender CSV 
	lender_loader = LenderCSVLoader( filename )
	loan_calculator = LoanCalculator(lender_loader.get_lender_list())
	loan_calculator.calculate_repayment( principal )
	
	print "-- Results --"
	print "Requested amount: " + str(loan_calculator.get_principal())
	print "Rate: " + str(loan_calculator.get_interest()*100) + "%"
	print "Monthly repayment: " + str(loan_calculator.get_repayment())
	print "Total repayment: " + str(loan_calculator.get_total_repayment())
	






