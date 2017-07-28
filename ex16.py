# import argv
from sys import argv

# assign arguments to variables script and filename
script, filename = argv

# printing instructions to user
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# wait for user to hit enter or escape
raw_input("?")

# open the file in write mode
print "Opening the file..."
target = open(filename, 'w')

# truncate the file to erase it
#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

# read in 3 new lines from the user
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# write the read in lines to the file
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# close the file
print "And finally, we close it."
target.close()