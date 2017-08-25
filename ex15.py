# Import argv module for reading in input from command line
from sys import argv

# Specify the first and second command line inputs to be read in
script, filename = argv

# Open the file and assign to txt
txt = open(filename)

# Print the filename
print "Here's your file %r:" % filename

# Print the contents of txt
print txt.read()

# Prompt user to input filename again
print "Type the filename again:"

# Receive input filename from user and assign to file_again
file_again = raw_input("> ")

# Open filename stored in file_again and assign to txt_again
txt_again = open(file_again, 'r+')

# Read and print contents of file
print txt_again.read()


# Take use input to write to file
output = raw_input("Write something to add to the file: ")

# Write to file
txt_again.write(output)

# Rewind to beginning of file
txt_again.seek(0)

# Print contents again
print txt_again.read()

# Close files
txt.close()
txt_again.close()