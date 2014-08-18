import os,time
from Stack import Stack
from numpy import *


#Parameters: matrix, epsilon, satr_point
def  regiongrowing(mat,epsilon,meancount,start_point):
	
	print mat.shape
	#use stack store candidates
	ST = Stack()
	
	#extracted result  is stored here	
	s = []						
	x = start_point[0]
	y = start_point[1]
	
	#feed enter stack
	ST.ensta((x,y))					
	
	while not ST.isEmpty():
		
		#get mean
		temp = ST.getLastN(meancount)
		sum = 0
		for i in temp:
			xt = i[0]
			yt = i[1]
			sum += mat[xt][yt]
			
			
		mean = float(sum)/len(temp)
		
		t = ST.desta()
		x = t[0]
		y = t[1]
		
		if t not in s:
			s.append( t )
		
		#8-connected neighborhood 
		if x < len(mat)-1 and abs(mat[x+1][y] - mean ) <= epsilon :
			if not ST.isInside( (x + 1 , y) ) and not (x + 1 , y) in s:
				ST.ensta( (x + 1 , y) )
				
		if x < len(mat)-1 and y < len(mat[0])-1 and abs(mat[x+1][y+1] - mean ) <= epsilon :
			if not ST.isInside( (x + 1 , y+1) ) and not (x + 1 , y+1) in s:
				ST.ensta( (x + 1 , y+1) )
			
		if y < len(mat[0])-1 and abs(  mat[x][y+1]-mean ) <= epsilon:
			if not ST.isInside( (x, y + 1) ) and not (x , y + 1) in s:
				ST.ensta( (x , y + 1) )
			
		if x >0 and y < len(mat[0])-1 and abs(mat[x-1][y+1] - mean ) <= epsilon :
			if not ST.isInside( (x - 1 , y+1) ) and not (x - 1 , y+1) in s:
				ST.ensta( (x - 1 , y+1) )
				
		if x > 0 and abs( mat[x - 1] [y] - mean  ) <= epsilon:
			if not ST.isInside( (x - 1 , y) ) and not (x - 1 , y) in s:
				ST.ensta( (x - 1 , y) )	
				
		if x > 0 and y >0 and abs(mat[x-1][y-1] - mean ) <= epsilon :
			if not ST.isInside( (x - 1 , y - 1) ) and not (x - 1 , y -1) in s:
				ST.ensta( (x - 1 , y-1) )	
				
		if y > 0 and abs( mat[x][y-1]-mean ) <= epsilon:
			if not ST.isInside( (x ,y - 1) ) and not (x , y - 1) in s:
				ST.ensta( (x , y - 1) )
	
		if x < len(mat)-1 and y >0 and abs(mat[x+1][y-1] - mean ) <= epsilon :
			if not ST.isInside( (x +1 , y - 1) ) and not (x + 1 , y -1) in s:
				ST.ensta( (x + 1 , y - 1 ) )
		
		print len(s)
	
	return s
	

	



