name = 'Julian E. Hassinger'
age = 25 # soon to be 26
height = 72 # inches
weight = 212 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s." % teeth

# apparently this line is tricky
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
	
# testing %r
print "Name: %r, Age: %r" % (name, age)

# converting height and weight to metric
height_cm = height * 2.54
weight_kg = weight * 0.453592
print "He's %0.1f centimeters tall." % height_cm
print "He's %0.1f kilograms heavy." % weight_kg
 