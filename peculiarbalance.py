# This code takes a decimal number, and converts it twice:
# 1.) decimal > ternary (0, 1, 2's)
# 2.) ternary > balanced ternary (-1, 0, 1) (L, -, R; in this case)
# Balanced ternary tells us exactly which powers of three we 
# need to add/subtract to get two balanced values. 

def answer(x):
    def ternary(n):
    	if n == 0:
    		return 0
    	nums = []
    	while n:
    		n,r = divmod(n,3)
    		nums.append(str(r))
    	return ''.join(nums)
    def btern(n):
    	carry = 0
    	narr = []
    	for i in range(0, len(n)):
    		temp = int(n[i]) + carry
    		carry=0
    		if(temp == 3):
    			narr.append("-")
    			carry = 1
    		elif(temp == 2):
    			narr.append("L")
    			carry = 1
    		elif(temp == 1):
    			narr.append("R")
    			carry = 0
    		else:
    			carry = 0
    			narr.append("-")
    	if(carry == 1):
    		narr.append("R")
    	return narr
    return btern(ternary(x))
print(answer(8))
