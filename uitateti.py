# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tateti.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(310, 400)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(10, 10, 90, 90))
        
        font = QtGui.QFont()
        font.setPointSize(25)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(110, 10, 90, 90))
        
        font = QtGui.QFont()
        font.setPointSize(25)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(210, 10, 90, 90))
        
        font = QtGui.QFont()
        font.setPointSize(25)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(210, 110, 90, 90))
        
        font = QtGui.QFont()
        font.setPointSize(25)
        self.b6.setFont(font)
        self.b6.setAutoDefault(False)
        self.b6.setDefault(False)
        self.b6.setFlat(False)
        self.b6.setObjectName("b6")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(110, 110, 90, 90))
        
        font = QtGui.QFont()
        font.setPointSize(25)
        self.b5.setFont(font)
        self.b5.setObjectName("b5")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(10, 110, 90, 90))
        
        font = QtGui.QFont()
        font.setPointSize(25)
        self.b4.setFont(font)
        self.b4.setObjectName("b4")
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(210, 210, 90, 90))
        
        font = QtGui.QFont()
        font.setPointSize(25)
        self.b9.setFont(font)
        self.b9.setObjectName("b9")
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(110, 210, 90, 90))
        
        font = QtGui.QFont()
        font.setPointSize(25)
        self.b8.setFont(font)
        self.b8.setObjectName("b8")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(10, 210, 90, 90))
        
        font = QtGui.QFont()
        font.setPointSize(25)
        self.b7.setFont(font)
        self.b7.setObjectName("b7")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuReset = QtWidgets.QMenu(self.menubar)
        self.menuReset.setEnabled(True)
        self.menuReset.setObjectName("menuReset")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuReset.menuAction())

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "TATETI"))
        self.b1.setText(_translate("main", "1"))
        self.b2.setText(_translate("main", "2"))
        self.b3.setText(_translate("main", "3"))
        self.b6.setText(_translate("main", "6"))
        self.b5.setText(_translate("main", "5"))
        self.b4.setText(_translate("main", "4"))
        self.b9.setText(_translate("main", "9"))
        self.b8.setText(_translate("main", "8"))
        self.b7.setText(_translate("main", "7"))
        self.menuReset.setTitle(_translate("main", "Reset"))