from interface import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import sqlite3
import datetime

class Database:

	def __init__(self):
		self.database= sqlite3.connect("inventory.sqlite")
		self.create_table()
		
	def create_table(self):
		# creating tables if they do not exist
		self.database.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER NOT NULL, description TEXT, price INTEGER NOT NULL, quantity INTEGER NOT NULL)")
		self.database.execute("CREATE TABLE IF NOT EXISTS transhistory(id INTEGER  NOT NULL, quantity INTEGER, client TEXT, date TEXT)")
		self.database.execute("CREATE TABLE IF NOT EXISTS stockhistory(id INTEGER  NOT NULL, quantity INTEGER, date TEXT)")

	def load_data(self, tablename: str):

		content = self.database.execute("SELECT * FROM "+tablename)
		return content


def main():
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	
	# creating database
	inventory = Database()
	cursor = inventory.database.cursor()

	def show_message(text):
		msg = QMessageBox()
		msg.setWindowTitle("Inventory Manager")
		msg.setText("     "+text+"     ")
		msg.setIcon(QMessageBox.Warning)
		x = msg.exec_()

	def insert_data_to_table(tableObj, tablename: str):
		content = inventory.load_data(tablename)
		tableObj.setRowCount(0)
		for row_number,row_data in enumerate(content):
			tableObj.insertRow(row_number)
			for column_number, data in enumerate(row_data):
				tableObj.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))

	def updateStock():
		try:
			if ui.stockItemId.text().isnumeric():
				date = datetime.datetime.now().strftime("%x")
				id_ = int(ui.stockItemId.text())
				quantity = int(ui.stockItemQuantity.text())
				inventory.database.execute("INSERT INTO stockhistory VALUES(?, ?, ?)", (id_, quantity, date))
				inQuan = cursor.execute("SELECT products.quantity FROM products WHERE products.id = ?",(id_,))
				inQuantity = inQuan.fetchone()
				inQuantity = inQuantity[0]
				inQuantity += quantity
				cursor.execute("UPDATE products SET quantity = ? WHERE id = ?",(inQuantity, id_))
				ui.stockItemId.setText("")
				ui.stockItemQuantity.setText("")
		except (ValueError, TypeError):
			show_message("Item ID is not registered.")

	def addItem():
		itemCursor= cursor.execute("SELECT products.id from products").fetchall()
		id_ = int(ui.newItemId.text())
		try:
			price = int(ui.newItemPrice.text())
		except ValueError:
			show_message("Price is numeric and cannot be empty.")
			return
		desc = ui.newItemDesc.text()
		item_list = []
		for item in itemCursor:
			item_list.append(item[0])
		if id_ not in item_list:
			if ui.newItemId.text().isnumeric():	
				try:				
					cursor.execute("INSERT INTO products VALUES(?, ?, ?, ?)", (id_, desc, price, 0))
					ui.newItemId.setText("")
					ui.newItemPrice.setText("")
					ui.newItemDesc.setText("")
				except ValueError:
					show_message("Price cannot be empty.")

		else:
			show_message("The Item ID already exists.")


	def updateTrans():
		date = datetime.datetime.now().strftime("%x")
		client = ui.clientName.text()
		try:
			id_ =  int(ui.purchaseId.text())
			quantity = int(ui.purchaseQuantity.text())
		except ValueError:
			show_message("Item ID and quantity must be numeric.")
			return
		itemCursor= cursor.execute("SELECT products.id from products").fetchall()
		item_list = []
		for item in itemCursor:
			item_list.append(item[0])
		if id_ in item_list:
			inventory.database.execute("INSERT INTO transhistory VALUES(?, ?, ?, ?)", (id_, quantity, client, date))
			inQuan = cursor.execute("SELECT products.quantity FROM products WHERE products.id = ?",(id_,))
			inQuantity = inQuan.fetchone()
			inQuantity = inQuantity[0]
			inQuantity -= quantity
			cursor.execute("UPDATE products SET quantity = ? WHERE id = ?",(inQuantity, id_))
			cursor.connection.commit()
		else:
			show_message("Item is not registered")
		ui.clientName.setText("")
		ui.purchaseId.setText("")
		ui.purchaseQuantity.setText("")



	# run functions relevant to particular page
	def run_dash():
		ui.stackedWidget.setCurrentIndex(3)
		

	def run_items():
		ui.stackedWidget.setCurrentIndex(1)
		insert_data_to_table(ui.productTbl, 'products')
		ui.stockItemUpdateBtn.clicked.connect(updateStock)
		ui.newItemSaveBtn.clicked.connect(addItem)
		cursor.connection.commit()

	def run_sales():
		ui.stackedWidget.setCurrentIndex(2)
		ui.savePurchaseBtn.clicked.connect(updateTrans)

	def run_history():

		def productHist():
			ui.stackedHistory.setCurrentIndex(0)
			insert_data_to_table(ui.productHistoryTbl, 'stockhistory')
			
		def transHist():
			ui.stackedHistory.setCurrentIndex(1)
			insert_data_to_table(ui.transHistoryTbl, 'transhistory')

		ui.stackedWidget.setCurrentIndex(0)
		productHist()
		ui.productHistoryBtn.clicked.connect(productHist)
		ui.transHistoryBtn.clicked.connect(transHist)

	# starting with the dashboard
	ui.stackedWidget.setCurrentIndex(3)
	insert_data_to_table(ui.productHistoryTbl, 'stockhistory')
	run_history()
	run_dash() 

	# navbar button configuration
	ui.dashBtn.clicked.connect(run_dash)
	ui.itemsBtn.clicked.connect(run_items)
	ui.salesBtn.clicked.connect(run_sales)
	ui.historyBtn.clicked.connect(run_history)


	MainWindow.show()
	sys.exit(app.exec_())
	inventory.database.close()

main()