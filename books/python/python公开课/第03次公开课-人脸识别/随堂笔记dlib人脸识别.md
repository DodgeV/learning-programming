# dlib人脸识别

### 1、dlib安装

​	代码的编写在jupyter notebook中来完成

​	jupyter notebook是一个工具

​	pip install jupyter ------------>安装使用

​	如何启动：

​		命令行输入：jupyter notebook

​		前提，环境变量配置成功

​	

​	dlib安装-------------> pip install dlib

​	dlib有不同的版本，最新版本（19.17.0），经过测试，dll包不完备，所以上次我在使用时，出了一点问题,随着时间的推移，修复

​	建议大家安装之前的版本（19.8.1）

​	pip install dlib==19.8.1

### 2、dlib人脸识别

​	cv2和dlib异同

​	都可以识别人脸

​	cv2级联方式识别人脸，启用算法时，人脸特征数据：haar

​	dlib底层使用的是深度神经网络

​	所以dlib识别准确率，要比opencv（cv2）高

​	pip install opencv-python

​	我们就可以在代码中，导包了

​	dlib调用相应方法，识别人脸

​	face_detector = dlib.get_frontal_face_detector()

​	调用：

​			人脸坐标数据

​			faces = face_detector(image,1)

​	绘制：

    	for face in faces:
    		left = face.left()
    		top = face.top()
    		right = face.right()
    		bottom = face.bottom()
    
    		cv2.rectangle(jin,pt1 = (left,top),pt2 = (right,bottom),color = [0,0,255],thickness = 2)
​	

### 3、dlib多张人脸的识别

​	jupyter执行代码 Ctrl + Enter

​	多张人脸和单张人脸识别的代码完全一样的

### 4、dlib可以识别视频中的人脸

​	视频操作，首先读取视频

​	cv2工具---------> opencv------->计算机视觉

​	演示，视频每一张图片，进行显示

​	cv2.waitKey(10) -------->毫秒，快进感觉

​	视频中人脸可以检测，但是播放速度变慢，为什么？？？

​	因为人脸识别，算法应用，大量计算，计算时，花时间的

### 5、dlib可以标记人脸的关键点（轮廓点）

​	1、识别人脸

​	2、轮廓识别人脸关键点

​		人脸68个关键点：嘴巴，鼻子，眼睛，眉毛，轮廓

​		shape = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

​		facemarks = shape(jin,face)



​		for mark in facemarks.parts():    

​			x =  mark.x    

​			y = mark.y    

​			cv2.circle(jin,center = (x,y),radius = 2,color = [0,255,0],thickness = 2)

### 6、相应的软件：
+ jupyter notebook---------> pip install jupyter
+ opencv -------------------> pip install opencv-python
+ dlib -----------------------> pip install dlib==19.8.1