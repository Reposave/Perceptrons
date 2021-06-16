from topology import topology

if __name__ == '__main__':
	gateTrainAccuracy = 0.96
	
	XOR = topology(gateTrainAccuracy)
	
	verbose = False	#Prints Perceptron training information.
	seeGates = False #Set to True to see each gate's output.
	generateSets = True	#Generate training and validation examples.
	num_of_training_sessions = -1  #set to -1 to train until accuracy reached.
	XOR.train(num_of_training_sessions,verbose,generateSets)
	
	print("Constructing Network...")
	print("Done!");
	
	num = input ("Please enter two inputs: \n")
	
	while(num!="exit"):
		inputs = num.split()
		print(inputs)
		a = eval(inputs[0])
		b = eval(inputs[1])
		
		result = XOR.XORGate([a,b],seeGates)
		print("XOR Gate: "+str(result))
		num = input ("Please enter two inputs: \n")
		
	print("Exiting...")
