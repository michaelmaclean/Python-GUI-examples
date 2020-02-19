# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.chkMore = QtWidgets.QCheckBox(self.centralwidget)
        self.chkMore.setObjectName("chkMore")
        self.horizontalLayout.addWidget(self.chkMore)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.grPlot = PlotWidget(self.centralwidget)
        self.grPlot.setObjectName("grPlot")
        self.verticalLayout.addWidget(self.grPlot)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qt Graphey graph"))
        self.btnAdd.setText(_translate("MainWindow", "update sine wave"))
        self.chkMore.setText(_translate("MainWindow", "keep updating"))
        self.actionclose.setText(_translate("MainWindow", "closedsf"))

from pyqtgraph import PlotWidget
