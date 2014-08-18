class Stack:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
	

	def ensta(self,item):
		self.items.append(item)
	
	
	def desta(self):
		return self.items.pop()
	
	def ssize(self):
		return len(self.items)
	
	def isInside(self,item):
		return (item in self.items)
		

	def getLastN(self,n):
		if self.ssize() < n:
			return self.items
		else:
			return self.items[-n:]
	
	def __str__(self):
		return self.items