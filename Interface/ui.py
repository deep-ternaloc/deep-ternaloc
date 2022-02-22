# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacegpARet.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1276, 710)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.top_left_frame = QFrame(self.top_frame)
        self.top_left_frame.setObjectName(u"top_left_frame")
        self.top_left_frame.setMinimumSize(QSize(800, 0))
        self.top_left_frame.setMaximumSize(QSize(800, 466))
        self.top_left_frame.setFrameShape(QFrame.StyledPanel)
        self.top_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_left_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.graph_widget = QWidget(self.top_left_frame)
        self.graph_widget.setObjectName(u"graph_widget")

        self.horizontalLayout_2.addWidget(self.graph_widget)


        self.horizontalLayout.addWidget(self.top_left_frame)

        self.top_right_frame = QFrame(self.top_frame)
        self.top_right_frame.setObjectName(u"top_right_frame")
        self.top_right_frame.setFrameShape(QFrame.StyledPanel)
        self.top_right_frame.setFrameShadow(QFrame.Raised)
        self.connectbutton = QPushButton(self.top_right_frame)
        self.connectbutton.setObjectName(u"connectbutton")
        self.connectbutton.setGeometry(QRect(90, 80, 75, 23))

        self.horizontalLayout.addWidget(self.top_right_frame)


        self.verticalLayout.addWidget(self.top_frame)

        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 200))
        self.bottom_frame.setMaximumSize(QSize(16777215, 200))
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.bottom_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.connectbutton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
    # retranslateUi

