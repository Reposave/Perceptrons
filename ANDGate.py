import random
from Perceptron import Perceptron

class ANDGate:
	def __init__(self,accuracy):
		self.acc = accuracy
		self.AND = Perceptron(2, bias=-1.0)
		return None
		
	def train(self,sessions,Generate: bool = True,verbose: bool =False): #Set default to 50.
		generate_training_set = Generate
		num_train = 1000
		generate_validation_set = Generate
		num_valid = 1000

		training_examples = [[1.0, 1.0],
							[1.0, 0.0],
							[0.0, 1.0],
							[0.0, 0.0]]

		training_labels = [1.0, 0.0, 0.0, 0.0]

		validate_examples = training_examples
		validate_labels = training_labels

		if generate_training_set:

			training_examples = []
			training_labels = []

			for i in range(num_train):
				training_examples.append([random.uniform(0,1), random.uniform(0,1)])
				# We want our perceptron to be noise tolerant, so we label all examples where x1 and x2 > 0.8 as 1.0
				training_labels.append(1.0 if ((training_examples[i][0] > 0.75) and (training_examples[i][1] > 0.75)) else 0.0)

		if generate_validation_set:

			validate_examples = []
			validate_labels = []

			for i in range(num_train):
				validate_examples.append([random.uniform(0,1), random.uniform(0,1)])
				validate_labels.append(1.0 if ((validate_examples[i][0] > 0.75) and (validate_examples[i][1] > 0.75)) else 0.0)


		# Create Perceptron
		if(verbose):
			print(self.AND.weights)
		valid_percentage = self.AND.validate(validate_examples, validate_labels, verbose)
		if(verbose):
			print(valid_percentage)
		i = 0
		while valid_percentage < self.acc: # We want our Perceptron to have an accuracy of at least 80%

			i += 1

			self.AND.train(training_examples, training_labels, 0.8)  # Train our Perceptron
			if(verbose):
				print('------ Iteration ' + str(i) + ' ------')
				print(self.AND.weights)
				
			valid_percentage = self.AND.validate(validate_examples, validate_labels, verbose) # Validate it
			if(verbose):
				print(valid_percentage)

			# This is just to break the training if it takes over 50 iterations. (For demonstration purposes)
			# You shouldn't need to do this as your networks may require much longer to train. 
			if i == sessions: 
				break
		print("AND"+str(valid_percentage))	
				
	def activate(self,inputs):
		return self.AND.activate(inputs)
