#Syntax
mySet = {"Tesla", "Ferrari", "BMW", "Aston Martin" , "Tesla"}
mySet2 = {"Chevrolet", "Nissan", "Tesla"}

#looping a set
for el in mySet:
  print(el)

#some methods
mySet.add("ADDD")
mySet.add("BMW")
mySet.update(mySet2)

my_newSet = mySet.union(mySet2)

print(mySet)
print(my_newSet)
print(type(mySet))