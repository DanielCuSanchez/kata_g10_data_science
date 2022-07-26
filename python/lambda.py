# basic syntax lambda
sum = lambda number1, number2 : number1 + number2
print(sum(10,20)) #calculating the result in the second function



# lambda in highOrderFunction
def highOrderLambda(n1): #this is the first function
  return lambda n2: n1+n2 #this is another function

internFunction = highOrderLambda(10) #another function

print(internFunction(30)) #calculating the result in the second function