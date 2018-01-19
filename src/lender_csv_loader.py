# Libraries imports
import csv

# Project imports
from lender import Lender

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
            if len(row) != 3:
                raise IOError("wrong column name")
            self.lender_list.append( Lender(row[0], float(row[1]), int(row[2]) ) )

  def get_lender_list(self):
    return self.lender_list