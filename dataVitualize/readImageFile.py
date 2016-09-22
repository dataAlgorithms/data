#! coding=utf-8

def showImageFile():

    import scipy.misc
    import matplotlib.pyplot as plt

    # load already prepared ndarray from scipy
    lena = scipy.misc.lena()

    # set the default colormap to gray
    plt.gray()
    plt.imshow(lena)
    plt.colorbar()
    plt.show()

    print lena.shape
    print lena.max()
    print lena.dtype

def readImageFile():

    import numpy
    from PIL import Image # can work
    import matplotlib.pyplot as plt

    bug = Image.open('stinkbug.png')
    arr = numpy.array(bug.getdata(), numpy.uint8).reshape(bug.size[1],bug.size[0],3)
    plt.gray()
    plt.imshow(arr)
    plt.colorbar()
    plt.show()
    
    import scipy

    bug = scipy.misc.imread('stinkbug.png')
    # if you want to inspect the shape of the loaded image
    # uncomment following line
    print bug.shape
    # the original image is RGB having values for all three
    # channels separately. For simplicity, we convert that to greyscale image
    # by picking up just one channel.
    # convert to gray
    bug = bug[:,:,0]
    
    # huge image file
    import numpy
    file_name = 'stinkbug.png'
    image = numpy.memmap(file_name, dtype=numpy.uint8, shape = (375, 500))

if __name__ == "__main__":
    showImageFile()
    readImageFile()