import pytest

# importing classes and function which we use in this file
from errors import OutOfRangeError
from errors import TypeError
from houses import calculatePrice


# calculatePrice => category, code, type, area, place

# category is not valid
def test_category_invalid():
	with pytest.raises(TypeError):
		calculatePrice("industrial", 12345, "plotted", 600, "N")

# property code less than 11111
def test_property_code_less():
	with pytest.raises(OutOfRangeError):
		calculatePrice("commercial", 123, "plotted", 600, "S")

# property code greater than 99999
def test_property_code_greater():
	with pytest.raises(OutOfRangeError):
		calculatePrice("commercial", 1234567890, "plotted", 600, "E")

# property type not valid
def test_property_type_invalid():
	with pytest.raises(TypeError):
		calculatePrice("commercial", 12345, "flats", 600, "W")

# area less than 500
def test_area_less():
	with pytest.raises(OutOfRangeError):
		calculatePrice("commercial", 12345, "plotted", 100, "N")

# area greater than 5000
def test_area_more():
	with pytest.raises(OutOfRangeError):
		calculatePrice("commercial", 12345, "plotted", 6000, "S")

# place not valid
def test_place_invalid():
	with pytest.raises(TypeError):
		calculatePrice("commercial", 12345, "plotted", 600, "NW")

# commercial can't we apartment
def test_commercial_aparment():
  with pytest.raises(TypeError):
    calculatePrice("commercial", 12345, "apartment", 600, "N")

# valid class - determines interest of loan	
def test_valid():
	assert calculatePrice("commercial", 12345, "plotted", 600, "N") == 5024881.0
