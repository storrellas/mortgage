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