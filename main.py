from interface import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3

class Database:

	def __init__(self):
		self.database= sqlite3.connect("inventory.sqlite")
		self.create_table()
		
	def create_table(self):
		# creating tables if they do not exist
		self.database.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY NOT NULL, description TEXT, price INTEGER NOT NULL, quantity INTEGER NOT NULL)")
		self.database.execute("CREATE TABLE IF NOT EXISTS transhistory(id INTEGER PRIMARY KEY NOT NULL, quantity INTEGER, client TEXT, date TEXT)")
		self.database.execute("CREATE TABLE IF NOT EXISTS stockhistory(id INTEGER PRIMARY KEY NOT NULL, quantity INTEGER, date TEXT)")

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


def main():
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	
	# creating database
	inventory = Database()

	# run functions relevant to particular page
	def run_dash():
		ui.stackedWidget.setCurrentIndex(3)
		

	def run_items():
		ui.stackedWidget.setCurrentIndex(1)
		itemContent = inventory.load_data('products')
		for row_number,row_data in enumerate(itemContent):
			ui.productTbl.insertRow(row_number)
			for column_number, data in enumerate(row_data):
				ui.productTbl.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))

	def run_sales():
		ui.stackedWidget.setCurrentIndex(2)
		

	def run_history():
		ui.stackedWidget.setCurrentIndex(0)
		

	# starting with the dashboard
	ui.stackedWidget.setCurrentIndex(3)
	run_dash() 

	# navbar button configuration
	ui.dashBtn.clicked.connect(run_dash)
	ui.itemsBtn.clicked.connect(run_items)
	ui.salesBtn.clicked.connect(run_sales)
	ui.historyBtn.clicked.connect(run_history)


	MainWindow.show()
	sys.exit(app.exec_())

main()