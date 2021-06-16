from ANDGate import ANDGate
from ORGate import ORGate
from NOTGate import NOTGate

class topology:
	#Initialize each gate.
	def __init__(self,accuracy):
		self.ANDh = ANDGate(accuracy)
		self.ANDo = ANDGate(accuracy)
		self.ORh = ORGate(accuracy)
		self.NOTh = NOTGate(accuracy)
		
	#Trains all the gates required by the XOR
	def train(self,sessions,verbose,Generate):
		print("Training GATE_0...")
		self.ANDh.train(sessions,Generate,verbose)
		print("Training GATE_1...")
		self.ANDo.train(sessions,Generate,verbose)
		print("Training GATE_2...")
		self.ORh.train(sessions,Generate,verbose)
		print("Training GATE_3...")
		self.NOTh.train(sessions,Generate,verbose)
	
	#Give two inputs into the network.
	def XORGate(self,inputs: [float],verbose):
		y1 = self.ANDh.activate(inputs)
		
		if(verbose):
			print("AND "+str(y1))
			
		y1 = self.NOTh.activate([y1])
		y2 = self.ORh.activate(inputs)
		
		if(verbose):
			print("NOT "+str(y1))
			print("OR "+str(y2))
			print("AND "+str(self.ANDo.activate([y1,y2])))
		
		return self.ANDo.activate([y1,y2])
