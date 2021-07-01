# parent class for Error
class Error(BaseException):
	pass

# child class of Error named OutOfRangeError
class OutOfRangeError(Error):
	def __init__(self, message):
		self.message = message

# child class of Error named ArtError		
class TypeError(Error):
	def __init__(self, message):
		self.message = message
