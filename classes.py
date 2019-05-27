class MyClass:
	f_name = "  rajender"
	l_name = "dandyal"

	def full_name(self):
		return self.f_name + " " + self.l_name


raj = MyClass()

print(raj.f_name, raj.l_name, raj.full_name())


# Class => Library
# layers of abstraction => display available books, to lend a book, to add a book

# Class => Customer
# Layers of abstraction => request for a book, return a book
class Library:
	def __init__(self, listOfBooks):
		self.availableBooks = listOfBooks

	def displayAvailableBooks(self):
		print()
		print("Available Books: ")
		for book in self.availableBooks:
			print(book)

	def lendBook(self, requestedBook):
		if requestedBook in self.availableBooks:
			self.availableBooks.remove(requestedBook)
			print(f"You have borrowed: {requestedBook}")

	def addBook(self, returnedBook):
		self.availableBooks.append(returnedBook)
		print(f"You have returned:{returnedBook}")


class Customer:
	def requestBook(self):
		print("Enter the name of a book you would like to borrow: ")
		self.book = input()
		return self.book

	def returnBook(self):
		print("Enter the name of book you want to return: ")
		self.book = input()
		return self.book


library = Library(['Think and Grow Rich', "Rich Dad & Poor Dad"])
customer = Customer()


#
# while True:
#
# 	print("Enter 1 to display the available books")
# 	print("Enter 2 to request for a book")
# 	print("Enter 3 to return a book")
# 	print("Enter 4 to exit")
# 	userChoice = int(input())
#
# 	if userChoice is 1:
# 		library.displayAvailableBooks()
# 	elif userChoice is 2:
# 		requestedBook = customer.requestBook()
# 		library.lendBook(requestedBook)
# 	elif userChoice is 3:
# 		returnedBook = customer.returnBook()
# 		library.addBook(returnedBook)
# 	elif userChoice is 4:
# 		quit()

# inheritance
class Apple:
	manufacturer = "Apple Inc."
	contactWebsite = "www.apple.com/contact"

	def contactDetails(self):
		print("To contact us, log on to ", self.contactWebsite)


class Os:
	multiTasking = True


# multiple inheritance
class MacBook(Apple, Os):
	def __init__(self):
		self.yearOfManufacture = 2017

	def manufactureDetails(self):
		print(f"This MacBook was manufactured in the year {self.yearOfManufacture} by {self.manufacturer}")

	def isMultiTasking(self):
		print(f"Is this Macbook multitasking: {self.multiTasking}")


macBook = MacBook()
macBook.manufactureDetails()
macBook.contactDetails()
macBook.isMultiTasking()

# python also dosent have public protected private keywords
# so as a good developers practice .. these naming syntax are considered by all developers,
# to think methods as public, private, protected
# Public => methodName
# Protected => _methodName -- use in class and its derived class/inheriting class
# Private => __methodName -- use only in class itself -- not even by inheriting class
# static => @staticMethod -- use only in class itself -- inheriting class can also use, --
# but instance of class will not have access to static methods
