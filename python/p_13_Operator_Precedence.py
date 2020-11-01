#Operator Precedence:
#Precedence ---->>>> Priority
x = 10 + 3 * 2  #Multiplication has higher precedence then addition so multiplication is done first
print(x)

# ORDER OF PRECEDENCE :
#    --->  Parenthesis () eg; (10 + 4) * 2 ** 3
#    --->  Exponentiation 2 ** 3
#    --->  {* , / } multiplication or Division
#    --->  {+, - }  Addition or subtraction

#More Example :
a = 10 + 3 * 2 ** 2  #first 2 ** 2 is performed and the result of this is multipled with 3 and at the last added
print(a)

#More Example with parenthesis:
y = (10 + 3) * 2 ** 2
print(y)

#Exercise :
c = (2 + 3) * 10 - 3
print(c)


