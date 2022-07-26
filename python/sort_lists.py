# Sorting strings lists
countries = ["Germany", "Mexico", "Canada", "canada", "puerto rico", "Brazil"]
countries.sort()
countries.sort( key = str.islower, reverse = True)
print(countries)

#Sorting numbers lists
def helper(number):
  return abs(number - 1)

numbers = [33, 44, 11, 2, 0, -344]
numbers.sort( reverse = True )
numbers.sort( key = helper )
print(numbers)
