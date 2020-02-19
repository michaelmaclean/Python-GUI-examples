from PyQt5 import QtGui,QtCore, QtWidgets
import sys
import ui_main
import numpy as np
import pylab
import time
import pyqtgraph

class ExampleApp(QtWidgets.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.update)
        self.grPlot.plotItem.showGrid(True, True, 0.7)

    def update(self):
        t1=time.perf_counter()
        points=100 #number of data points
        X=np.arange(points)
        Y=np.sin(np.arange(points)/points*3*np.pi+time.time())
        C=pyqtgraph.hsvColor(t1%1,alpha=.5)
        pen=pyqtgraph.mkPen(color=C,width=10)
        self.grPlot.plot(X,Y,pen=pen,clear=True)
        print("update took %.02f ms"%((time.perf_counter()-t1)*1000))
        if self.chkMore.isChecked():
            QtCore.QTimer.singleShot(1, self.update) # QUICKLY repeat

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update() #start with something
    app.exec_()
    print("DONE")