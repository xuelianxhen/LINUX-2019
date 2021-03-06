# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query_pane.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(642, 405)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.query_pane_top = QtWidgets.QWidget(Form)
        self.query_pane_top.setStyleSheet("")
        self.query_pane_top.setObjectName("query_pane_top")
        self.gridLayout = QtWidgets.QGridLayout(self.query_pane_top)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.query_pane_top)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.from_station_cb = QtWidgets.QComboBox(self.query_pane_top)
        self.from_station_cb.setEditable(True)
        self.from_station_cb.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.from_station_cb.setObjectName("from_station_cb")
        self.gridLayout.addWidget(self.from_station_cb, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.query_pane_top)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.to_station_cb = QtWidgets.QComboBox(self.query_pane_top)
        self.to_station_cb.setEditable(True)
        self.to_station_cb.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.to_station_cb.setObjectName("to_station_cb")
        self.gridLayout.addWidget(self.to_station_cb, 0, 3, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.query_pane_top)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 5, 2, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.query_pane_top)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 6, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.query_pane_top)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.start_date_de = QtWidgets.QDateEdit(self.query_pane_top)
        self.start_date_de.setCalendarPopup(True)
        self.start_date_de.setObjectName("start_date_de")
        self.gridLayout.addWidget(self.start_date_de, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.query_pane_top)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.normal_cb = QtWidgets.QRadioButton(self.query_pane_top)
        self.normal_cb.setChecked(True)
        self.normal_cb.setObjectName("normal_cb")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.normal_cb)
        self.gridLayout.addWidget(self.normal_cb, 1, 3, 1, 1)
        self.stu_cb = QtWidgets.QRadioButton(self.query_pane_top)
        self.stu_cb.setObjectName("stu_cb")
        self.buttonGroup.addButton(self.stu_cb)
        self.gridLayout.addWidget(self.stu_cb, 1, 4, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setColumnStretch(6, 1)
        self.verticalLayout.addWidget(self.query_pane_top)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tickets_tv = QtWidgets.QTableView(self.widget_2)
        self.tickets_tv.setObjectName("tickets_tv")
        self.horizontalLayout.addWidget(self.tickets_tv)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.query_tickets)
        self.pushButton_2.clicked.connect(Form.book_tickets)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "出发地"))
        self.label_2.setText(_translate("Form", "目的地"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "抢票"))
        self.label_3.setText(_translate("Form", "出发日"))
        self.start_date_de.setDisplayFormat(_translate("Form", "yyyy-MM-dd"))
        self.label_4.setText(_translate("Form", "类型"))
        self.normal_cb.setText(_translate("Form", "普通"))
        self.normal_cb.setProperty("q_value", _translate("Form", "ADULT"))
        self.stu_cb.setText(_translate("Form", "学生"))
        self.stu_cb.setProperty("q_value", _translate("Form", "0X00"))

