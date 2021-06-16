from ANDGate import ANDGate
from ORGate import ORGate
from NOTGate import NOTGate

class topology:
	def __init__(self,accuracy):
		self.ANDh = ANDGate(accuracy)
		self.ANDo = ANDGate(accuracy)
		self.ORh = ORGate(accuracy)
		self.NOTh = NOTGate(accuracy)
		
	def train(self,sessions,verbose,Generate):
		print("Training GATE_0...\n")
		self.ANDh.train(sessions,Generate,verbose)
		print("Training GATE_1...\n")
		self.ANDo.train(sessions,Generate,verbose)
		print("Training GATE_2...\n")
		self.ORh.train(sessions,Generate,verbose)
		print("Training GATE_3...\n")
		self.NOTh.train(sessions,Generate,verbose)
	
	def input():
		return 0
		
	def XORGate(self,inputs: [float]):
		y1 = self.ANDh.activate(inputs)
		print("AND "+str(y1))
		y1 = self.NOTh.activate([y1])
		print("NOT "+str(y1))
		y2 = self.ORh.activate(inputs)
		print("OR "+str(y2))
		
		print("AND "+str(self.ANDo.activate([y1,y2])))
		
		return self.ANDo.activate([y1,y2])
