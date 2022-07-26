#Syntax
myTuple = ("Belem", "Paola", "Viviana", "Andres")
myTuple2 = ("Belem", "Paola", "Viviana", "Andres")
#myTuple[0] = "Hannia"


print(myTuple[0])
print(type(myTuple))


#update

#hack to update tupples
aux_list = list(myTuple)

aux_list.append("Juana")

aux_list[1] = "Mariana"

myTuple = tuple(aux_list)


#Joining tupples
join_tupple = myTuple + myTuple2


print(myTuple.count("Juana"))

print(join_tupple)

# This counts how many is for a specific element
print(join_tupple.count("Belem"))
print(join_tupple.index("Paola"))