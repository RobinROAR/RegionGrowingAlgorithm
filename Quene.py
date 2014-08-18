class Quene:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
	
	def enque(self,item):
		self.items.insert(0,item)
		
	def deque(self):
		return self.items.pop()
	
	def qsize(self):
		return len(self.items)
	
	def isInside(self,item):
		return (item in self.items)
		

	def getLastN(self,n):
		if self.qsize() < n:
			return self.items
		else:
			return self.items[-n:]
	
	def __str__(self):
		return self.items