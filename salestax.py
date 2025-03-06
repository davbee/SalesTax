# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file
# 'C:\Users\pihd\Documents\Programming\Python\SalesTax\SalesTax.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(40, 30, 231, 16))

        self.txtPurchase = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPurchase.setGeometry(QtCore.QRect(40, 100, 113, 20))
        self.txtPurchase.setObjectName("txtPurchase")

        self.txtSalesTaxRate = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSalesTaxRate.setGeometry(QtCore.QRect(40, 160, 113, 20))
        self.txtSalesTaxRate.setObjectName("txtSalesTaxRate")

        self.txtSalesTax = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSalesTax.setGeometry(QtCore.QRect(40, 220, 113, 20))
        self.txtSalesTax.setObjectName("txtSalesTax")

        self.txtTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTotal.setGeometry(QtCore.QRect(40, 280, 113, 20))
        self.txtTotal.setObjectName("txtTotal")

        self.labelPuchase = QtWidgets.QLabel(self.centralwidget)
        self.labelPuchase.setGeometry(QtCore.QRect(40, 80, 111, 16))
        self.labelPuchase.setObjectName("labelPuchase")

        self.labelSalesTaxRate = QtWidgets.QLabel(self.centralwidget)
        self.labelSalesTaxRate.setGeometry(QtCore.QRect(40, 140, 111, 16))
        self.labelSalesTaxRate.setObjectName("labelSalesTaxRate")

        self.labelSalesTax = QtWidgets.QLabel(self.centralwidget)
        self.labelSalesTax.setGeometry(QtCore.QRect(40, 200, 111, 16))
        self.labelSalesTax.setObjectName("labelSalesTax")

        self.labelTotalAmount = QtWidgets.QLabel(self.centralwidget)
        self.labelTotalAmount.setGeometry(QtCore.QRect(40, 260, 111, 16))
        self.labelTotalAmount.setObjectName("labelTotalAmount")

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.pB_Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.pB_Calculate.setGeometry(QtCore.QRect(40, 330, 111, 23))
        self.pB_Calculate.setObjectName("pB_Calculate")
        self.pTE_Message = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pTE_Message.setGeometry(QtCore.QRect(200, 100, 181, 201))
        self.pTE_Message.setObjectName("pTE_Message")
        self.labelMessage = QtWidgets.QLabel(self.centralwidget)
        self.labelMessage.setGeometry(QtCore.QRect(200, 80, 47, 13))
        self.labelMessage.setObjectName("labelMessage")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # above are QT Designer generated code
        # add customized section below
        self.pB_Calculate.clicked.connect(self.calculate_tax)
        # self.actionQuit.triggered.connect(self.Exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitle.setText(_translate(
            "MainWindow", "Sales Tax Calculation"))

        self.txtPurchase.setText(_translate("MainWindow", "100"))
        self.txtSalesTaxRate.setText(_translate("MainWindow", "9.00"))

        self.labelPuchase.setText(_translate("MainWindow", "Purchase, $"))
        self.labelSalesTaxRate.setText(_translate(
            "MainWindow", "Sales Tax Rate, %"))
        self.labelSalesTax.setText(_translate("MainWindow", "Sales Tax, $"))
        self.labelTotalAmount.setText(_translate(
            "MainWindow", "Total Amount, $"))
        self.labelMessage.setText(_translate("MainWindow", "Message"))

        self.pB_Calculate.setText(_translate("MainWindow", "Calculate"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))

    def calculate_tax(self):
        purchase = Decimal(self.txtPurchase.text())

        salesTaxRate = Decimal(self.txtSalesTaxRate.text()) / 100
        salesTax = purchase * salesTaxRate
        sSalesTax = f"{salesTax:.2f}"
        self.txtSalesTax.setText(sSalesTax)

        totalAmount = purchase + salesTax
        sTotalAmount = f"{totalAmount:.2f}"
        self.txtTotal.setText(sTotalAmount)

        sTotalAmountMessage = "The total amount due is $" + sTotalAmount + "."
        self.pTE_Message.setPlainText(sTotalAmountMessage)

    # def Exit(self):
    #     sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
