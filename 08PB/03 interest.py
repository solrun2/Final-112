def simple_interest(p, r, t) :
    interest = p*(r/100)*t + p
    return interest

def compound_interest(p, r, t) :
    fund = p*((1+(r/100))**t)
    return fund
    
p = float(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))

print('Return money for simple interest calculation is %.2f Baht.' % (simple_interest(p, r, t)))
print('Return money for compound interest calculation is %.2f Baht.' % (compound_interest(p, r, t)))