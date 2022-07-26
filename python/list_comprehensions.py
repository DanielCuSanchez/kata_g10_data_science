students = ["Daniel", "David", "Damian", "Denis"]

best_students = []
for s in students:
  if "David" not in s:
    best_students.append(s)

#Creating a list using a list comprehension
list_cpr = [ student for student in students  if "David" not in student ]
print(list_cpr)

print("LIST_COMPREHENSION")
[ print(student) for student in students  if "David" not in student ]