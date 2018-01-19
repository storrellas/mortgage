# Libraries imports
import math

# Project imports
from lender import Lender

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
                lender = Lender(lender.name, lender.interest, principal)
                self.selected_lender_list.append ( lender )
                break;
            # Substract for next iteration
            principal = principal - lender.available
            self.selected_lender_list.append( lender )
        return self.selected_lender_list
        

    def calculate_repayment(self, principal):
        '''
        calculate repayment for all lenders
        '''
        
        if not(principal >= 1000 and principal <= 15000): 
            raise ValueError("principal exceeds range [1000,15000]")
        
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
        return True

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
