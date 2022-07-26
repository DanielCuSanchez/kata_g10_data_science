myDictionary1 = {
  "name": "Daniel",
  "last_name":"Cu"
}

myDictionary2 = {
  "name": "David",
  "last_name":"Ku"
}
myDictionary3 = {
  "name": "Juan Carlos",
  "last_name":"Villacorta"
}

employeesDictionary = {
  "0": myDictionary1,
  "1": myDictionary1,
  "2": myDictionary2,
  "3": myDictionary3
}

#print(employeesDictionary["1"]["name"])

for id in employeesDictionary:
  print(employeesDictionary[id]["name"])

# methods
newD = {}
#print(newD.fromkeys("psi"))

# Returns the key value
print(employeesDictionary.get("2"))

# Removes the specific element
print(employeesDictionary.pop("3"))
print(employeesDictionary)


# Removes just the value from key
print(employeesDictionary.popitem())
print(employeesDictionary)

# Update dictionary
print(employeesDictionary.update({'4': "new value"}))
print(employeesDictionary)
