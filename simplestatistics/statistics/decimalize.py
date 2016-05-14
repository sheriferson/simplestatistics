from decimal import *

# To avoid errors resulting from floating point arithmetic
# I will use the Decimal function to convert all numbers
# to type decimal before calculating variance
def decimalize(data):
    # if asked to decimalize one number
    if type(data) is int or type(data) is float:
        return(Decimal(data))
    # if asked to decimalize a list/vector
    else:
        for ii in range(len(data)):
            data[ii] = Decimal(data[ii])

        return(data)

