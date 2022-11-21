import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}
        self.pushButton.clicked.connect(self.update)

    def update(self):
        self.w2 = MyWidget_2()
        self.w2.show()
        self.hide()


class MyWidget_2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.insert)
        self.pushButton.clicked.connect(self.update)
        self.pushButton.clicked.connect(self.back)

    def insert(self):
        cur = self.con.cursor()
        e1 = self.lineEdit.text()
        e2 = self.lineEdit_2.text()
        e3 = self.lineEdit_3.text()
        e4 = self.lineEdit_4.text()
        e5 = self.lineEdit_5.text()
        e6 = self.lineEdit_6.text()
        e7 = self.lineEdit_7.text()
        cur.execute("""INSERT INTO coffee(ID, название сорта, степень обжарки, молотый/в зернах, описание вкуса, 
        цена, объем упаковки гр) VALUES(?, ?, ?, ?, ?, ?, ?)""", (e1, e2, e3, e4, e5, e6, e7)).fetchall()
        self.con.commit()

    def update(self):
        cur = self.con.cursor()
        e8 = self.lineEdit_8.text()
        e9 = self.lineEdit_9.text()
        e10 = self.lineEdit_10.text()
        cur.execute("""UPDATE coffee SET ? = ? WHERE ID = ?""", (e9, e10, e8)).fetchall()
        self.con.commit()

    def back(self):
        ex.show()
        self.hide()
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())