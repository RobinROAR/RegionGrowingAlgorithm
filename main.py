import regiongrowing as rr
import Image,time
from numpy import *

st = time.time();

image = Image.open('image/1.jpg') 
#转换称灰度图，转成矩阵
mat = array(image.convert("L"),'f')	

s = rr.regiongrowing(mat,20,24,(160,190))
#写入模块	
image.load()
putpixel = image.im.putpixel   #fill pixel

#矩阵和图像的坐标位相反

for i in range(image.size[1]):
	for j in range(image.size[0]):
		if (i,j) not in s:
			putpixel( (j,i),20)
		else:
			putpixel( (j,i),150)
			
	
output = "image/new"
image.thumbnail( (image.size[0], image.size[1] ), Image.ANTIALIAS )
image.save(output + ".JPEG","JPEG")

print image.size[0]*image.size[1]
print image.size[0],image.size[1]
	
et = time.time();
print 'It took '+ str(et-st)+'  s'
	
