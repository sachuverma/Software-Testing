import pytest

# importing classes and function which we use in this file
from tickets import OutOfRangeError
from tickets import TicketError
from tickets import calculateCost

# membership_id, membership_type, number_of_tickets, name, ticket_type

# check invalid name
def test_invalid_name():
	with pytest.raises(TicketError):
		calculateCost(1234567, 'P' , 5 , '1abcd' ,'E')

# check if member_id < 1111111
def test_invalid_less_member_id():
	with pytest.raises(OutOfRangeError):
		calculateCost(123456, 'P' , 5 , 'abcd' ,'E')

# check if member_id > 9999999
def test_invalid_more_member_id():
	with pytest.raises(OutOfRangeError):
		calculateCost(12345678, 'P' , 3 , 'abcde' ,'B')

# check invalid memebership type
def test_invalid_membership_type():
	with pytest.raises(TicketError):
		calculateCost(1234567, 'A' , 5 , 'abcd' ,'E')

# check invalid number of ticket < 1
def test_invalid_number_of_less_tickets():
	with pytest.raises(OutOfRangeError):
		calculateCost(1234567, 'G' , 0 , 'abcd' ,'E')

# check invalid number of ticket > 10
def test_invalid_number_of_more_tickets():
	with pytest.raises(OutOfRangeError):
		calculateCost(1234567, 'G' , 50 , 'abcd' ,'E')

# check invalid ticeket type
def test_invalid_ticket_type():
	with pytest.raises(TicketError):
		calculateCost(1234567, 'S' , 5 , 'abcd' ,'A')

# valid class - determines interest of loan	
def test_valid():
	assert calculateCost(1234567, 'S' , 9 , 'abcd' ,'B') == 130950
