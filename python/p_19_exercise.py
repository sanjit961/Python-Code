#Exercise :
#Price of a house is $1M.
#If buyer has a good credit,
#They need to put down 10%
#Otherwise
#they need to put down 20%
#print the down payment.


#My solution :
#is_good = False


#if is_good:
 #   print("Your downpayment is: $100000 ")
#else:
 #   print("Your downpayment is: $200000 ")

#Final Solution:

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")


