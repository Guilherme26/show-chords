import yaml
import random
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from time import sleep


def main():
	params = yaml.load(open("params.yml"))

	files = os.listdir(params["imgs_path"])
	images = [mpimg.imread(os.path.join(params["imgs_path"], file)) for file in files]
	
	plt.ion()

	for _ in range(params["train_time"] // params["sleep_time"]):
		image = random.choice(images)
		
		plt.imshow(image)
		plt.draw()
		plt.pause(params["sleep_time"])


if __name__=="__main__":
	main()
