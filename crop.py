import cv2


# Load image, convert to grayscale, Otsu's threshold
image = cv2.imread('test.jpeg')
result = image.copy()
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Detect horizontal lines
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (800,1))
detect_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
cnts = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
i=0 
y=0
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
	yp=y
	cv2.drawContours(result, [c], -1, (36,255,12), 2)
	x,y,w,h = cv2.boundingRect(c)
	ROI = result[y:h+y, x:w+x]
	i=i+1
	if i > 1:
		j=len(cnts)+1
		print (i)
		print(x,y)
		crop_img = result[y:yp, x:w+x]
		print(x+w,y+yp)
		cv2.imwrite("Ans"+str(j-i)+".jpg", crop_img)
	
	#cv2.waitKey(0)

cv2.imwrite('./images/result.jpg', result)
cv2.waitKey()
