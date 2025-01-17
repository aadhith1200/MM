import numpy as np

def get_minimum_penalty(x:str, y:str, pxy:int, pgap:int):
	"""
	Function to find out the minimum penalty

	:param x: pattern X
	:param y: pattern Y
	:param pxy: penalty of mis-matching the characters of X and Y
	:param pgap: penalty of a gap between pattern elements
	"""

	# initializing variables
	i = 0
	j = 0
	
	# pattern lengths
	m = len(x)
	n = len(y)
	
	# table for storing optimal substructure answers
	dp = np.zeros([m+1,n+1], dtype=int) #int dp[m+1][n+1] = {0};

	# initialising the table
	dp[0:(m+1),0] = [ i * pgap for i in range(m+1)]
	dp[0,0:(n+1)] = [ i * pgap for i in range(n+1)]

	# calculating the minimum penalty
	i = 1
	while i <= m:
		j = 1
		while j <= n:
			if x[i - 1] == y[j - 1]:
				dp[i][j] = dp[i - 1][j - 1]
			else:
				dp[i][j] = min(dp[i - 1][j - 1] + pxy,
								dp[i - 1][j] + pgap,
								dp[i][j - 1] + pgap)
			j += 1
		i += 1
	
	# Reconstructing the solution
	l = n + m # maximum possible length
	i = m
	j = n
	
	xpos = l
	ypos = l

	# Final answers for the respective strings
	xans = np.zeros(l+1, dtype=int)
	yans = np.zeros(l+1, dtype=int)
	

	while not (i == 0 or j == 0):
		#print(f"i: {i}, j: {j}")
		if x[i - 1] == y[j - 1]:	
			xans[xpos] = ord(x[i - 1])
			yans[ypos] = ord(y[j - 1])
			xpos -= 1
			ypos -= 1
			i -= 1
			j -= 1
		elif (dp[i - 1][j - 1] + pxy) == dp[i][j]:
		
			xans[xpos] = ord(x[i - 1])
			yans[ypos] = ord(y[j - 1])
			xpos -= 1
			ypos -= 1
			i -= 1
			j -= 1
		
		elif (dp[i - 1][j] + pgap) == dp[i][j]:
			xans[xpos] = ord(x[i - 1])
			yans[ypos] = ord('_')
			xpos -= 1
			ypos -= 1
			i -= 1
		
		elif (dp[i][j - 1] + pgap) == dp[i][j]:	
			xans[xpos] = ord('_')
			yans[ypos] = ord(y[j - 1])
			xpos -= 1
			ypos -= 1
			j -= 1
		

	while xpos > 0:
		if i > 0:
			i -= 1
			xans[xpos] = ord(x[i])
			xpos -= 1
		else:
			xans[xpos] = ord('_')
			xpos -= 1
	
	while ypos > 0:
		if j > 0:
			j -= 1
			yans[ypos] = ord(y[j])
			ypos -= 1
		else:
			yans[ypos] = ord('_')
			ypos -= 1

	# Since we have assumed the answer to be n+m long,
	# we need to remove the extra gaps in the starting
	# id represents the index from which the arrays
	# xans, yans are useful
	id = 1
	i = l
	while i >= 1:
		if (chr(yans[i]) == '_') and chr(xans[i]) == '_':
			id = i + 1
			break
		
		i -= 1

	# Printing the final answer
	print(f"Minimum Penalty in aligning the genes = {dp[m][n]}")
	print("The aligned genes are:")
	# X
	i = id
	x_seq = ""
	while i <= l:
		x_seq += chr(xans[i])
		i += 1
	print(f"X seq: {x_seq}")

	# Y
	i = id
	y_seq = ""
	while i <= l:
		y_seq += chr(yans[i])
		i += 1
	print(f"Y seq: {y_seq}")

def test_get_minimum_penalty():
	"""
	Test the get_minimum_penalty function
	"""
	# input strings
	gene1 = "gttgctccctaaactaagtgtgctggagcgccggggggaggatgtagattggaagacggccgttgtatagcctcgtaagttgctcactggctagctcccc".upper()
	gene2 = "caggttaagctgaagggcaaaatgtgtgatctggatacctatatctatagcaacggggtgccgaggcatactgggcttgatcaggtcccatcctatgtga".upper()
	
	# initialising penalties of different types
	mismatch_penalty = 3
	gap_penalty = 2

	# calling the function to calculate the result
	get_minimum_penalty(gene1, gene2, mismatch_penalty, gap_penalty)

test_get_minimum_penalty()

# This code is contributed by wilderchirstopher.
