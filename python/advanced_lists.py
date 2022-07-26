myList = [1,2,3,4,5,6,7,8]

# Ways to add something in a list
myList.append(9)
myList.append(10)
myList.insert(0,0)

# Ways to delete somthing in a list
myList.remove(7)
myList.pop()
del myList[3]


# Clear all list
# myList.clear()

print("INITIAL LENGTH")
print(len(myList))


#Looping a list
print("FOR IN LOOP")
for user in myList:
  print(user)

print("FOR IN RANGE LOOP")
for e in range(len(myList)):
  print(myList[e])

print("WHILE LOOP")
itr = 0
while itr < len(myList):
  print(myList[itr])
  itr = itr + 1

print("LOOPING LIST BY LIST COMPREHENSION")
[print(x) for x in myList]

# PRINT LIST
print(myList)


