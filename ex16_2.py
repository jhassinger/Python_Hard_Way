from sys import argv

script, filename = argv

print "Opening file %r..." % filename
txt = open(filename)

print "Here are the contents of %r:" % filename
print txt.read()

print "Closing file %r..." % filename
txt.close()