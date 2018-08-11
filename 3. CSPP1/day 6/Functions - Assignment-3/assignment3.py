'''Functions - Assignment-3 - Using Bisection Search to Make the Program Faster'''

# You'll notice that in Problem 2, your monthly payment had to be a multiple of $10.
#Why did we make it that way? You can try running
# your code locally so that the payment can be any dollar and cent amount
#(in other words, the monthly payment is a multiple of $0.01).
# Does your code still work? It should, but you may notice that your
#code runs more slowly, especially in cases with very large balances
# and interest rates. (Note: when your code is running on our servers,
#there are limits on the amount of computing time each submission
# is allowed, so your observations from running this experiment on the
#grading system might be limited to an error message complaining
# about too much time taken.)
def payingdebtoffinayear(balance_bal, annual_interest_rate):
    '''paying debt off'''
    balance = balance_bal
    month_interest = (annual_interest_rate) / 12.0
    month_payment_low = balance_bal / 12
    month_payment_upp = (balance * (1 + month_interest) ** 12) / 12.0
    newbal = balance_bal
    epsilon = 0.03
    num = (month_payment_low + month_payment_upp) / 2
    while True:
        month = 1
        while month <= 12:
            newbal = newbal - num
            newbal = newbal + (month_interest * newbal)
            month += 1
        if newbal > 0 and newbal > epsilon:
            month_payment_low = num
            newbal = balance_bal
        elif newbal < 0 and newbal < -epsilon:
            month_payment_upp = num
            newbal = balance_bal
        else:
            return num
        num = (month_payment_low + month_payment_upp) / 2
def main():
    '''main'''
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", round(payingdebtoffinayear(data[0], data[1]), 2))
if __name__ == "__main__":
    main()
