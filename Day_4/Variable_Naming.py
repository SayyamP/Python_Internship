#Variable naming rules


#Valid variable names
myvar = "Shiv" 
my_var = "Shiv"
_my_var = "Shiv"
myVar = "Shiv"
MYVAR = "Shiv"
myvar2 = "Shiv"


'''
#Invalid variable names
2myvar = "Shiv"
my-var = "Shiv"
my var = "Shiv"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)




print(2myvar)
print(my-var)
print(my var) 
'''


#Assigning Multiple Values to Multiple Variables


a = 50 ; b = "ABC" ; c = 5.45


print(a)
print(b)
print(c)


col1, col2, col3 = "red", "orange", "green"


print(col1)
print(col2)
print(col3) 


#Assigning one value to multiple variables


col1 = col2 = col3 = "Yellow"


print(col1)
print(col2)
print(col3) 


#Assigning values from list to variables


colours = ["Yellow", "Grenn", "Red"]


print("Assigning values from list to variables")


col1, col2, col3 = colours


print(col1)
print(col2)
print(col3)


#Multiple variables in one statement


x = "Shiv "
y = "is "
z = "awesome"


print(x + y + z)
print(x , y , z)


#In case of '+' operator 


x = 100
y = "shiv"
print(x + y)