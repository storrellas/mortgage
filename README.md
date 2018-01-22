# Description
This project contains the performance tests for the *CORE modules*.
It is meant to figure out how to dimension an environment or to know the current concurrence limitations.

In the project these tests can be found under directory _/src/test/scala/simulations_ where they might be grouped by project.
The objects/endpoints are modeled under projects's simulations folder in order to make the code reusable among tests.
All needed data-input is stored under _/src/test/resources_

There is a need for a rate calculation system allowing prospective borrowers to obtain a quote
from our pool of lenders for 36 month loans. This system will take the form of a command-line
application.
You will be provided with a file containing a list of all the offers being made by the lenders within
the system in CSV format, see the example market.csv file provided alongside this specification.
You should strive to provide as low a rate to the borrower as is possible to ensure that Zopa's
quotes are as competitive as they can be against our competitors'. You should also provide the
borrower with the details of the monthly repayment amount and the total repayment amount.
Repayment amounts should be displayed to 2 decimal places and the rate of the loan should be
displayed to one decimal place.
Borrowers should be able to request a loan of any £100 increment between £1000 and £15000
inclusive. If the market does not have sufficient offers from lenders to satisfy the loan then the
system should inform the borrower that it is not possible to provide a quote at that time.
The application should take arguments in the form:

```
cmd> [application] [marke_file] [loan_amount]
```

# Dependencies
* Python 2.7
* VirtualEnv 1.11.4
* nose

# Usage
```
* Run application: python src/main.py [market_file] [loan_amount]
* Run tests: pip install nose; nosetests
```
