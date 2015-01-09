import Image
from Quene import Quene
import regiongrowing
import numpy as np
from PIL import Image
import time
import block as bk
	
st = time.time()

#转换称灰度图，转成矩阵
image = Image.open('image/monkey.jpg') 
mat = np.array(image.convert("L"),'f')	

print mat	 

L = bk.blockInit(16,mat)

cnt = 0
for i in L:
	print '%0.4d' % (i.scoreMean(mat)),
	cnt+=1
	if(cnt ==15):
		print ''
		cnt=0




