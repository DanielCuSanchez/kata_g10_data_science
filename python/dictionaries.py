#Syntax
myDictionary = {
  "name" : "Daniel",
  "last_name": "Cu",
  "age": 24,
  "weight": 78.6,
  'city': 'Qro',
  "hobbies": ["running", "playing xbox", "dancing"]
}

print(myDictionary)
# access to a key
print(myDictionary["weight"])
# class
print(type(myDictionary))
# length dictionary
print(len(myDictionary))


# looping a dictionary

# values
for value in myDictionary.values():
  print(value)
# keys
for key in myDictionary.keys():
  print(key)

# keys
for key, value in myDictionary.items():
  print(key, value)

# copying a dictionary
myNewDictionary = myDictionary.copy()

#print(myNewDictionary)

