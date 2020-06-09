#interst for given values.

def compound_interest(principle, rate, time):

    #calculates compound interest
    Ci = principle * (pow((1+rate/100), time))
    print('compound interest is', Ci)