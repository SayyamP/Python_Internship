Name = "Shiv"


'''def myfunc():
 # print("My name is " + Name)


  Name = "ABC"
  print(Name) 


myfunc()
'''


def myfunc_2():


  global Name 
  Name = "ABC" 
  print(Name) 


myfunc_2()


print("My name is " + Name)