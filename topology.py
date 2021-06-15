from ANDGate import ANDGate
from ORGate import ORGate
from NOTGate import NOTGate

class topology:
	def __init__(self,accuracy):
		self.ANDh = ANDGate(accuracy)
		self.ANDo = ANDGate(accuracy)
		self.ORh = ORGate(accuracy)
		self.NOTh = NOTGate(accuracy)
		
	def train(self,sessions,Generate:bool = True):
		self.ANDh.train(sessions,Generate)
		self.ANDo.train(sessions,Generate)
		self.ORh.train(sessions,Generate)
		self.NOTh.train(sessions,Generate)
	
	def input():
		return 0
