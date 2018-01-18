

''' 
mortgage_loan_calc1.py
calculate the monthly payment on a mortgage loan
tested with Python27 and Python33
'''
import math
import csv
def calc_mortgage(principal, interest, years):
	'''
        given mortgage loan principal, interest(%) and years to pay
        calculate and return monthly payment amount
        '''
        # monthly rate from annual percentage rate
        interest_rate = interest/(100 * 12)
        # total number of payments
        payment_num = years * 12
        # calculate monthly payment
        payment = principal * \
            (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))
        return payment


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

def getKey(item):
	return item.interest



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

	# Sort list by interest
	lender_list.sort(key=lambda x: x.interest)
	print lender_list


	
	principal = 1000

	print "++++++++++++++++"		
	captured_lender_list = []
	principal_local = principal
	for lender in lender_list:
		principal_local = principal_local - lender.available
		if principal_local < 0:
			break;
		captured_lender_list.append( lender )

	print captured_lender_list
	print "++++++++++++++++"

	interest_rate = 0.07 /12 
	payment_num = 36	
	payment = principal * \
            (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))
	print payment
	print interest_rate
	print payment*36
	#exit(0)

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





