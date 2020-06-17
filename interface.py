from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 625)
        MainWindow.setStyleSheet("background:white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 201, 811))
        self.frame.setStyleSheet("background:#212F3D;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.dashBtn = QtWidgets.QPushButton(self.frame)
        self.dashBtn.setGeometry(QtCore.QRect(-10, 80, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dashBtn.setFont(font)
        self.dashBtn.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    border:0;\n"
"    text-align:left;\n"
"    padding-left:20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#117864;\n"
"    \n"
"}\n"
"")
        self.dashBtn.setObjectName("dashBtn")
        self.itemsBtn = QtWidgets.QPushButton(self.frame)
        self.itemsBtn.setGeometry(QtCore.QRect(0, 140, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.itemsBtn.setFont(font)
        self.itemsBtn.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    border:0;\n"
"    text-align:left;\n"
"    padding-left:20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#117864;\n"
"    \n"
"}\n"
"")
        self.itemsBtn.setObjectName("itemsBtn")
        self.salesBtn = QtWidgets.QPushButton(self.frame)
        self.salesBtn.setGeometry(QtCore.QRect(0, 200, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.salesBtn.setFont(font)
        self.salesBtn.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    border:0;\n"
"    text-align:left;\n"
"    padding-left:20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#117864;\n"
"    \n"
"}\n"
"")
        self.salesBtn.setObjectName("salesBtn")
        self.historyBtn = QtWidgets.QPushButton(self.frame)
        self.historyBtn.setGeometry(QtCore.QRect(0, 260, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.historyBtn.setFont(font)
        self.historyBtn.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    border:0;\n"
"    text-align:left;\n"
"    padding-left:20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#117864;\n"
"    \n"
"}\n"
"")
        self.historyBtn.setObjectName("historyBtn")
        self.companyLogo = QtWidgets.QLabel(self.frame)
        self.companyLogo.setGeometry(QtCore.QRect(0, 0, 201, 51))
        self.companyLogo.setText("")
        self.companyLogo.setPixmap(QtGui.QPixmap("images/logo.PNG"))
        self.companyLogo.setScaledContents(True)
        self.companyLogo.setObjectName("companyLogo")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 50, 931, 741))
        self.stackedWidget.setStyleSheet("background:#D0D3D4 ;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.historyPage = QtWidgets.QWidget()
        self.historyPage.setObjectName("historyPage")
        self.stackedHistory = QtWidgets.QStackedWidget(self.historyPage)
        self.stackedHistory.setGeometry(QtCore.QRect(0, 50, 741, 481))
        self.stackedHistory.setStyleSheet("background:#D0D3D4;")
        self.stackedHistory.setObjectName("stackedHistory")
        self.productHistory = QtWidgets.QWidget()
        self.productHistory.setObjectName("productHistory")
        self.productHistoryTbl = QtWidgets.QTableWidget(self.productHistory)
        self.productHistoryTbl.setGeometry(QtCore.QRect(30, 20, 551, 411))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(65)
        self.productHistoryTbl.setFont(font)
        self.productHistoryTbl.setStyleSheet("border:3px solid rgba(103,103,103,0.4); \n"
"background:#D2D9F8;\n"
"")
        self.productHistoryTbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.productHistoryTbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.productHistoryTbl.setShowGrid(True)
        self.productHistoryTbl.setGridStyle(QtCore.Qt.SolidLine)
        self.productHistoryTbl.setRowCount(0)
        self.productHistoryTbl.setColumnCount(3)
        self.productHistoryTbl.setObjectName("productHistoryTbl")
        item = QtWidgets.QTableWidgetItem()
        self.productHistoryTbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productHistoryTbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productHistoryTbl.setHorizontalHeaderItem(2, item)
        self.productHistoryTbl.horizontalHeader().setCascadingSectionResizes(False)
        self.productHistoryTbl.horizontalHeader().setDefaultSectionSize(180)
        self.stackedHistory.addWidget(self.productHistory)
        self.transHistory = QtWidgets.QWidget()
        self.transHistory.setObjectName("transHistory")
        self.transHistoryTbl = QtWidgets.QTableWidget(self.transHistory)
        self.transHistoryTbl.setGeometry(QtCore.QRect(30, 20, 551, 411))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(65)
        self.transHistoryTbl.setFont(font)
        self.transHistoryTbl.setStyleSheet("border:3px solid rgba(103,103,103,0.4); \n"
"background:#D2D9F8;\n"
"")
        self.transHistoryTbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.transHistoryTbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.transHistoryTbl.setGridStyle(QtCore.Qt.SolidLine)
        self.transHistoryTbl.setRowCount(0)
        self.transHistoryTbl.setColumnCount(4)
        self.transHistoryTbl.setObjectName("transHistoryTbl")
        item = QtWidgets.QTableWidgetItem()
        self.transHistoryTbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.transHistoryTbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.transHistoryTbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.transHistoryTbl.setHorizontalHeaderItem(3, item)
        self.transHistoryTbl.horizontalHeader().setDefaultSectionSize(180)
        self.stackedHistory.addWidget(self.transHistory)
        self.productHistoryBtn = QtWidgets.QPushButton(self.historyPage)
        self.productHistoryBtn.setGeometry(QtCore.QRect(0, 0, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.productHistoryBtn.setFont(font)
        self.productHistoryBtn.setStyleSheet("QPushButton{\n"
"color:white; background:#1F618D;border:0;padding-left:5px;border-right:7px solid rgba(100, 97, 141);\n"
"}\n"
"QPushButton:hover{\n"
"        border-right:7px solid rgba(50, 97, 141);\n"
"        background:7px solid rgba(100, 97, 141, 0.6);\n"
"}")
        self.productHistoryBtn.setObjectName("productHistoryBtn")
        self.transHistoryBtn = QtWidgets.QPushButton(self.historyPage)
        self.transHistoryBtn.setGeometry(QtCore.QRect(180, 0, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.transHistoryBtn.setFont(font)
        self.transHistoryBtn.setStyleSheet("QPushButton{\n"
"color:white; background:#1F618D;border:0;padding-left:5px;\n"
"}\n"
"QPushButton:hover{\n"
"        background:7px solid rgba(100, 97, 141, 0.6);\n"
"}")
        self.transHistoryBtn.setObjectName("transHistoryBtn")
        self.stackedWidget.addWidget(self.historyPage)
        self.itemsPage = QtWidgets.QWidget()
        self.itemsPage.setObjectName("itemsPage")
        self.label_8 = QtWidgets.QLabel(self.itemsPage)
        self.label_8.setGeometry(QtCore.QRect(30, 390, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#494B51; padding:5px;")
        self.label_8.setObjectName("label_8")
        self.newItemId = QtWidgets.QLineEdit(self.itemsPage)
        self.newItemId.setGeometry(QtCore.QRect(140, 430, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newItemId.setFont(font)
        self.newItemId.setStyleSheet("border-radius:10px; border:1px solid gray;color:#273746;")
        self.newItemId.setObjectName("newItemId")
        self.label_9 = QtWidgets.QLabel(self.itemsPage)
        self.label_9.setGeometry(QtCore.QRect(50, 420, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:#494B51")
        self.label_9.setObjectName("label_9")
        self.newItemDesc = QtWidgets.QLineEdit(self.itemsPage)
        self.newItemDesc.setGeometry(QtCore.QRect(450, 430, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newItemDesc.setFont(font)
        self.newItemDesc.setStyleSheet("border-radius:10px; border:1px solid gray;color:#273746;")
        self.newItemDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.newItemDesc.setObjectName("newItemDesc")
        self.label_10 = QtWidgets.QLabel(self.itemsPage)
        self.label_10.setGeometry(QtCore.QRect(310, 430, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:#494B51")
        self.label_10.setObjectName("label_10")
        self.newItemSaveBtn = QtWidgets.QPushButton(self.itemsPage)
        self.newItemSaveBtn.setGeometry(QtCore.QRect(600, 500, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.newItemSaveBtn.setFont(font)
        self.newItemSaveBtn.setStyleSheet("QPushButton{\n"
"     border-radius:15px;\n"
"    background:#5D6D7E;\n"
"    color:white;\n"
"     transition-duration:200ms;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#1695F3;\n"
"    \n"
"}")
        self.newItemSaveBtn.setObjectName("newItemSaveBtn")
        self.label_11 = QtWidgets.QLabel(self.itemsPage)
        self.label_11.setGeometry(QtCore.QRect(30, 280, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:#494B51; padding:5px;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.itemsPage)
        self.label_12.setGeometry(QtCore.QRect(50, 310, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:#494B51")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.itemsPage)
        self.label_13.setGeometry(QtCore.QRect(240, 310, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:#494B51")
        self.label_13.setObjectName("label_13")
        self.stockItemId = QtWidgets.QLineEdit(self.itemsPage)
        self.stockItemId.setGeometry(QtCore.QRect(130, 320, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stockItemId.setFont(font)
        self.stockItemId.setStyleSheet("border-radius:10px; border:1px solid gray;color:#273746;")
        self.stockItemId.setObjectName("stockItemId")
        self.stockItemQuantity = QtWidgets.QLineEdit(self.itemsPage)
        self.stockItemQuantity.setGeometry(QtCore.QRect(350, 320, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stockItemQuantity.setFont(font)
        self.stockItemQuantity.setStyleSheet("border-radius:10px; border:1px solid gray;color:#273746;")
        self.stockItemQuantity.setObjectName("stockItemQuantity")
        self.stockItemUpdateBtn = QtWidgets.QPushButton(self.itemsPage)
        self.stockItemUpdateBtn.setGeometry(QtCore.QRect(480, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stockItemUpdateBtn.setFont(font)
        self.stockItemUpdateBtn.setStyleSheet("QPushButton{\n"
"     border-radius:15px;\n"
"    background:#5D6D7E;\n"
"    color:white;\n"
"     transition-duration:200ms;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#1695F3;\n"
"    \n"
"}")
        self.stockItemUpdateBtn.setObjectName("stockItemUpdateBtn")
        self.productTbl = QtWidgets.QTableWidget(self.itemsPage)
        self.productTbl.setGeometry(QtCore.QRect(40, 10, 661, 271))
        self.productTbl.setStyleSheet("border:3px solid #ABB0B5; \n"
"background:#BEC5CD;\n"
"")
        self.productTbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(65)
        self.productTbl.setFont(font)
        self.productTbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.productTbl.setGridStyle(QtCore.Qt.SolidLine)
        self.productTbl.setRowCount(0)
        self.productTbl.setColumnCount(4)
        self.productTbl.setObjectName("productTbl")
        item = QtWidgets.QTableWidgetItem()
        self.productTbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTbl.setHorizontalHeaderItem(3, item)
        self.productTbl.horizontalHeader().setDefaultSectionSize(180)
        self.label_14 = QtWidgets.QLabel(self.itemsPage)
        self.label_14.setGeometry(QtCore.QRect(60, 470, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:#494B51")
        self.label_14.setObjectName("label_14")
        self.newItemPrice = QtWidgets.QLineEdit(self.itemsPage)
        self.newItemPrice.setGeometry(QtCore.QRect(140, 480, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newItemPrice.setFont(font)
        self.newItemPrice.setStyleSheet("border-radius:10px; border:1px solid gray;color:#273746;")
        self.newItemPrice.setObjectName("newItemPrice")
        self.stackedWidget.addWidget(self.itemsPage)
        self.salesPage = QtWidgets.QWidget()
        self.salesPage.setObjectName("salesPage")
        self.label_15 = QtWidgets.QLabel(self.salesPage)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 271, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:#494B51; padding:5px;")
        self.label_15.setObjectName("label_15")
        self.clientName = QtWidgets.QLineEdit(self.salesPage)
        self.clientName.setGeometry(QtCore.QRect(150, 110, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clientName.setFont(font)
        self.clientName.setStyleSheet("border-radius:10px; border:1px solid gray;color:#273746;")
        self.clientName.setText("")
        self.clientName.setObjectName("clientName")
        self.savePurchaseBtn = QtWidgets.QPushButton(self.salesPage)
        self.savePurchaseBtn.setGeometry(QtCore.QRect(310, 380, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.savePurchaseBtn.setFont(font)
        self.savePurchaseBtn.setStyleSheet("QPushButton{\n"
"     border-radius:15px;\n"
"    background:#5D6D7E;\n"
"    color:white;\n"
"     transition-duration:200ms;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#1695F3;\n"
"    \n"
"}")
        self.savePurchaseBtn.setObjectName("savePurchaseBtn")
        self.label_16 = QtWidgets.QLabel(self.salesPage)
        self.label_16.setGeometry(QtCore.QRect(30, 180, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:#494B51; padding:5px;")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.salesPage)
        self.label_17.setGeometry(QtCore.QRect(30, 270, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:#494B51; padding:5px;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.salesPage)
        self.label_18.setGeometry(QtCore.QRect(30, 90, 111, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:#494B51; padding:5px;")
        self.label_18.setObjectName("label_18")
        self.purchaseId = QtWidgets.QLineEdit(self.salesPage)
        self.purchaseId.setGeometry(QtCore.QRect(170, 200, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.purchaseId.setFont(font)
        self.purchaseId.setStyleSheet("border-radius:10px; border:1px solid gray;color:#273746;")
        self.purchaseId.setObjectName("purchaseId")
        self.purchaseQuantity = QtWidgets.QLineEdit(self.salesPage)
        self.purchaseQuantity.setGeometry(QtCore.QRect(170, 290, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.purchaseQuantity.setFont(font)
        self.purchaseQuantity.setStyleSheet("border-radius:10px; border:1px solid gray;color:#273746;")
        self.purchaseQuantity.setObjectName("purchaseQuantity")
        self.stackedWidget.addWidget(self.salesPage)
        self.dashPage = QtWidgets.QWidget()
        self.dashPage.setObjectName("dashPage")
        self.label = QtWidgets.QLabel(self.dashPage)
        self.label.setGeometry(QtCore.QRect(40, 30, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#494B51; padding:5px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dashPage)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 231, 161))
        self.label_2.setStyleSheet("QLabel{\n"
"border:1px solid #494B51;\n"
"border-radius:10px;\n"
"}\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.dashPage)
        self.label_3.setGeometry(QtCore.QRect(430, 100, 231, 161))
        self.label_3.setStyleSheet("border:1px solid #494B51;\n"
"border-radius:10px;")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.numberOfItems = QtWidgets.QLabel(self.dashPage)
        self.numberOfItems.setGeometry(QtCore.QRect(150, 130, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.numberOfItems.setFont(font)
        self.numberOfItems.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.numberOfItems.setStyleSheet("QLabel{\n"
"border:0px solid #494B51;\n"
"border-radius:10px;\n"
"color:#9F2352;\n"
"}\n"
"QLabel:hover {\n"
"    background:#C8ADCF;\n"
"    color:#FFF;\n"
"}\n"
"")
        self.numberOfItems.setAlignment(QtCore.Qt.AlignCenter)
        self.numberOfItems.setObjectName("numberOfItems")
        self.numberOfOutStock = QtWidgets.QLabel(self.dashPage)
        self.numberOfOutStock.setGeometry(QtCore.QRect(480, 130, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.numberOfOutStock.setFont(font)
        self.numberOfOutStock.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.numberOfOutStock.setStyleSheet("QLabel{\n"
"border:0px solid #494B51;\n"
"border-radius:10px;\n"
"color:#2A6DB2;\n"
"}\n"
"QLabel:hover {\n"
"    background:#C8ADCF;\n"
"    color:#FFF;\n"
"}\n"
"")
        self.numberOfOutStock.setAlignment(QtCore.Qt.AlignCenter)
        self.numberOfOutStock.setObjectName("numberOfOutStock")
        self.label_6 = QtWidgets.QLabel(self.dashPage)
        self.label_6.setGeometry(QtCore.QRect(120, 220, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{color:#494B51;}\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.dashPage)
        self.label_7.setGeometry(QtCore.QRect(460, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#494B51;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.dashPage)
        self.label_4.setGeometry(QtCore.QRect(100, 330, 231, 161))
        self.label_4.setStyleSheet("QLabel{\n"
"border:1px solid #494B51;\n"
"border-radius:10px;\n"
"}\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.monthlySales = QtWidgets.QLabel(self.dashPage)
        self.monthlySales.setGeometry(QtCore.QRect(150, 350, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.monthlySales.setFont(font)
        self.monthlySales.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.monthlySales.setStyleSheet("QLabel{\n"
"border:0px solid #494B51;\n"
"border-radius:10px;\n"
"color:#D29600;\n"
"}\n"
"QLabel:hover {\n"
"    background:#C8ADCF;\n"
"    color:#FFF;\n"
"}\n"
"")
        self.monthlySales.setAlignment(QtCore.Qt.AlignCenter)
        self.monthlySales.setObjectName("monthlySales")
        self.label_19 = QtWidgets.QLabel(self.dashPage)
        self.label_19.setGeometry(QtCore.QRect(120, 440, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("QLabel{color:#494B51;}\n"
"")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_5 = QtWidgets.QLabel(self.dashPage)
        self.label_5.setGeometry(QtCore.QRect(430, 330, 231, 161))
        self.label_5.setStyleSheet("QLabel{\n"
"border:1px solid #494B51;\n"
"border-radius:10px;\n"
"}\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.monthlyIncome = QtWidgets.QLabel(self.dashPage)
        self.monthlyIncome.setGeometry(QtCore.QRect(490, 350, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.monthlyIncome.setFont(font)
        self.monthlyIncome.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.monthlyIncome.setStyleSheet("QLabel{\n"
"border:0px solid #494B51;\n"
"border-radius:10px;\n"
"color:#268038;\n"
"}\n"
"QLabel:hover {\n"
"    background:#C8ADCF;\n"
"    color:#FFF;\n"
"}\n"
"")
        self.monthlyIncome.setAlignment(QtCore.Qt.AlignCenter)
        self.monthlyIncome.setObjectName("monthlyIncome")
        self.label_20 = QtWidgets.QLabel(self.dashPage)
        self.label_20.setGeometry(QtCore.QRect(440, 440, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("QLabel{color:#494B51;}\n"
"")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.stackedWidget.addWidget(self.dashPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("border:2px solid gray;\n"
"")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedHistory.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dashBtn.setText(_translate("MainWindow", " Dashboard"))
        self.itemsBtn.setText(_translate("MainWindow", "Items"))
        self.salesBtn.setText(_translate("MainWindow", "Sales"))
        self.historyBtn.setText(_translate("MainWindow", "History"))
        item = self.productHistoryTbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item_ID"))
        item = self.productHistoryTbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.productHistoryTbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        item = self.transHistoryTbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item_ID"))
        item = self.transHistoryTbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.transHistoryTbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Client"))
        item = self.transHistoryTbl.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        self.productHistoryBtn.setText(_translate("MainWindow", "PRODUCTION"))
        self.transHistoryBtn.setText(_translate("MainWindow", "TRANSACTIONS"))
        self.label_8.setText(_translate("MainWindow", "Add Item"))
        self.label_9.setText(_translate("MainWindow", "ITEM ID:"))
        self.label_10.setText(_translate("MainWindow", "DESCRIPTION:"))
        self.newItemSaveBtn.setText(_translate("MainWindow", "SAVE"))
        self.label_11.setText(_translate("MainWindow", "New Stock"))
        self.label_12.setText(_translate("MainWindow", "ITEM ID:"))
        self.label_13.setText(_translate("MainWindow", "QUANTITY:"))
        self.stockItemUpdateBtn.setText(_translate("MainWindow", "UPDATE"))
        item = self.productTbl.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.productTbl.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Description"))
        item = self.productTbl.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.productTbl.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        self.label_14.setText(_translate("MainWindow", "PRICE:"))
        self.label_15.setText(_translate("MainWindow", "Client Purchase"))
        self.savePurchaseBtn.setText(_translate("MainWindow", "SAVE"))
        self.label_16.setText(_translate("MainWindow", "Item ID:"))
        self.label_17.setText(_translate("MainWindow", "Quantity:"))
        self.label_18.setText(_translate("MainWindow", "Client:"))
        self.label.setText(_translate("MainWindow", "Sales Activity"))
        self.numberOfItems.setText(_translate("MainWindow", "10"))
        self.numberOfOutStock.setText(_translate("MainWindow", "10"))
        self.label_6.setText(_translate("MainWindow", "ITEMS"))
        self.label_7.setText(_translate("MainWindow", "OUT OF STOCK"))
        self.monthlySales.setText(_translate("MainWindow", "10"))
        self.label_19.setText(_translate("MainWindow", "MONTHLY SALES"))
        self.monthlyIncome.setText(_translate("MainWindow", "10"))
        self.label_20.setText(_translate("MainWindow", "MONTHLY INCOME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
