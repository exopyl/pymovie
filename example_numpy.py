import numpy, cv2

frameSize = (500, 500)

out = cv2.VideoWriter('numpy.avi',cv2.VideoWriter_fourcc('P','I','M','1'), 60, frameSize)

for i in range(0,255):
    img = numpy.ones((500, 500, 3), dtype=numpy.uint8)*i
    out.write(img)

out.release()
