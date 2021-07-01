# import math

# parent class for Error
class Error(BaseException):
	pass

# child class of Error named OutOfRangeError
class OutOfRangeError(Error):
	def __init__(self, message):
		self.message = message

# child class of Error named ArtError		
class ArtError(Error):
	def __init__(self, message):
		self.message = message

# checks if variables are in range
# if variables not in range then OutOfRangeError is raised
def checkRange(total,amount,time):
	if total<0:
		raise OutOfRangeError('Total paintings sold is out of the given range')
	if amount<100000 or amount>400000:
		raise OutOfRangeError('Amount is out of the given range')
	if time<2 or time>20: 
		raise OutOfRangeError('Time is out of range')

# checks if the given value is valid
# if not, then Art error is raised
def checkName(name):
    if ((name[0]>='a' and name[0]<='z') or (name[0]>='A' and name[0]<='Z')):
        print(name,'Valid Name')
    else:
        raise ArtError('Invalid name')

def checkArtType(type):
	if type!='M' and type!='S' and type!='P':
		raise ArtError('No Such Art Type Exists')

def checkTotal(totalArtists):
    if totalArtists!=10 :
        raise ArtError('Invalid no. of Artists')


# determines the price		
def calculatePrice(total,amount,time,name,type,totalArtists):
    checkRange(total,amount,time)
    checkName(name)
    checkArtType(type)
    checkTotal(totalArtists)
    if type == 'M' :
        if time>5:
            amount = amount + 0.1*amount

    else:
        if total>10:
            amount = amount +0.1*amount
    return amount


def main():
    try:
        print("Enter Art Details : ")
        total = int(input('Enter total paintings:'))
        amount = int(input('Enter amount:'))
        name = str(input('Enter name:'))
        time = int(input('Enter time:'))
        type = str(input('Enter type:'))
        totalArtists = int(input('Enter no. of artists:'))
    except ValueError as v:
        print(v + " Raised :Invalid Input Type.")
        exit(0)
    try:
        checkRange(total,amount,time)
    except OutOfRangeError as e:
        print("OutOfRangeError:" + e.message)
        
    try:
        checkName(name)
    except ArtError as e:
        print('NameError:' + e.message)

    try:
        checkArtType(type)
    except ArtError as e:
        print('TypeError:' + e.message)

    try:
        checkTotal(totalArtists)
    except ArtError as e:
        print('TotalError' + e.message)
        
    price = calculatePrice(total,amount,time,name,type,totalArtists)
    print("Art Price : " + price)

if __name__ == "__main__":
	main()
