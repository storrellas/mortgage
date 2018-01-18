

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

# total number of payments (fixed to 36 months)
n_payment = 36
def calc_mortgage(principal, interest):
	'''
        given mortgage loan principal, interest(%) and years to pay
        calculate and return monthly payment amount
        '''

        # monthly rate from annual percentage rate
        interest_rate = interest/12

        # calculate monthly payment
        payment = principal * \
            (interest_rate/(1-math.pow((1+interest_rate), (-n_payment))))
        return payment



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


	print "-- Calculations --"
	total_payment = 0.0
	average_interest = 0.0
	for selected_lender in selected_lender_list:
		payment = calc_mortgage(selected_lender.available, selected_lender.interest)
		print "payment for " + selected_lender.name +"; payment=" + str(payment)
		total_payment += payment
		average_interest += selected_lender.interest
	average_interest = average_interest / len(selected_lender_list)

	print "-- Summary --"
	print "Requested amount: " + str(principal)
	print "Rate: " + str(average_interest*100) + "%"
	print "Monthly repayment: " + str(total_payment)
	print "Total repayment: " + str(total_payment * n_payment)
	exit(0)

	# mortgage loan principal
	principal = 1000
	# percent annual interest
	interest = 7.5
	# years to pay off mortgage
	years = 30
	# calculate monthly payment amount
	monthly_payment = calc_mortgage(principal, interest, years)
	# calculate total amount paid
	total_amount = monthly_payment * years * 12
	# show result ...
	# {:,} uses the comma as a thousands separator
	sf = '''\
	For a {} year mortgage loan of ${:,}
	at an annual interest rate of {:.2f}%
	you pay ${:.2f} monthly'''
	print(sf.format(years, principal, interest, monthly_payment))
	print('-'*40)
	print("Total amount paid will be ${:,.2f}".format(total_amount))
	''' result ...
	For a 30 year mortgage loan of $100,000
	at an annual interest rate of 7.50%
	you pay $699.21 monthly
	----------------------------------------
	Total amount paid will be $251,717.22
	'''





