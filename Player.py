class Player(object):
	"""docstring for Player"""
	name = None
	points = 0

	def __init__(self, name, points):
		self.name = name
		self.points = points

	def getName(self):
		return self.name

	def getPoints(self):
		return self.points

	def addPoints(self, add):
		self.points = self.points + add

	def removePoints(self, take):
		self.points = self.points - take
