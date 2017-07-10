#!/usr/bin/env python

from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QAction, qApp, QMenu, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.createMenus()

    def initUI(self):
        self.resize(950, 500)
        self.center()  # Centro la pantalla

        self.setWindowTitle('Aplicacion')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def funcion(self):
        pass

    def createActions(self):
        self.newAct = QAction("&New", self, shortcut=QKeySequence.New,
                              statusTip="Create a new file", triggered=self.newFile)

        self.openAct = QAction("&Open...", self, shortcut=QKeySequence.Open,
                               statusTip="Open an existing file", triggered=self.open)

        self.saveAct = QAction("&Save", self, shortcut=QKeySequence.Save,
                               statusTip="Save the document to disk", triggered=self.save)

        self.printAct = QAction("&Print...", self, shortcut=QKeySequence.Print,
                                statusTip="Print the document", triggered=self.print_)

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                               statusTip="Exit the application", triggered=self.close)

        self.undoAct = QAction("&Undo", self, shortcut=QKeySequence.Undo,
                               statusTip="Undo the last operation", triggered=self.undo)

        self.redoAct = QAction("&Redo", self, shortcut=QKeySequence.Redo,
                               statusTip="Redo the last operation", triggered=self.redo)

        self.cutAct = QAction("Cu&t", self, shortcut=QKeySequence.Cut,
                              statusTip="Cut the current selection's contents to the clipboard",
                              triggered=self.cut)

        self.copyAct = QAction("&Copy", self, shortcut=QKeySequence.Copy,
                               statusTip="Copy the current selection's contents to the clipboard",
                               triggered=self.copy)

        self.pasteAct = QAction("&Paste", self, shortcut=QKeySequence.Paste,
                                statusTip="Paste the clipboard's contents into the current selection",
                                triggered=self.paste)

        self.boldAct = QAction("&Bold", self, checkable=True,
                               shortcut="Ctrl+B", statusTip="Make the text bold",
                               triggered=self.bold)



    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.funcion())
        self.fileMenu.addAction(self.funcion())
        self.fileMenu.addAction(self.funcion())
        self.fileMenu.addAction(self.funcion())
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.funcion())

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.funcion())
        self.editMenu.addAction(self.funcion())
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.funcion())
        self.editMenu.addAction(self.funcion())
        self.editMenu.addAction(self.funcion())
        self.editMenu.addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.funcion())
        self.helpMenu.addAction(self.funcion())

        self.formatMenu = self.editMenu.addMenu("&Format")
        self.formatMenu.addAction(self.funcion())
        self.formatMenu.addAction(self.funcion())
        self.formatMenu.addSeparator().setText("Alignment")
        self.formatMenu.addAction(self.funcion())
        self.formatMenu.addAction(self.funcion())
        self.formatMenu.addAction(self.funcion())
        self.formatMenu.addAction(self.funcion())
        self.formatMenu.addSeparator()
        self.formatMenu.addAction(self.funcion())
        self.formatMenu.addAction(self.funcion())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
