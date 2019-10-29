import urllib
from urllib import urlopen
import cv2
import numpy as np
import os
import time
import glob
 
cv2.namedWindow("Out",cv2.WINDOW_NORMAL)
 
def store_raw_images():
    neg_images_link ='http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02758863'
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02692232'
    neg_image_urls = urlopen(neg_images_link).read()
    print neg_image_urls
    pic_num = 520
 
    if not os.path.exists('pos'):
        os.makedirs('pos')
 
    for i in neg_image_urls.split('\n'):
        try:
            urllib.urlretrieve(i, "pos/"+str(pic_num)+".jpg")
            img = cv2.imread("pos/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (200, 200))
            if resized_image is not None:
                cv2.imwrite("pos/"+str(pic_num)+".jpg",resized_image)
            print str(pic_num) + " - " + str(i) + "\n"
            pic_num += 1
 
        except Exception as e:
            print(str(e))
 
store_raw_images()
