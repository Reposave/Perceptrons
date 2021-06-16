from topology import topology

if __name__ == '__main__':
	XOR = topology(0.95)
	XOR.train(-1,False,True) #set to -1 to train until finished.
	
	print("Constructing Network...")
	print("Done!");
	
	num = input ("Please enter two inputs: \n")
	
	while(num!="exit"):
		inputs = num.split()
		print(inputs)
		a = eval(inputs[0])
		b = eval(inputs[1])
		
		result = XOR.XORGate([a,b])
		print("XOR Gate: "+str(result))
		num = input ("Please enter two inputs: \n")
		
	print("Exiting...")
