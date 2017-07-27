# Demonstrate how to tab in
tabby_cat = "\tI'm tabbed in."

# New line escape
persian_cat = "I'm split\non a line."

# Backslash escape
backslash_cat = "I'm \\ a \\ cat."

# Multiline string w/ tabs and new line
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

# Print the strings
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# continuously looping
while True:
	for i in ["/","-","|","\\","|"]: # loops through symbols
		print "%s\r" %i, # print string symbol followed by carriage return