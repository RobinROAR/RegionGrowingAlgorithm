#Robin 
#@Cnic 2014.12.27
#反向块增长
import numpy as np

class Block:
	
	def __init__(self, a = (0,0), width = 2):
		''' 生成一个正方形abcd，a为左上角点，宽度为width = 1，矩形包括点数pn = 4'''
		self.width = width
		self.a = a
		self.b = (a[0],a[1]+width)
		self.c = (a[0]+width,a[1])
		self.d = (a[0]+width,a[1]+width)
		self.pn = width**2
	
	def testConnectivity(self,bt):
		'''测试两个块之间的联通性，如果四个顶点有交点则联通'''
		for i in [self.a, self.b, self.c, self.d]:
			for j in [bt.a, bt.b, bt.c, bt.d ]:
				if(i == j):
					return 1
		return 0

	def scoreVar(self,mat):
		'''评价函数1：方差'''
		L = []
		x = self.a[0]
		y = self.a[1]
		for i in range(self.width):
			for j in range(self.width):
				L.append(mat[x,y])
				y+=1
			x+=1
			y = 0
		L = np.array(L)
		return np.var(L)
			

#调试用方法
if __name__ == "__main__":
	import Image,time
	
	#~ b1 = Block((0,0),50)
	#~ b2 = Block((13,13),2)
	#~ print b1.a,b1.d,b1.width,b1.pn
	#~ print b1.testConnectivity(b2)
	
	
	image = Image.open('image/monkey.jpg') 
	#转换称灰度图，转成矩阵
	mat = np.array(image.convert("L"),'f')	
	
	#求宽度
	hig = mat.shape[0]
	wid = mat.shape[1]
	if(hig >=wid):
		if(wid%2 == 0):
			width = wid
		else:
			width = wid-1
	else:
		if(hig%2 == 0):
			width = hig
		else:
			width = hig-1
	
	#第一次划分
	n=2
	bw = width / n
	point = [0,0]
	L = []
	for i in range(n):
		for j in range(n):
			btemp = Block(point,bw)
			L.append(btemp)
			for i in L:
				print i.a
			print '____________'
			point[1] +=bw
		point[0]+=bw
		point[1] =0
	

	
		
