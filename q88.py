
Input = [[1, 1, 1, 2], [2, 3, 4], [1, 2, 3], [4, 5, 6]] 


list_search = [4, 5, 6] 

 
if any(list == list_search for list in Input): 
	print("True") 
else: 
	print("False") 
	
