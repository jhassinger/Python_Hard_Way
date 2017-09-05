def numList(num, increment):

	i = 0
	numbers = []

	while i < num:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom i is % d" % i
	

	print "The numbers: "

	for num in numbers:
		print num
		
	j = 0
	numbers2 = []
		
	for j in range(0, num, increment):
		print "At the top j is %d" % j
		numbers2.append(j)
	
		j = j + increment
		print "Numbers now: ", numbers2
		print "At the bottom j is % d" % j
	

	print "The numbers: "

	for num in numbers:
		print num
	