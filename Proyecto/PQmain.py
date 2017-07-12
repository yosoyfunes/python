import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic



# python -m PyQt5.uic.pyuic -o Qmain.py main.ui


#class MyApplication(QMainWindow, Ui_MainWindow):
class MyApplication(QMainWindow):
	def __init__(self, parent=None):
#		super(MyApplication, self).__init__(parent)
		QMainWindow.__init__(self)
		uic.loadUi("layout/Qmain.ui", self)

		# Set up the user interface from Designer.
        self.ui = Ui_ImageDialog()
        self.ui.setupUi(self)

	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyApplication()
	window.show()
	sys.exit(app.exec_())