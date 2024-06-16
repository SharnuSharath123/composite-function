# Python3 code to implement iterative Binary
# Search.


# It returns location of x in given array arr
def binarySearch(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")



# Python3 Program for recursive binary search.


# Returns index of x in arr if present, else -1
def binarySearch(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)

    # Element is not present in the array
    else:
        return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")



# Python3 implementation of the approach
# Function to search key in the given array


def sentinelSearch(arr, n, key):

	# Last element of the array
	last = arr[n - 1]

	# Element to be searched is
	# placed at the last index
	arr[n - 1] = key
	i = 0

	while (arr[i] != key):
		i += 1

	# Put the last element back
	arr[n - 1] = last

	if ((i < n - 1) or (arr[n - 1] == key)):
		print(key, "is present at index", i)
	else:
		print("Element Not found")


# Driver code
arr = [10, 20, 180, 30, 60, 50, 110, 100, 70]
n = len(arr)
key = 180

sentinelSearch(arr, n, key)

# This code is contributed by divyamohan123, Mandeep Dalavi




def sentinelLinearSearch(array, key):
	last = array[len(array) - 1]
	array[len(array) - 1] = key
	i = 0
	while array[i] != key:
		i += 1
	array[len(array) - 1] = last
	if i < len(array) - 1 or last == key:
		return i
	else:
		return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
key = 5
index = sentinelLinearSearch(array, key)
if index == -1:
	print(f"{key} is not found in the array: {array}")
else:
	print(f"{key} is found at index {index} in the array: {array}")



# Python 3 implementation of 
# above approach

# Function to show the working
# of Meta binary search
import math
def bsearch(A, key_to_search):

	n = len(A)
	# Set number of bits to represent
	lg = int(math.log2(n-1)) + 1;

	# largest array index
	#while ((1 << lg) < n - 1):
		#lg += 1

	pos = 0
	for i in range(lg - 1, -1, -1) :
		if (A[pos] == key_to_search):
			return pos

		# Incrementally construct the
		# index of the target value
		new_pos = pos | (1 << i)

		# find the element in one
		# direction and update position
		if ((new_pos < n) and
			(A[new_pos] <= key_to_search)):
			pos = new_pos

	# if element found return
	# pos otherwise -1
	return (pos if(A[pos] == key_to_search) else -1)

# Driver code
if __name__ == "__main__":

	A = [ -2, 10, 100, 250, 32315 ]
	print( bsearch(A, 10))

# This implementation was improved by Tanin

# This code is contributed
# by ChitraNayal




# Python3 program to illustrate
# recursive approach to ternary search
import math as mt

# Function to perform Ternary Search
def ternarySearch(l, r, key, ar):

    if (r >= l):

        # Find the mid1 and mid2
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3

        # Check if key is present at any mid
        if (ar[mid1] == key): 
            return mid1
        
        if (ar[mid2] == key): 
            return mid2
        
        # Since key is not present at mid,
        # check in which region it is present
        # then repeat the Search operation
        # in that region
        if (key < ar[mid1]): 

            # The key lies in between l and mid1
            return ternarySearch(l, mid1 - 1, key, ar)
        
        elif (key > ar[mid2]): 

            # The key lies in between mid2 and r
            return ternarySearch(mid2 + 1, r, key, ar)
        
        else: 

            # The key lies in between mid1 and mid2
            return ternarySearch(mid1 + 1, 
                                 mid2 - 1, key, ar)
        
    # Key not found
    return -1

# Driver code
l, r, p = 0, 9, 5

# Get the array
# Sort the array if not sorted
ar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Starting index
l = 0

# end element index
r = 9

# Checking for 5

# Key to be searched in the array
key = 5

# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)

# Checking for 50

# Key to be searched in the array
key = 50

# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)

# This code is contributed by 
# Mohit kumar 29



# Python 3 program to illustrate iterative
# approach to ternary search

# Function to perform Ternary Search
def ternarySearch(l, r, key, ar):
    while r >= l:
        
        # Find mid1 and mid2
        mid1 = l + (r-l) // 3
        mid2 = r - (r-l) // 3

        # Check if key is at any mid
        if key == ar[mid1]:
            return mid1
        if key == ar[mid2]:
            return mid2

        # Since key is not present at mid, 
        # Check in which region it is present
        # Then repeat the search operation in that region
        if key < ar[mid1]:
            # key lies between l and mid1
            r = mid1 - 1
        elif key > ar[mid2]:
            # key lies between mid2 and r
            l = mid2 + 1
        else:
            # key lies between mid1 and mid2
            l = mid1 + 1
            r = mid2 - 1

    # key not found
    return -1

# Driver code

# Get the list
# Sort the list if not sorted
ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Starting index
l = 0

# end element index
r = 9

# Checking for 5
# Key to be searched in the list
key = 5

# Search the key using ternary search
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)

# Checking for 50
# Key to be searched in the list
key = 50

# Search the key using ternary search
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)

# This code has been contributed by Sujal Motagi




# Python3 code to implement Jump Search
import math

def jumpSearch( arr , x , n ):
	
	# Finding block size to be jumped
	step = math.sqrt(n)
	
	# Finding the block where element is
	# present (if it is present)
	prev = 0
	while arr[int(min(step, n)-1)] < x:
		prev = step
		step += math.sqrt(n)
		if prev >= n:
			return -1
	
	# Doing a linear search for x in 
	# block beginning with prev.
	while arr[int(prev)] < x:
		prev += 1
		
		# If we reached next block or end 
		# of array, element is not present.
		if prev == min(step, n):
			return -1
	
	# If element is found
	if arr[int(prev)] == x:
		return prev
	
	return -1

# Driver code to test function
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
	34, 55, 89, 144, 233, 377, 610 ]
x = 55
n = len(arr)

# Find the index of 'x' using Jump Search
index = jumpSearch(arr, x, n)

# Print the index where 'x' is located
print("Number" , x, "is at index" ,"%.0f"%index)

# This code is contributed by "Sharad_Bhardwaj".




# Python3 program to implement
# interpolation search
# with recursion

# If x is present in arr[0..n-1], then
# returns index of it, else returns -1.


def interpolationSearch(arr, lo, hi, x):

	# Since array is sorted, an element present
	# in array must be in range defined by corner
	if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

		# Probing the position with keeping
		# uniform distribution in mind.
		pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
					(x - arr[lo]))

		# Condition of target found
		if arr[pos] == x:
			return pos

		# If x is larger, x is in right subarray
		if arr[pos] < x:
			return interpolationSearch(arr, pos + 1,
									hi, x)

		# If x is smaller, x is in left subarray
		if arr[pos] > x:
			return interpolationSearch(arr, lo,
									pos - 1, x)
	return -1

# Driver code


# Array of items in which
# search will be conducted
arr = [10, 12, 13, 16, 18, 19, 20,
	21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)

# Element to be searched
x = 18
index = interpolationSearch(arr, 0, n - 1, x)

if index != -1:
	print("Element found at index", index)
else:
	print("Element not found")

# This code is contributed by Hardik Jain




# Python equivalent of above C++ code 
# Python program to implement interpolation search by using iteration approach
def interpolationSearch(arr, n, x): 

	# Find indexes of two corners 
	low = 0
	high = (n - 1) 

	# Since array is sorted, an element present 
	# in array must be in range defined by corner 
	while low <= high and x >= arr[low] and x <= arr[high]: 
		if low == high: 
			if arr[low] == x: 
				return low; 
			return -1; 

		# Probing the position with keeping 
		# uniform distribution in mind. 
		pos = int(low + (((float(high - low)/( arr[high] - arr[low])) * (x - arr[low])))) 

		# Condition of target found 
		if arr[pos] == x: 
			return pos 

		# If x is larger, x is in upper part 
		if arr[pos] < x: 
			low = pos + 1; 

		# If x is smaller, x is in lower part 
		else: 
			high = pos - 1; 
	
	return -1

# Main function
if __name__ == "__main__":
	# Array of items on whighch search will 
	# be conducted.
	arr = [10, 12, 13, 16, 18, 19, 20, 21,
		22, 23, 24, 33, 35, 42, 47]
	n = len(arr) 

	x = 18 # Element to be searched
	index = interpolationSearch(arr, n, x) 

	# If element was found
	if index != -1: 
		print ("Element found at index",index)
	else: 
		print ("Element not found")




# Python program to find an element x
# in a sorted array using Exponential Search

# A recursive binary search function returns 
# location of x in given array arr[l..r] is 
# present, otherwise -1
def binarySearch( arr, l, r, x):
	if r >= l:
		mid = l + ( r-l ) // 2
		
		# If the element is present at 
		# the middle itself
		if arr[mid] == x:
			return mid
		
		# If the element is smaller than mid, 
		# then it can only be present in the 
		# left subarray
		if arr[mid] > x:
			return binarySearch(arr, l, 
								mid - 1, x)
		
		# Else he element can only be
		# present in the right
		return binarySearch(arr, mid + 1, r, x)
		
	# We reach here if the element is not present
	return -1

# Returns the position of first
# occurrence of x in array
def exponentialSearch(arr, n, x):
	# IF x is present at first 
	# location itself
	if arr[0] == x:
		return 0
		
	# Find range for binary search 
	# j by repeated doubling
	i = 1
	while i < n and arr[i] <= x:
		i = i * 2
	
	# Call binary search for the found range
	return binarySearch( arr, i // 2, 
						min(i, n-1), x)
	

# Driver Code
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exponentialSearch(arr, n, x)
if result == -1:
	print ("Element not found in the array")
else:
	print ("Element is present at index %d" %(result))

# This code is contributed by Harshit Agrawal



def exponential_search(arr, x):
	n = len(arr)
	if n == 0:
		return -1

	# Find range for binary search by repeatedly doubling i
	i = 1
	while i < n and arr[i] < x:
		i *= 2

	# Perform binary search on the range [i/2, min(i, n-1)]
	left = i // 2
	right = min(i, n-1)

	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			left = mid + 1
		else:
			right = mid - 1

	return -1

	

# Driver Code
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exponential_search(arr, x)
if result == -1:
	print ("Element not found in the array")
else:
	print ("Element is present at index %d" %(result))

# This code is contributed by Ajay singh




# Python3 program for Fibonacci search. 
from bisect import bisect_left 

# Returns index of x if present, else 
# returns -1 


def fibMonaccianSearch(arr, x, n): 

	# Initialize fibonacci numbers 
	fibMMm2 = 0 # (m-2)'th Fibonacci No. 
	fibMMm1 = 1 # (m-1)'th Fibonacci No. 
	fibM = fibMMm2 + fibMMm1 # m'th Fibonacci 

	# fibM is going to store the smallest 
	# Fibonacci Number greater than or equal to n 
	while (fibM < n): 
		fibMMm2 = fibMMm1 
		fibMMm1 = fibM 
		fibM = fibMMm2 + fibMMm1 

	# Marks the eliminated range from front 
	offset = -1

	# while there are elements to be inspected. 
	# Note that we compare arr[fibMm2] with x. 
	# When fibM becomes 1, fibMm2 becomes 0 
	while (fibM > 1): 

		# Check if fibMm2 is a valid location 
		i = min(offset+fibMMm2, n-1) 

		# If x is greater than the value at 
		# index fibMm2, cut the subarray array 
		# from offset to i 
		if (arr[i] < x): 
			fibM = fibMMm1 
			fibMMm1 = fibMMm2 
			fibMMm2 = fibM - fibMMm1 
			offset = i 

		# If x is less than the value at 
		# index fibMm2, cut the subarray 
		# after i+1 
		elif (arr[i] > x): 
			fibM = fibMMm2 
			fibMMm1 = fibMMm1 - fibMMm2 
			fibMMm2 = fibM - fibMMm1 

		# element found. return index 
		else: 
			return i 

	# comparing the last element with x */ 
	if(fibMMm1 and arr[n-1] == x): 
		return n-1

	# element not found. return -1 
	return -1


# Driver Code 
arr = [10, 22, 35, 40, 45, 50, 
	80, 82, 85, 90, 100,235] 
n = len(arr) 
x = 235
ind = fibMonaccianSearch(arr, x, n) 
if ind>=0: 
  print("Found at index:",ind) 
else: 
  print(x,"isn't present in the array"); 

# This code is contributed by rishabh_jain 



def fibonacci_search(arr, x): 
	n = len(arr) 
	if n == 0: 
		return -1

	# Initialize Fibonacci numbers 
	fib1, fib2 = 0, 1
	fib3 = fib1 + fib2 

	# Find the smallest Fibonacci number greater than or equal to n 
	while fib3 < n: 
		fib1, fib2 = fib2, fib3 
		fib3 = fib1 + fib2 

	# Initialize variables for the current and previous split points 
	offset = -1
	while fib3 > 1: 
		i = min(offset + fib2, n-1) 

		# If x is greater than the value at index i, move the split point to the right 
		if arr[i] < x: 
			fib3 = fib2 
			fib2 = fib1 
			fib1 = fib3 - fib2 
			offset = i 

		# If x is less than the value at index i, move the split point to the left 
		elif arr[i] > x: 
			fib3 = fib1 
			fib2 = fib2 - fib1 
			fib1 = fib3 - fib2 

		# If x is equal to the value at index i, return the index 
		else: 
			return i 

	# If x is not found in the array, return -1 
	if fib2 == 1 and arr[offset+1] == x: 
		return offset + 1
	else: 
		return -1




# Driver Code 
arr = [10, 22, 35, 40, 45, 50, 
	80, 82, 85, 90, 100,235] 
n = len(arr) 
x = 235
ind = fibonacci_search(arr, x) 
if ind>=0: 
	print("Found at index:",ind) 
else: 
	print(x,"isn't present in the array"); 

# This code is contributed by ajay singh 








