class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#Function can Return a Boolean Value:

def myFunction():
    return True
print(myFunction())

#More Example on Functios:
 
def myFunction():
    return False
if myFunction():
    print("Yes..!!!")
else:
    print("No...!!!")

#More Example:
x  = 200
print(isinstance(x, int))




