from PIL import Image
import numpy, cv2
from rich import print

# images source & target
image1 = Image.new('RGB', (640, 480), (255, 0, 0))
image2 = Image.new('RGB', (640, 480), (0, 255, 0))

height, width, layers =  numpy.array(image1).shape
print("{} x {} ({})".format(width, height, layers))

# codecs : http://www.fourcc.org/codecs.php
video = cv2.VideoWriter("transition.avi", # Filename
                        cv2.VideoWriter_fourcc('P','I','M','1'), # -1 for manual codec selection. You can make this automatic by defining the "fourcc codec" with "cv2.VideoWriter_fourcc"
                        30, # 10 frames per second is chosen as a demo, 30FPS and 60FPS is more typical
                        (width,height) # The width and height come from the stats of image1
                        )

for i in range(0,60):
    images1And2 = Image.blend(image1, image2, i/60.0)
    video.write(cv2.cvtColor(numpy.array(images1And2), cv2.COLOR_RGB2BGR))

video.release()
