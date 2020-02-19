from PyQt5 import QtWidgets,QtCore
import sys
import ui_main
import numpy as np
import pylab
import time

class ExampleApp(QtWidgets.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.update)
        #self.matplotlibwidget.axes.hold(False) #clear on plot()
        #^ deprecated. need to call axes.clear() where required instead (at start of update?)
    def update(self):
        t1=time.time()
        points=100 #number of data points
        X=np.arange(points)
        Y=np.sin(np.arange(points)/points*3*np.pi+time.time())
        C=pylab.cm.jet(time.time()%10/10) # random color
        self.matplotlibwidget.axes.clear()
        self.matplotlibwidget.axes.plot(X,Y,ms=100,color=C,lw=10,alpha=.8)
        self.matplotlibwidget.axes.grid()
        self.matplotlibwidget.axes.get_figure().tight_layout() # fill space
        self.matplotlibwidget.draw() # required to update the window
        print("update took %.02f ms"%((time.time()-t1)*1000))
        if self.chkMore.isChecked():
            QtCore.QTimer.singleShot(10, self.update) # QUICKLY repeat

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update() #start with something
    app.exec_()
    print("DONE")