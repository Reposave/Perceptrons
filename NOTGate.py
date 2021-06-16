import random
from Perceptron import Perceptron

class NOTGate:
	def __init__(self,accuracy):
		self.acc = accuracy
		self.NOT = Perceptron(1, bias=0.5)
		return None
	
	#Trains the perceptron.
	def train(self,sessions,Generate: bool = True,verbose: bool =False): #Set default to 50.
		generate_training_set = Generate
		num_train = 1000
		generate_validation_set = Generate
		num_valid = 1000

		training_examples = [[1.0],
							[1.0],
							[0.0],
							[0.0]]

		training_labels = [0.0, 0.0, 1.0, 1.0]

		validate_examples = training_examples
		validate_labels = training_labels

		if generate_training_set:

			training_examples = []
			training_labels = []

			for i in range(num_train):
				training_examples.append([random.uniform(0,1)])
				# We want our perceptron to be noise tolerant, so we label all examples where x1 and x2 > 0.8 as 1.0
				training_labels.append(0.0 if (training_examples[i][0] > 0.75) else 1.0)

		if generate_validation_set:

			validate_examples = []
			validate_labels = []

			for i in range(num_train):
				validate_examples.append([random.uniform(0,1)])
				validate_labels.append(0.0 if (validate_examples[i][0] > 0.75) else 1.0)


		# Train Perceptron
		if(verbose):
			print(self.NOT.weights)
		valid_percentage = self.NOT.validate(validate_examples, validate_labels, verbose)
		if(verbose):
			print(valid_percentage)
			
		i = 0
		while valid_percentage < self.acc: # We want our Perceptron to have an accuracy of at least 80%

			i += 1

			self.NOT.train(training_examples, training_labels, 0.8)  # Train our Perceptron
			if(verbose):
				print('------ Iteration ' + str(i) + ' ------')
				print(self.NOT.weights)
			valid_percentage = self.NOT.validate(validate_examples, validate_labels, verbose) # Validate it
			if(verbose):
				print(valid_percentage)

			# This is just to break the training if it takes over 50 iterations. (For demonstration purposes)
			# You shouldn't need to do this as your networks may require much longer to train. 
			if i == sessions: 
				break
				
		#print("NOT"+str(valid_percentage))	
	
	#Used to get the threshold output from the weighted sum.	
	def activate(self,inputs):
		return self.NOT.activate(inputs)
			
