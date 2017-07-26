# Assign a formatter string with raw format
formatter = "%r %r %r %r"

# Print some integers
print formatter % (1, 2, 3, 4)

# Print some strings
print formatter % ("one", "two", "three", "four")

# Print some booleans
print formatter % (True, False, False, True)

# Print the formatter string
print formatter % (formatter, formatter, formatter, formatter)

# Print several strings on one line
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)
	