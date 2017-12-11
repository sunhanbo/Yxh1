import tensorflow as tf
import numpy as np
from skimage import io,transform 
from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtCore import QThread
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListWidgetItem ,QListView
from PyQt5.Qt import QFont
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 822)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(290, 20, 781, 731))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setIconSize(QSize(180, 185))
        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setMovement(QListView.Static)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(30, 30, 191, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 190, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 260, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 330, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 400, 151, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 470, 151, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 540, 151, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 610, 151, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 240, 41))
        self.lineEdit.setObjectName("lineEdit")
        
        self.images = get_all_picture('E:\pic')
        for i in range(len(self.images)):
            jpg = QPixmap(self.images[i])
            item = QListWidgetItem(QIcon(jpg.scaled(QSize(160, 160))), self.images[i] ,self.listWidget)
            item.setSizeHint(QSize(180, 185))
            self.listWidget.addItem(item)
            #self.listWidget.insertItem(i, item)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "请输入文件夹："))
        self.pushButton.setText(_translate("MainWindow", "查看全部图片"))
        self.pushButton_2.setText(_translate("MainWindow", "动物"))
        self.pushButton_3.setText(_translate("MainWindow", "二次元"))
        self.pushButton_4.setText(_translate("MainWindow", "风景"))
        self.pushButton_5.setText(_translate("MainWindow", "美食"))
        self.pushButton_6.setText(_translate("MainWindow", "人物"))
        self.pushButton_7.setText(_translate("MainWindow", "相似图片"))
        self.lineEdit.setText(_translate("MainWindow", "E:\\pic"))

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(655, 755)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(QtCore.QRect(80, 60, 50, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 540, 30))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


a = []
a_animal = []
a_erciyuan = []
a_fengjing = []
a_food = []
a_man = []
a_sample = []
b = []
c = []
images_all = []
#pixels = []
class myThread(QThread):
    global b, images_all
    finishSignal = QtCore.pyqtSignal(list)
    def __init__(self, pth, parent=None):
        super(myThread,self).__init__(parent=parent)
        self.pth = pth
    def run(self):
        if len(b) == 0:
            b.append(self.pth)
            images = get_all_picture(self.pth)
            for i in range(len(images)):
                images_all.append(images[i])
            self.finishSignal.emit(images_all)
        elif b[0] == self.pth:
            self.finishSignal.emit(images_all)
        else :
            b.pop()
            b.append(self.pth)
            num = len(images_all)
            for i in range(num):
                images_all.pop()
            images = get_all_picture(self.pth)
            for i in range(len(images)):
                images_all.append(images[i])
            self.finishSignal.emit(images_all)
class myThread2(QThread):
    global a
    global a_animal, a_erciyuan, a_fengjing, a_food, a_man
    finishSignal = QtCore.pyqtSignal(list)
    def __init__(self, pth, parent=None):
        super(myThread2,self).__init__(parent=parent)
        self.pth = pth
    def run(self):
        if len(a) == 0:
            a.append(self.pth)
            images = get_all_picture(self.pth)
            labs = getClass(images)
            for i in range(len(labs)):
                if labs[i] == 0:
                    a_animal.append(images[i])
                elif labs[i] == 1:
                    a_erciyuan.append(images[i])
                elif labs[i] == 2:
                    a_fengjing.append(images[i])
                elif labs[i] == 3:
                    a_food.append(images[i])
                elif labs[i] == 4:
                    a_man.append(images[i])
            self.finishSignal.emit([2, 2])
        elif a[0] == self.pth:
            self.finishSignal.emit([1, 1])
        else:
            a.pop()
            a.append(self.pth)
            images = get_all_picture(self.pth)
            labs = getClass(images)
            num = len(a_animal)
            for _ in range(num):
                a_animal.pop()
            num = len(a_erciyuan)
            for _ in range(num):
                a_erciyuan.pop()
            num = len(a_fengjing)
            for _ in range(num):
                a_fengjing.pop()
            num = len(a_food)
            for _ in range(num):
                a_food.pop()
            num = len(a_man)
            for _ in range(num):
                a_man.pop()
                
            for i in range(len(labs)):
                if labs[i] == 0:
                    a_animal.append(images[i])
                elif labs[i] == 1:
                    a_erciyuan.append(images[i])
                elif labs[i] == 2:
                    a_fengjing.append(images[i])
                elif labs[i] == 3:
                    a_food.append(images[i])
                elif labs[i] == 4:
                    a_man.append(images[i])
            self.finishSignal.emit([3, 3])
   
class myThread3(QThread):
    global c, a_sample
    finishSignal = QtCore.pyqtSignal(list)
    def __init__(self, pth, parent=None):
        super(myThread3,self).__init__(parent=parent)
        self.pth = pth
    def run(self):
        if len(c) == 0:
            c.append(self.pth)
            images = get_all_picture(self.pth)
            img = getSample(images)
            for i in range(len(img)):
                a_sample.append(img[i])
            self.finishSignal.emit(a_sample)
        elif c[0] == self.pth:
            self.finishSignal.emit(a_sample)
        else :
            c.pop()
            c.append(self.pth)
            num = len(a_sample)
            for i in range(num):
                a_sample.pop()
            images = get_all_picture(self.pth)
            img = getSample(images)
            for i in range(len(img)):
                a_sample.append(img[i])
            self.finishSignal.emit(a_sample)
    
class windowTwo(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self,parent=None):
        super(windowTwo, self).__init__(parent=parent)
        self.setupUi(self)
class windowOne(QtWidgets.QMainWindow, Ui_MainWindow):
    def  __init__(self,parent=None):
        super(windowOne, self).__init__(parent=parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.doWork)
        self.pushButton_2.clicked.connect(self.doWork2)
        self.pushButton_3.clicked.connect(self.doWork3)
        self.pushButton_4.clicked.connect(self.doWork4)
        self.pushButton_5.clicked.connect(self.doWork5)
        self.pushButton_6.clicked.connect(self.doWork6)
        self.pushButton_7.clicked.connect(self.doWork7)
        self.listWidget.itemDoubleClicked.connect(self.print1)
    def print1(self):
        myshowpic.label_2.setText(self.listWidget.currentItem().text())
        myshowpic.label_2.setFont(QFont('Arial', 10))
        jpg = QPixmap(self.listWidget.currentItem().text())
        myshowpic.label.resize(jpg.width(), jpg.height())
        myshowpic.label.setPixmap(jpg)
        myshowpic.show()
    def close_w1(self):
        self.close()
    def open_w1(self):
        self.show()
    def doWork(self):
        self.pushButton.setDisabled(True)
        #开始一个进度条？
        self.mThread = myThread(self.lineEdit.text())
        self.mThread.finishSignal.connect(self.doneWork)
        self.mThread.start()
    def doWork2(self):
        self.pushButton_2.setDisabled(True)
        #开始一个进度条？
        self.mThread2 = myThread2(self.lineEdit.text())
        self.mThread2.finishSignal.connect(self.doneWork2)
        self.mThread2.start()
    def doWork3(self):
        self.pushButton_3.setDisabled(True)
        #开始一个进度条？
        self.mThread2 = myThread2(self.lineEdit.text())
        self.mThread2.finishSignal.connect(self.doneWork3)
        self.mThread2.start()
    def doWork4(self):
        self.pushButton_4.setDisabled(True)
        #开始一个进度条？
        self.mThread2 = myThread2(self.lineEdit.text())
        self.mThread2.finishSignal.connect(self.doneWork4)
        self.mThread2.start()
    def doWork5(self):
        self.pushButton_5.setDisabled(True)
        #开始一个进度条？
        self.mThread2 = myThread2(self.lineEdit.text())
        self.mThread2.finishSignal.connect(self.doneWork5)
        self.mThread2.start()
    def doWork6(self):
        self.pushButton_6.setDisabled(True)
        #开始一个进度条？
        self.mThread2 = myThread2(self.lineEdit.text())
        self.mThread2.finishSignal.connect(self.doneWork6)
        self.mThread2.start()
    def doWork7(self):
        self.pushButton_7.setDisabled(True)
        self.mThread3 = myThread3(self.lineEdit.text())
        self.mThread3.finishSignal.connect(self.doneWork7)
        self.mThread3.start()
    def doneWork(self, ls):
        #结束进度条？
        num = self.listWidget.count()
        for _ in range(num):
            self.listWidget.takeItem(0)
        #print(self.listWidget.count())
        for i in range(len(ls)):
            jpg = QPixmap(ls[i])
            item = QListWidgetItem(QIcon(jpg.scaled(QSize(160, 160))), ls[i] ,self.listWidget)
            item.setSizeHint(QSize(180, 185))
            self.listWidget.addItem(item)
        self.pushButton.setDisabled(False)
    def doneWork2(self, ls):
        num = self.listWidget.count()
        for _ in range(num):
            self.listWidget.takeItem(0)
        #print(self.listWidget.count())
        for i in range(len(a_animal)):
            jpg = QPixmap(a_animal[i])
            item = QListWidgetItem(QIcon(jpg.scaled(QSize(160, 160))), a_animal[i] ,self.listWidget)
            item.setSizeHint(QSize(180, 185))
            self.listWidget.addItem(item)
        self.pushButton_2.setDisabled(False)
    def doneWork3(self, ls):
        num = self.listWidget.count()
        for _ in range(num):
            self.listWidget.takeItem(0)
        #print(self.listWidget.count())
        for i in range(len(a_erciyuan)):
            jpg = QPixmap(a_erciyuan[i])
            item = QListWidgetItem(QIcon(jpg.scaled(QSize(160, 160))), a_erciyuan[i] ,self.listWidget)
            item.setSizeHint(QSize(180, 185))
            self.listWidget.addItem(item)
        self.pushButton_3.setDisabled(False)
    def doneWork4(self, ls):
        num = self.listWidget.count()
        for _ in range(num):
            self.listWidget.takeItem(0)
        #print(self.listWidget.count())
        for i in range(len(a_fengjing)):
            jpg = QPixmap(a_fengjing[i])
            item = QListWidgetItem(QIcon(jpg.scaled(QSize(160, 160))), a_fengjing[i] ,self.listWidget)
            item.setSizeHint(QSize(180, 185))
            self.listWidget.addItem(item)
        self.pushButton_4.setDisabled(False)
    def doneWork5(self, ls):
        num = self.listWidget.count()
        for _ in range(num):
            self.listWidget.takeItem(0)
        #print(self.listWidget.count())
        for i in range(len(a_food)):
            jpg = QPixmap(a_food[i])
            item = QListWidgetItem(QIcon(jpg.scaled(QSize(160, 160))), a_food[i] ,self.listWidget)
            item.setSizeHint(QSize(180, 185))
            self.listWidget.addItem(item)
        self.pushButton_5.setDisabled(False)
    def doneWork6(self, ls):
        num = self.listWidget.count()
        for _ in range(num):
            self.listWidget.takeItem(0)
        #print(self.listWidget.count())
        for i in range(len(a_man)):
            jpg = QPixmap(a_man[i])
            item = QListWidgetItem(QIcon(jpg.scaled(QSize(160, 160))), a_man[i] ,self.listWidget)
            item.setSizeHint(QSize(180, 185))
            self.listWidget.addItem(item)
        self.pushButton_6.setDisabled(False)     
    def doneWork7(self, ls):
        print(ls)
        num = self.listWidget.count()
        for _ in range(num):
            self.listWidget.takeItem(0)
        #print(self.listWidget.count())
        for i in range(len(ls)):
            jpg = QPixmap(ls[i])
            item = QListWidgetItem(QIcon(jpg.scaled(QSize(160, 160))), ls[i] ,self.listWidget)
            item.setSizeHint(QSize(180, 185))
            self.listWidget.addItem(item)
        self.pushButton_7.setDisabled(False)        
def get_all_picture(str1):
    images = []
    for root, dirs, files in os.walk(str1):
        for file in files:
            if os.path.splitext(file)[1] == '.bmp' or os.path.splitext(file)[1] == '.jpg' or os.path.splitext(file)[1] == '.png':
                images.append(os.path.join(root, file))
        for dir1 in dirs:
            get_all_picture(dir1)
    return images

def getSample(pth):
    pixels = []
    finallist = []
    for i in range(len(pth)):
        a = get_64_pixel(pth[i])
        pixels.append(a)
    while len(pixels) > 0:
        pth0 = pth[0]
        p0 = pixels[0]
        temp2 = 0
        del pth[0]
        del pixels[0]
        i = 0
        while i < len(pixels):
            temp = 0
            pi = pixels[i]
            for j in range(64):
                if p0[j] != pi[j]:
                    temp += 1
                if temp >= 5:
                    break
            if temp < 5:
                if temp2 == 0:
                    temp2 += 1
                    finallist.append(pth0)
                    finallist.append(pth[i])
                else:
                    finallist.append(pth[i])
                del pth[i]
                del pixels[i]
                i -= 1
            i += 1
    return finallist
def get_64_pixel(pt):
    code = []
    try:
        img = io.imread(pt)
        img = transform.resize(img, (8, 8, 3))
    except Exception:
        for i in range(64):
            code.append(1)
        return code
    else:
        sum = 0
        pix = []
        for i in range(8):
            for j in range(8):
                gray = (int)(64 * (img[i][j][0] + img[i][j][1] + img[i][j][2])/3)
                pix.append(gray)
                sum += gray
        ave = sum / 64
        for i in range(8):
            for j in range(8):
                if pix[i * 8 + j] >= ave:
                    code.append(1)
                else:
                    code.append(0)
        return code
def getClass(pth):
    labels = []
    with tf.Graph().as_default():
        output_graph_def = tf.GraphDef()
 
        with open('E:\\final\\output\\yxhtest2tf.pb', "rb") as f:
            output_graph_def.ParseFromString(f.read()) #rb
            _ = tf.import_graph_def(output_graph_def, name="")
 
        with tf.Session() as sess:
            tf.global_variables_initializer().run()
            input_x = sess.graph.get_tensor_by_name("input:0")
            print(input_x)
            out_softmax = sess.graph.get_tensor_by_name("out_softmax:0")
            print(out_softmax)
            
            for i in range(len(pth)):
                try:
                    img = io.imread(pth[i])
                    img = transform.resize(img, (208, 208, 3))
                except Exception:
                    print(pth[i])
                else:
                    img_out_softmax = sess.run(out_softmax, feed_dict={
                        input_x: np.reshape(img,[-1, 208, 208, 3]),})
                    prediction_labels = np.argmax(img_out_softmax, axis=1)
                    if img_out_softmax[0][prediction_labels[0]] > 0.6:
                        labels.append(prediction_labels[0])
                    else:
                        labels.append(10)
    return labels

app = QtWidgets.QApplication(sys.argv)    
    
mymain = windowOne()
myshowpic = windowTwo()
mymain.show()
    
sys.exit(app.exec())
