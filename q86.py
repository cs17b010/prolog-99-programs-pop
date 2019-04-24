
def checkKey(dict, key): 
	
	if dict.has_key(key): 
		print "Present, value =", dict[key] 
	else: 
		print "Not present"


dict = {'a': 100, 'b':200, 'c':300} 
key = 'b'
checkKey(dict, key) 

key = 'w'
checkKey(dict, key) 
