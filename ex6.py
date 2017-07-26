# Assign string x while formatting integer number
x = "There are %d types of people." % 10

# a string
binary = "binary"

# another string
do_not = "don't"

# Assign string x while formatting strings binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# Print strings x and y
print x
print y

# Print string with strings x and y formatted in
print "I said: %r." % x
print "I also said: '%s'." % y

# Boolean variable
hilarious = False

# Assign string with formatting character in place
joke_evaluation = "Isn't that joke so funny?! %r"

# Print string with formatting 
print joke_evaluation % hilarious

# Assign left and right sides of strings
w = "This is the left side of..."
e = "a string with a right side."

# Print concatenation of strings w and e
print w + e