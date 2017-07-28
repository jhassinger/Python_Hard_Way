# Copies one file to another via command line
# syntax: python ex17.py from_file to_file

from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
#in_file = open(from_file)
#indata = open(from_file).read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#out_file = open(to_file, 'w')
open(to_file, 'w').write(open(from_file).read())

#print "Alright, all done."

#out_file.close()
#in_file.close()