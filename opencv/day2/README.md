## Windows 環境：
* 開啟 程式-> Anaconda3(64-bit) -> Anaconda Navigator
* 檢查所安裝的 python 套件版本
* 點選左邊選單的 Environment -> Create -> opencv , Python: 3.6 or 3.7
* ------------------------------------------------------------------
* 或是直接在 Anaconda Prompt 中直接執行:
*    conda create -n opencv python=3.6
*    activate opencv
*    pip install -r require.txt
*    下載： keras-yolo3：https://github.com/qqwweee/keras-yolo3
*    下載: [我的分享](https://drive.google.com/open?id=1OlIaqN1n-0bPlIBKpTOdNsvkRCXg63XN) 中的 yolo weights
* [VC++ Runtime](https://visualstudio.microsoft.com/zh-hant/downloads/)
* [Build tool](https://www.microsoft.com/zh-TW/download/details.aspx?id=48159)
## 樹莓派:
*   sudo apt-get update && sudo apt-get upgrade
*   安裝 OpenCV 4，參考: [Install OpenCV 4 on Raspberry Pi 4 and Raspbian Buster](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/)
*   或是直接安裝 opencv 套件
### python -m pip install opencv-python
### python -m pip install opencv-contrib-python
### python 
### >>> import cv2
### >>> `cv2.__version__`
##
*   workon cv
*   git clone https://github.com/pjreddie/darknet
*   cd darknet
*   make
*   下載: https://github.com/jumbokh/cv_face
##
### 參考網頁:
### [Darknet -- YOLO V2 with RPI](https://pjreddie.com/darknet/yolov2/)
### [比较OpenCV中4个haar特征训练的级联分类器](https://blog.csdn.net/u012679707/article/details/80377387)
### [使用Haar Cascade 进行人脸识别](https://blog.csdn.net/wutao1530663/article/details/78294349)
### [實驗參考一: 十行Python代码实现人脸识别](https://zhuanlan.zhihu.com/p/66368987)
### [實驗參考二:Face Recognition with Python, in Under 25 Lines of Code](https://realpython.com/face-recognition-with-python/)
### [不同版本 opencv 參數錯誤參考: 人脸定位和识别](http://zhangchunlei.com/blog/2015/11/26/face-detection-and-recognition/)
### [實驗參考三:重磅：TensorFlow实现YOLOv3](https://cloud.tencent.com/developer/article/1093051)
### [實驗參考四(樹莓派 DarkNet): YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolov2/)
### [實驗參考五(opencv): Python 與 OpenCV 基本讀取、顯示與儲存圖片教學](https://blog.gtwang.org/programming/opencv-basic-image-read-and-write-tutorial/)
### [實驗參考六 : Haar Training](https://github.com/sauhaardac/Haar-Training)

