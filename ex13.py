from sys import argv

#script, first, second, third = argv
#script, first, second = argv
script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

first = raw_input("What is your favorite food? ")
second = raw_input("How about your second favorite? ")
third = raw_input("Third? ")
fourth = raw_input("Fourth? ")

print "Your favorite foods are %s, %s, %s, and %s." %(
	first, second, third, fourth)