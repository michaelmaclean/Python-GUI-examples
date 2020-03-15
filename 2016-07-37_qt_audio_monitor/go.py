from PyQt5 import QtGui,QtCore, QtWidgets

import sys
import ui_main
import numpy as np
import pyqtgraph
import SWHear
import time
import threading

class ExampleApp(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.grFFT.plotItem.showGrid(True, True, 0.7)
        self.grPCM.plotItem.showGrid(True, True, 0.7)
        self.maxFFT=0
        self.maxPCM=0
        self.ear = SWHear.SWHear(device=2,rate=44100,updatesPerSecond=20)
        self.btnStart.clicked.connect(self.start)
        self.btnStop.clicked.connect(self.stop)
        self.statusBar.showMessage('Message in statusbar.',2500)

    def start(self):
        #if valid connection, and not started, then
        self.ear.stream_start()

    def stop(self):
        #if valid connection, and not started, then
        self.ear.stream_stop()

    def tick(self):
        #time up - permanent widget in status bar with time connected!
        #put clock somewhere.
        #allow for linking other tasks - e.g. pacing summary etc.
        pass

    def sec_tick(self):
        """do stuff once per sec"""
        if self.keepRecording:
            self.tick=threading.Thread(target=self.sec_tick)
            self.tick.start()
            print(len(self.data))
            time.sleep(1)
        else:
            print(" -- tick STOPPED")

    def update(self):
        if not self.ear.data is None and not self.ear.fft is None:
            pcmMax=np.max(np.abs(self.ear.data))
            if pcmMax>self.maxPCM:
                self.maxPCM=pcmMax
                self.grPCM.plotItem.setRange(yRange=[-pcmMax,pcmMax])
            if np.max(self.ear.fft)>self.maxFFT:
                self.maxFFT=np.max(np.abs(self.ear.fft))
                #self.grFFT.plotItem.setRange(yRange=[0,self.maxFFT])
                self.grFFT.plotItem.setRange(yRange=[0,1])
            self.pbLevel.setValue(1000*pcmMax/self.maxPCM)
            pen=pyqtgraph.mkPen(color='b')
            self.grPCM.plot(self.ear.datax,self.ear.data,pen=pen,clear=True)
            pen=pyqtgraph.mkPen(color='r')
            self.grFFT.plot(self.ear.fftx,self.ear.fft/self.maxFFT,pen=pen,clear=True)
        QtCore.QTimer.singleShot(1, self.update) # QUICKLY repeat

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update() #start with something
    app.exec_()
    form.ear.close()
    print("DONE")
