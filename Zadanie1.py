from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

def main():
    image = Image.open("Lemon.png")
    imageArray = np.asarray(image)

    #print(repr(imageArray))
    imagePlot = plt.imshow(imageArray)
    plt.show()

if __name__ == "__main__":
    main()