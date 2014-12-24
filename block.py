#Robin 
#@Cnic 2014.12.27
#反向块增长
import numpy as np

#自定义类--
class Block:
	
	def __init__(self, a = (0,0), width = 2,num=0):
		''' 生成一个正方形abcd，num为代号，a为左上角点，宽度为width = 1，矩形包括点数pn = 4，flag为标志位，'''
		self.num = num
		self.width = width
		self.a = a
		self.b = (a[0],a[1]+width)
		self.c = (a[0]+width,a[1])
		self.d = (a[0]+width,a[1]+width)
		self.pn = width**2
		self.flag = 0
	
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
			

#自定义方法-暂时放在一起
def 	findBiggestSubset(L1):
	'''返回最大联通子集'''
	maxsubset = []
	sum = 0
	for i in L1:
		#~ print 'i = ',i.num
		result =[]
		temp = [i]
		while len(temp)>0:
			j = temp[0]
			for k in L1:
				if j==k:
					continue
				else:
					if j.testConnectivity(k) and k not in temp and k not in result:
						temp.append(k)
						#~ print 'add:',k.num
						
			#~ print 'j:',j.num
			result.append(j)
			temp.remove(j)
			#~ for x in temp:
				#~ print "t:",x.num
			#~ print 'temp长：',len(temp)
		print 'result: ',i.num,len(result)
		if len(result)>sum:
			sum = len(result)
			maxsubset = result
	return maxsubset


def markBlock(list,mat):
	'''根据返回的最大子集标记点'''
	result= []
	hig = mat.shape[0]
	wid = mat.shape[1]
	for i in range(hig):
		for j in range(wid):
			for x in list:
			#x = list[0]
				if i>=x.a[0] and i<=x.d[0] and j >= x.a[1] and j <=x.d[1] and (i,j) not in result:
					result.append((i,j))
	return result
				
def redraw(result,mat):
	'''根据标记节点重新画图'''
	#矩阵和图像的坐标位相反
	
	
	st = time.time()
	putpixel = image.im.putpixel   
	for i in range(mat.shape[0]):
		for j in range(mat.shape[1]):
			putpixel( (j,i),20)			
	for i in result:
		j = (i[1],i[0])
		putpixel( j ,150)
				
		
	output = "new1"
	image.thumbnail( (image.size[0], image.size[1] ), Image.ANTIALIAS )
	image.save(output + ".JPEG","JPEG")

	print image.size[0]*image.size[1]
	print image.size[0],image.size[1]
		
	et = time.time();
	print 'It took '+ str(et-st)+'  s'
	
def  blockDividing(n,mat):
	'''基本的块增长算法'''
	#求宽度
	hig = mat.shape[0]
	wid = mat.shape[1]
	print 'hig: ',hig,'wid', wid
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
	bw = width / n
	x=0
	y=0
	L = []
	cnt = 1
	for i in range(n):
		for j in range(n):
			btemp = Block((x,y),bw,cnt)
			L.append(btemp)
			cnt+=1
			y+=bw
		x+=bw
		y =0
	return L

def  judgeBlock(L):
	'''通过判定函数筛选结果'''
	for i in L:
		#if i.scoreVar(mat)>=270 and i.scoreVar(mat)<387:
		if i.scoreVar(mat)>=200:
			i.flag = 1
	
	#打印结果
	L1 = []
	for i in L:
		if i.flag ==1:
			print i.num
			print i.scoreVar(mat)
			L1.append(i)
	return L1
	
	
def  BlockGrowing(result,mat,n):
	'''缩小窗口宽度，环绕增长'''
	L = blockDividing(n,mat)
	L1 = judgeBlock(L)
	L3 = []
	for i in L1: 
		cnt = 0
		if i.a in result:
			cnt+=1
		if i.b in result:
			cnt+=1
		if i.c in result:
			cnt+=1
		if i.d in result:
			cnt+=1
		if cnt >0 and cnt < 4:
			L3.append(i)
	return L3
			
		
		

#调试用方法
if __name__ == "__main__":
	from PIL import Image
	import time
	
	#转换称灰度图，转成矩阵
	image = Image.open('image/monkey.jpg') 
	mat = np.array(image.convert("L"),'f')	
	
	L = blockDividing(4,mat)
	L1 = judgeBlock(L)
	
	#~ print "***************************"
	
	
	#~ s = findBiggestSubset(L1)
	
	#~ for i in s:
		#~ print i.num
	#~ s1 = markBlock(s,mat)
	#~ redraw(s1,mat)

		
	
					
					
					