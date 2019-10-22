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
