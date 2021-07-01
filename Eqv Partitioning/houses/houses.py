# import math
# error classes


from errors import OutOfRangeError
from errors import TypeError

# checks if variables are in range
# if variables not in range then OutOfRangeError is raised
def checkCodeRange(code):
	if code < 11111 or code > 99999:
		raise OutOfRangeError('Code is out of the given range')

def checkAreaRange(area):  
	if area < 500 or area > 5000: 
		raise OutOfRangeError('Area is out of range')

# check if types are correct for all of them
# if they are not valid then return TypeError
def checkCategory(category):
  if category != "commercial" and category != "residential":
    raise TypeError('Category is not valid')

def checkType(type):
  if type != "plotted" and type != "independent" and type != "apartment":
    raise TypeError('Property type not valid')

def checkPlace(place):
  if place != "N" and place != "S" and place != "E" and place != "W":
    raise TypeError('Place is not valid')

def checkCategoryType(category, type):
  if type == "apartment" and category == "commercial":
    raise TypeError("Commercial can't be apartment is not valid")


# determines the price		
def calculatePrice(category, code, type, area, place):
  checkCodeRange(code)
  checkAreaRange(area)
  checkCategory(category)
  checkType(type)
  checkPlace(place)
  checkCategoryType(category, type)

  # price is calculates as 7000 * area
  price = area * 7000
  
  # id commercial, price is multiplied by 1.2 and rebate by 3%
  if category == "commercial":
    price = price * 1.2
    price = price - (price * 0.003)

  # else residential has rebate of 5%
  elif category == "residential":
    price = price - (price * 0.005)
  
  return price


def main():
  count = 100
  print("Enter House Details")

  while count > 0:
    count = count - 1;
    try:
      category = str(input('Enter category: '))
      code = int(input('Enter property code: '))
      type = str(input('Enter property type: '))
      area = float(input('Enter property area: '))
      place = str(input('Enter Place (N,S,E,W): '))
    except ValueError as v:
      print(v + " Raised: Invalid Input Type")
      exit(0)

    try:
      checkCodeRange(code)
    except OutOfRangeError as e:
      print("OutOfRangeError: " + e.message)

    try:
      checkAreaRange(area)
    except OutOfRangeError as e:
      print("OutOfRangeError: " + e.message)
        
    try:
      checkCategory(category)
    except TypeError as e:
      print("TypeError: " + e.message)

    try:
      checkType(type)
    except TypeError as e:
      print("TypeError: " + e.message)

    try:
      checkPlace(place)
    except TypeError as e:
      print("TypeError: " + e.message)
        
    try:
      checkCategoryType(category, type)
    except TypeError as e:
      print("TypeError: " + e.message)

    price = calculatePrice(category, code, type, area, place)
    print(f"House Price:  {price} \n" )

if __name__ == "__main__":
	main()
