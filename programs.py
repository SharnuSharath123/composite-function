# Python implementation 
# to demonstrate working 
# of Cassini’s Identity 

# Returns (-1)^n 
def cassini(n): 

    return -1 if (n & 1) else 1

# Driver program 

n = 5
print(cassini(n)) 
	
# This code is contributed 
# by Anant Agarwal. 



# Python3 code to print Hosoya's
# triangle of height n.

def Hosoya( n , m ):

	# Base case
	if ((n == 0 and m == 0) or
		(n == 1 and m == 0) or
		(n == 1 and m == 1) or
		(n == 2 and m == 1)):
				return 1
	
	# Recursive step
	if n > m:
		return Hosoya(n - 1, m) 
		+ Hosoya(n - 2, m)

	elif m == n:
		return Hosoya(n - 1, m - 1) 
		+ Hosoya(n - 2, m - 2)

	else:
		return 0
		
# Print the Hosoya triangle of height n.
def printHosoya( n ):
	for i in range(n):
		for j in range(i + 1):
			print(Hosoya(i, j) , end = " ")
		print("\n", end = "")
		
# Driven Code
n = 5
printHosoya(n)

# This code is contributed by Sharad_Bhardwaj




# Python3 Program to print 
# Hosoya's triangle of height n.
N = 5

# Print the Hosoya triangle 
# of height n.
def printHosoya(n):
	dp = [[0 for i in range(N)] 
			for i in range(N)]
			
	# base case.
	dp[0][0] = dp[1][0] = dp[1][1] = 1
	
	# For each row.
	for i in range(2, n):
		
		# for each column
		for j in range(n):
			
			# recursive steps.
			if (i > j):
				dp[i][j] = (dp[i - 1][j] +
							dp[i - 2][j])
			else:
				dp[i][j] = (dp[i - 1][j - 1] +
							dp[i - 2][j - 2])
							
	# printing the solution 
	for i in range(n):
		for j in range(i + 1):
			print(dp[i][j], end = ' ')
		print()

# Driver Code
n = 5
printHosoya(n)

# This code is contributed 
# by sahilshelangia




# Python3 implementation of the approach 
from math import *

# Function to return the previous 
# fibonacci number 
def previousFibonacci(n): 
	a = n/((1 + sqrt(5))/2.0)
	return round(a) 

# Driver code 
n = 8
print(previousFibonacci(n)) 





# Python3 code to find minimum number 
# of Fibonacci terms that sum to K. 

# Function to calculate Fibonacci Terms 
def calcFiboTerms(fiboTerms, K): 

	i = 3
	fiboTerms.append(0) 
	fiboTerms.append(1) 
	fiboTerms.append(1) 
	
	# Calculate all Fibonacci terms 
	# which are less than or equal to K. 
	while True: 
		nextTerm = (fiboTerms[i - 1] +
					fiboTerms[i - 2])

		# If next term is greater than K 
		# do not push it in vector and return. 
		if nextTerm > K:
			return

		fiboTerms.append(nextTerm) 
		i += 1
	
# Function to find the minimum number of 
# Fibonacci terms having sum equal to K. 
def findMinTerms(K): 

	# Vector to store Fibonacci terms. 
	fiboTerms = [] 
	calcFiboTerms(fiboTerms, K) 

	count, j = 0, len(fiboTerms) - 1

	# Subtract Fibonacci terms from 
	# sum K until sum > 0. 
	while K > 0:
		
		# Divide sum K by j-th Fibonacci 
		# term to find how many terms it 
		# contribute in sum. 
		count += K // fiboTerms[j] 
		K %= fiboTerms[j] 

		j -= 1
	
	return count 

# Driver code 
if __name__ == "__main__": 

	K = 17
	print(findMinTerms(K)) 

# This code is contributed
# by Rituraj Jain




# Python3 implementation of the approach 

# Function to return the nth 
# Fibonacci number 
def fib(n): 
	phi = ((1 + (5 ** (1 / 2))) / 2); 
	return round((phi ** n) / (5 ** (1 / 2))); 

# Function to return the required sum 
def calculateSum(l, r): 
	
	# To store the sum 
	sum = 0; 

	# Calculate the sum 
	for i in range(l, r + 1): 
		sum += fib(i); 

	return sum; 

# Driver Code 
if __name__ == '__main__': 
	l, r = 4, 8; 
	print(calculateSum(l, r)); 

# This code contributed by Rajput-Ji 





# Python3 program to Find the sum of 
# first N odd Fibonacci numbers 
mod = 1000000007 ;

# Function to calculate sum of 
# first N odd Fibonacci numbers 
def sumOddFibonacci(n): 

	Sum=[0]*(n + 1); 

	# base values 
	Sum[0] = 0; 
	Sum[1] = 1; 
	Sum[2] = 2; 
	Sum[3] = 5; 
	Sum[4] = 10; 
	Sum[5] = 23; 

	for i in range(6,n+1): 
		Sum[i] = ((Sum[i - 1] +
					(4 * Sum[i - 2]) % mod -
					(4 * Sum[i - 3]) % mod +
					mod) % mod + (Sum[i - 4] -
					Sum[i - 5] + mod) % mod) % mod; 

	return Sum[n]; 

# Driver code 
n = 6; 
print(sumOddFibonacci(n)); 

# This code is contributed by mits


