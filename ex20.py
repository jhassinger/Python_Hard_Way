# take in argument from the command line
from sys import argv

# unpack the command line arguments
script, input_file = argv

# define a function to print the whole file
def print_all(f):
	# reads the file and prints
	print f.read()
	
# define a function to rewind the file
def rewind(f):
	# sets file position to the beginning
	f.seek(0)
	
# define a function that prints a specified line of the file
def print_a_line(line_count, f):
	# prints the line number and the line of the file
	print line_count, f.readline()
	
# opens file and assigns it to a variable
current_file = open(input_file)

# print some text
print "First let's print the whole file:\n"

# calls function to print all of current_file
print_all(current_file)

# print some more text
print "Now let's rewind, kind of like a tape."

# calls function to rewind current_file
rewind(current_file)

# again print some text
print "Let's print three lines:"

# assigns variable current_line a value of one
current_line = 1
# calls function to print line 1 of current_file
print_a_line(current_line, current_file)

# adds one to current_line, now value is 2
current_line += 1
# calls function to print line 2 of current_file
print_a_line(current_line, current_file)

# adds one to current_line, now value is 3
current_line += 1
# calls function to print line 3 of current file
print_a_line(current_line, current_file)