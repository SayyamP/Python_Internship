'''tuple1 = ("Apple","Banana","Cheery","Banana",10,20,10.3)
print(tuple1)

#len
print(len(tuple1))

 #creating  tuple using tuple() constructor
 tuple2 = tuple(("Rahul","Ramesh","Ramya"))
 print(tuple2)

 #single element tuple
 tuple3 = ("one")
 print(tuple3)
 print(type(tuple3))

 tuple4 = ("one",)
 print(type(tuple4))

 print(tuple2[2])

 #tuple is unchangable, we cant asign the value to the tuple after creating it.
 # tuple4[1] = "two"
 # print(tuple4)
  
#converting tuples to list for modifying purpose
list1 = list(tuple2)
list1.insert(2,"Sameer")
new_tuple = tuple(list)
print(new_tuple)'''

#packing of tuple
fruits = ("Apple","Banana","Cheery")

#Unpacking of tuple
( fruits1, fruits2, fruits3) = fruits
print(fruits1, fruits2, fruits3)

colors = ("Red", "Pink", "Black", "White", "Blue", "Purple")
(red, pink, black, *others) = colors
print(red, pink, black, others)

(red1, pink1, *others1, blue, purple) = colors
print(red1,pink1,others1,blue,purple)

t_colors = ("Black","White","Red")
t_numbers = (10,20,30,40,20,30,40,20,30,40,20,30,40,20,30,40,20,30,40,20,30,40,20,30,40,20,30,40,20,30,40,20,30,40)

combine_tuple = t_colors + t_numbers
print(combine_tuple)

repeted_tuple = t_numbers * 5
print(repeted_tuple)

#count() number of occuries
print(t_numbers.count(30))

#index()
print(t_numbers.index(30))

