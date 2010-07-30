# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkin_form.ui'
#
# Created: Thu Jul 29 19:23:25 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Checkin_Form(object):
    def setupUi(self, Checkin_Form):
        Checkin_Form.setObjectName("Checkin_Form")
        Checkin_Form.resize(640, 480)
        self.gridLayout = QtGui.QGridLayout(Checkin_Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(Checkin_Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.recent_checkins_view = QtGui.QListWidget(self.groupBox)
        self.recent_checkins_view.setObjectName("recent_checkins_view")
        self.gridLayout_2.addWidget(self.recent_checkins_view, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Checkin_Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.vid_field = QtGui.QLineEdit(self.groupBox_2)
        self.vid_field.setObjectName("vid_field")
        self.horizontalLayout.addWidget(self.vid_field)
        self.checkin_button = QtGui.QPushButton(self.groupBox_2)
        self.checkin_button.setObjectName("checkin_button")
        self.horizontalLayout.addWidget(self.checkin_button)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.retranslateUi(Checkin_Form)
        QtCore.QMetaObject.connectSlotsByName(Checkin_Form)

    def retranslateUi(self, Checkin_Form):
        Checkin_Form.setWindowTitle(QtGui.QApplication.translate("Checkin_Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Checkin_Form", "Recent Check-Ins", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Checkin_Form", "Check-In by VID", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Checkin_Form", "Enter VID:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkin_button.setText(QtGui.QApplication.translate("Checkin_Form", "Check-In", None, QtGui.QApplication.UnicodeUTF8))

