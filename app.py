import sys
import cv2
import numpy as np

class MyImage:

	def __init__(self, path):
		self.image = cv2.imread(path)

	def displayImage(self):
		cv2.imshow('image', self.image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def applyGray(self):
		self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


path = sys.argv[1]

image = MyImage(path)
image.applyGray()
image.displayImage()
