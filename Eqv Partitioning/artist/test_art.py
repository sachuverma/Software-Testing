import pytest

# importing classes and function which we use in this file
from loan import OutOfRangeError
from loan import ArtError
from loan import calculatePrice

# calculatePrice => total, amount, time, name, type, totalArtists

# check if total<0
def test_invalid_total():
	with pytest.raises(OutOfRangeError):
		calculatePrice(-5, 200000 , 6 , 'abcd' ,'M',10)

# check if amount<100000
def test_invalid_less_amount():
	with pytest.raises(OutOfRangeError):
		calculatePrice(5, 2000 , 6 , 'abcd' ,'M',10)

# check if amount>400000		
def test_invalid_more_amount():
	with pytest.raises(OutOfRangeError):
		calculatePrice(5, 500000 , 6 ,'abcd','M',10)
		

# check if time<2
def test_invalid_less_time():
	with pytest.raises(OutOfRangeError):
		calculatePrice(5, 200000 , 1 , 'abcd' ,'M',10)

# check if time>20		
def test_invalid_more_time():
	with pytest.raises(OutOfRangeError):
		calculatePrice(5, 200000 , 25 , 'abcd' ,'M',10)

# check if name doesnt start with alphabet		
def test_invalid_wrong_name():
	with pytest.raises(ArtError):
		calculatePrice(5, 200000, 10, '1abc' , 'M',10)


# check if type !='M' and !='S' and !='P'	
def test_invalid_wrong_type():
	with pytest.raises(ArtError):
		calculatePrice(5, 200000, 10, 'abcd' , 'Z',10)


# check if no of customers !=10
def test_invalid_wrong_total():
	with pytest.raises(ArtError):
		calculatePrice(5, 200000, 10,'abcd', 'S',9)

# valid class - determines interest of loan	
def test_valid():
	assert calculatePrice(5, 200000, 6,'abcd','M',10) == 220000
