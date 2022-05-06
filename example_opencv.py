import cv2, numpy

img = numpy.zeros((500, 500, 3), dtype=numpy.uint8)
img.fill(255)
cv2.putText(img=img, text='Hello', org=(100, 250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 0, 0),thickness=3)
cv2.imwrite("hello.png", img)

frameSize = (500, 500)
out = cv2.VideoWriter('opencv.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, frameSize)

# kernel for the dilation
kernel = numpy.ones((2,2), numpy.uint8)

for i in range(100):
    img = cv2.erode(img, kernel, iterations=1)
    filename = "{}.png".format(i)
    out.write(img)

out.release()
