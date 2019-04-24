
import collections 

 
Input = [[1, 1, 1, 2], [2, 3, 4], [1, 2, 3], [4, 5, 6]] 

list_search = [2, 3, 4] 

 
flag = 0


for elem in Input: 
	if collections.Counter(elem) == collections.Counter(list_search) : 
		flag = 1
	

if flag == 0: 
	print("False") 
else: 
	print("True") 
