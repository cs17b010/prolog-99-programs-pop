
NA = -1

def moveToEnd(mPlusN, size): 

	i = 0
	j = size - 1
	for i in range(size-1, -1, -1): 
		if (mPlusN[i] != NA): 
	
			mPlusN[j] = mPlusN[i] 
			j-=1


def merge(mPlusN, N, m, n): 

	i = n 
	j = 0 
	k = 0 
	while (k < (m+n)): 
			if ((i < (m+n) and mPlusN[i] <= N[j]) or (j == n)): 
	
			mPlusN[k] = mPlusN[i] 
			k+=1
			i+=1
	
		else: # Otherwise take element from N[] 
		
			mPlusN[k] = N[j] 
			k+=1
			j+=1


def printArray(arr,size): 

	for i in range(size): 
		print(arr[i], " ", end="") 

	print() 

 
mPlusN = [2, 8, NA, NA, NA, 13, NA, 15, 20] 
N = [5, 7, 9, 25] 
n = len(N) 

m = len(mPlusN) - n 

moveToEnd(mPlusN, m+n) 

merge(mPlusN, N, m, n) 


printArray(mPlusN, m+n) 


