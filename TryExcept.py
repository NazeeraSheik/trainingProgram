##logical errors in python are
#Index Error,Assertion Error,Attribute Error ,Import Error,Key Error,Name Error,Memory Error,Type Error

#executing try and except with error
try:
	print("excecute some code")
	print(1/0)
except:
	print("if error occures")
finally:
	print("excecute every time")

#the output of the above code is
# excecute some code
# if error occures
# excecute every time
# [Finished in 423ms]




#executing try and except without error
try:
	print("excecute some code")
except:
	print("if error occures")
finally:
	print("excecute every time")

#the output of the above code is
# excecute some code
# excecute every time
# [Finished in 423ms]

#Raising exceptions for a predefined condition 
#When we want to code for the limitation of certain conditions then we can raise an exception. 
# try for unsafe code
try:
	amount = 1999
	if amount < 2999:
		
		# raise the ValueError
		raise ValueError("please add money in your account")
	else:
		print("You are eligible to purchase DSA Self Paced course")
			
# if false then raise the value error
except ValueError as e:
		print(e)

#the output of the above code is
#please add money in your account
#[Finished in 278ms]

#Creating User-defined Exception
#Programmers may name their own exceptions by creating a new exception class. Exceptions need to be derived from the Exception class, either directly or indirectly. Although not mandatory, most of the exceptions are named as names that end in “Error” similar to the naming of the standard exceptions in python.
# A python program to create user-defined exception
 
# class MyError is derived from super class Exception
class MyError(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))
 
try:
    raise(MyError(3*2))
 
# Value of Exception is stored in error
except MyError as error:
    print('A New Exception occured: ',error.value)

