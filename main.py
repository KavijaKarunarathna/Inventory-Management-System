from interface import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
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
		if tablename == 'products':
			content = self.database.execute("SELECT * FROM products")
			return content

		if tablename == 'transhistory':
			content = self.database.execute("SELECT * FROM transhistory")
			return content

		if tablename == 'stockhistory':
			content = self.database.execute("SELECT * FROM stockhistory")
			return content

	def insert_data(self, event: str, content: list):
		if event == "insertSales":
			# update the products by reducing quantity

			# update transHistoryTbl including the relevant transaction 

			pass

		if event == "insertProducts":
			# update the products by increasing quantity

			# update productsHistoryTable including the relevant information
			pass
	

def main():
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	
	# creating database
	inventory = Database()

	def insert_data_to_table(tableObj, tablename: str):
		content = inventory.load_data(tablename)
		tableObj.setRowCount(0)
		for row_number,row_data in enumerate(content):
			tableObj.insertRow(row_number)
			for column_number, data in enumerate(row_data):
				tableObj.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))

	def updateStock():
		date = datetime.datetime.now().strftime("%x")
		id_ = ui.stockItemId.text()
		quantity = ui.stockItemQuantity.text()
		inventory.database.execute("INSERT INTO stockhistory VALUES(?, ?, ?)", (id_, quantity, date))
		inQuan = inventory.database.execute("SELECT quantity FROM products WHERE id = ?",(id_,))
		inQuan = int(inQuan) + int(quantity)
		inventory.database.execute("UPDATE products SET quantity = ? WHERE id = ?",(inQuan, id_))
		inventory.database.commit()

	def addItem():
		id_ = int(ui.newItemId.text())
		price = int(ui.newItemPrice.text())
		desc = ui.newItemDesc.text()
		inventory.database.execute("INSERT INTO products VALUES(?, ?, ?, ?)", (id_, desc, price, 0))
		inventory.database.commit()
	# run functions relevant to particular page
	def run_dash():
		ui.stackedWidget.setCurrentIndex(3)
		

	def run_items():
		ui.stackedWidget.setCurrentIndex(1)
		insert_data_to_table(ui.productTbl, 'products')
		ui.stockItemUpdateBtn.clicked.connect(updateStock)
		ui.newItemSaveBtn.clicked.connect(addItem)

	def run_sales():
		ui.stackedWidget.setCurrentIndex(2)

	def run_history():
		ui.stackedWidget.setCurrentIndex(0)
		ui.transHistoryBtn.clicked.connect(lambda: ui.stackedHistory.setCurrentIndex(1))
		ui.productHistoryBtn.clicked.connect(lambda: insert_data_to_table(ui.productHistoryTbl, 'stockhistory'))	
		ui.productHistoryBtn.clicked.connect(lambda: insert_data_to_table(ui.transHistoryTbl, 'transhistory'))

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

main()