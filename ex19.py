# define a function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# print the first argument
	print "You have %d cheeses!" % cheese_count
	# print the second argument
	print "You have %d boxes of crackers!" % boxes_of_crackers
	# print some other text
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
	
print "We can just give the function numbers directly:"
# call the function by giving argument values directly
cheese_and_crackers(20, 30)


print "OR we can use variables from our script:"
# assign values to two variables
amount_of_cheese = 10
amount_of_crackers = 50

# call function using assigned variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# call function and do sums in the argument
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# call function using assigned variables and sums in the argument
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)