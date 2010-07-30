# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkin_complete_form.ui'
#
# Created: Thu Jul 29 19:23:25 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Checkin_Success_Form(object):
    def setupUi(self, Checkin_Success_Form):
        Checkin_Success_Form.setObjectName("Checkin_Success_Form")
        Checkin_Success_Form.resize(357, 210)
        Checkin_Success_Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout = QtGui.QGridLayout(Checkin_Success_Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(Checkin_Success_Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtGui.QFrame(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtGui.QFormLayout(self.frame_2)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.venue_name_label = QtGui.QLabel(self.frame_2)
        self.venue_name_label.setObjectName("venue_name_label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.venue_name_label)
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.venue_address_label = QtGui.QLabel(self.frame_2)
        self.venue_address_label.setObjectName("venue_address_label")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.venue_address_label)
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.checkin_date_label = QtGui.QLabel(self.frame_2)
        self.checkin_date_label.setObjectName("checkin_date_label")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkin_date_label)
        self.venue_icon_label = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(self.venue_icon_label.sizePolicy().hasHeightForWidth())
        self.venue_icon_label.setSizePolicy(sizePolicy)
        self.venue_icon_label.setObjectName("venue_icon_label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.venue_icon_label)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.ok_button = QtGui.QPushButton(Checkin_Success_Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 1, 0, 1, 1)

        self.retranslateUi(Checkin_Success_Form)
        QtCore.QMetaObject.connectSlotsByName(Checkin_Success_Form)

    def retranslateUi(self, Checkin_Success_Form):
        Checkin_Success_Form.setWindowTitle(QtGui.QApplication.translate("Checkin_Success_Form", "check-in complete!", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Checkin_Success_Form", "Success!  You have been checked into:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Checkin_Success_Form", "Venue:", None, QtGui.QApplication.UnicodeUTF8))
        self.venue_name_label.setText(QtGui.QApplication.translate("Checkin_Success_Form", "venue_name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Checkin_Success_Form", "Address:", None, QtGui.QApplication.UnicodeUTF8))
        self.venue_address_label.setText(QtGui.QApplication.translate("Checkin_Success_Form", "venue-addr", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Checkin_Success_Form", "date/time:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkin_date_label.setText(QtGui.QApplication.translate("Checkin_Success_Form", "date_time", None, QtGui.QApplication.UnicodeUTF8))
        self.venue_icon_label.setText(QtGui.QApplication.translate("Checkin_Success_Form", "ImageLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_button.setText(QtGui.QApplication.translate("Checkin_Success_Form", "OK", None, QtGui.QApplication.UnicodeUTF8))

