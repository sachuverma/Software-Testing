
# parent class for Error
class Error(BaseException):
	pass

# child class of Error named OutOfRangeError
class OutOfRangeError(Error):
	def __init__(self, message):
		self.message = message

# child class of Error named TicketError		
class TicketError(Error):
	def __init__(self, message):
		self.message = message

# checks if variables are in range
# if variables not in range then OutOfRangeError is raised
def checkRange(membership_id, number):
	if membership_id < 1111111 or membership_id > 9999999:
		raise OutOfRangeError('Membership Id is out of the given range\n')
	if number < 1 or number > 10: 
		raise OutOfRangeError('No. of Tickets Booked is out of range\n')

# checks if the given value is valid
# if not, then Ticket error is raised
def checkName(name):
    if ((name[0]>='a' and name[0]<='z') or (name[0]>='A' and name[0]<='Z')):
        # print(name,'Valid Name')
        return
    else:
        raise TicketError('Invalid name\n')

def checkTicketType(type):
	if type != "E" and type != "B":
		raise TicketError(f'No Such Ticket Type Exists: {type} \n')

def checkMembershipType(type):
	if type != 'P' and type != 'G' and type != 'S':
		raise TicketError(f'No Such Membership Type Exists: {type} \n')


# determines the price		
def calculateCost(membership_id, membership_type, number_of_tickets, name, ticket_type):
    checkName(name)
    checkRange(membership_id, number_of_tickets)
    checkTicketType(ticket_type)
    checkMembershipType(membership_type)

    amount = 0;
    # adding price per ticket of each type of ticket
    if ticket_type == 'B':
      amount = 15000 * number_of_tickets
    elif ticket_type == 'E':
      amount = 7000 * number_of_tickets
      
    if amount > 50000:
      if membership_type == 'P':
        amount -= (amount * 0.1)
      elif membership_type == 'G':
        amount -= (amount * 0.05)
      elif membership_type == 'S':
        amount -= (amount * 0.03)
    
    if amount > 50000:
      if membership_type == 'P':
        amount -= (amount * 0.05)

    return amount


def main():
  print("Enter Ticket Details ")
  while True:
    ans = str(input('Do you want to enter a input (y): '))
    if ans != "y":
      break 

    try:
      name = str(input('Enter name: '))
      membership_id = int(input('Enter membership id: '))
      membership_type = str(input('Enter membership type: '))
      number_ticket = int(input('Enter no. of tickets: '))
      ticket_type = str(input('Enter ticket type: '))
    except ValueError as v:
      print(v + " Raised :Invalid Input Type \n")
      exit(0)

    try:
      checkRange(membership_id, number_ticket)
    except OutOfRangeError as e:
      print("OutOfRangeError: " + e.message)
      # continue

    try:
      checkName(name)
    except TicketError as e:
      print('NameError: ' + e.message)
      # continue

    try:
      checkTicketType(ticket_type)
    except TicketError as e:
      print('TypeError: ' + e.message)

    try:
      checkMembershipType(membership_id)
    except TicketError as e:
      print('TypeError: ' + e.message)
      # continue;

    cost = calculateCost(membership_id, membership_type, number_ticket, name, ticket_type)
    print(f"Ticket Cost:  {cost} \n")


if __name__ == "__main__":
	main()
