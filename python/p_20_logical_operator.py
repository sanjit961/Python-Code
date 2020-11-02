#Logical Operator in Python:
#If applicant has high income AND good credit
#then he is eligible for loan

# Logical and operator ----> both condition should be true
# Logical or operator ----> at least one condition should be true.
# Logica not operator ----> it converses the value True ---> False, False ---> True


#Program: Logical AND Operator
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan :)")

#Prangram: Logical or operator
has_good_credit = False
has_high_income = True
if has_good_credit or has_high_income:
    print("You are Eligible for loan buddy...!!! Enjoy :)")


