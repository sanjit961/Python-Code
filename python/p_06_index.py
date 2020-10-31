#Index in Python
course = 'Python for Beginners'
print(course[0])                #index = [0], [1], [2],so on....

#we can also use negative index --->>> [-1], [-2], [-3], so on...
print(course[-1])                      # Negative prints from ending of the sentence..
print(course[-5])

#It can also print a range 
#Syntax --->> print(name_of_any[0:3])

print(course[0:4])

#Default index
print(course[0:])
print(course[:5])

print(course [:]) # It copies all the indexes...

another = course[:] #Copies the content of course
print(another)


