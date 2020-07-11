import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def get_hist(path_file):
    img = cv2.imread(path_file,0)
    file_name = path_file.split('/', -1)[-1]
    hist,bins = np.histogram(img.flatten(),256,[0,256])
    print(bins)
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()
    #print("element ", len(cdf))
    #print("cdf  ", cdf)
    #print("element ", len(cdf_normalized))
    # plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    # plt.xlim([0,256])
    # plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()

    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    print("cdf  ", cdf)
    img2 = cdf[img]

    cv2.imwrite('result_' + file_name, img2)

images_dir = 'C:/Users/huynh/OneDrive/Documents/Code/03_Thesis/01_Histogram/compare-histograms-opencv/images/'
image_files = os.listdir(images_dir)

for file in image_files:
    file_path = os.path.join(images_dir, file)
    get_hist(file_path)
