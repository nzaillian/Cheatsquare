# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created: Thu Jul 29 19:23:25 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Login_Form(object):
    def setupUi(self, Login_Form):
        Login_Form.setObjectName("Login_Form")
        Login_Form.resize(350, 340)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Login_Form.sizePolicy().hasHeightForWidth())
        Login_Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Login_Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtGui.QGroupBox(Login_Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.remember_username_checkbox = QtGui.QCheckBox(self.groupBox_2)
        self.remember_username_checkbox.setObjectName("remember_username_checkbox")
        self.verticalLayout.addWidget(self.remember_username_checkbox)
        self.remember_password_checkbox = QtGui.QCheckBox(self.groupBox_2)
        self.remember_password_checkbox.setObjectName("remember_password_checkbox")
        self.verticalLayout.addWidget(self.remember_password_checkbox)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.login_button = QtGui.QPushButton(Login_Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.login_button.setAutoFillBackground(False)
        self.login_button.setObjectName("login_button")
        self.gridLayout.addWidget(self.login_button, 4, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Login_Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.username_field = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_field.sizePolicy().hasHeightForWidth())
        self.username_field.setSizePolicy(sizePolicy)
        self.username_field.setObjectName("username_field")
        self.verticalLayout_2.addWidget(self.username_field)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.password_field = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_field.sizePolicy().hasHeightForWidth())
        self.password_field.setSizePolicy(sizePolicy)
        self.password_field.setObjectName("password_field")
        self.verticalLayout_2.addWidget(self.password_field)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)

        self.retranslateUi(Login_Form)
        QtCore.QMetaObject.connectSlotsByName(Login_Form)

    def retranslateUi(self, Login_Form):
        Login_Form.setWindowTitle(QtGui.QApplication.translate("Login_Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Login_Form", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.remember_username_checkbox.setText(QtGui.QApplication.translate("Login_Form", "  Remember username?", None, QtGui.QApplication.UnicodeUTF8))
        self.remember_password_checkbox.setText(QtGui.QApplication.translate("Login_Form", "  Remember Password?", None, QtGui.QApplication.UnicodeUTF8))
        self.login_button.setText(QtGui.QApplication.translate("Login_Form", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Login_Form", "Credentials", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Login_Form", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Login_Form", "Password:", None, QtGui.QApplication.UnicodeUTF8))

