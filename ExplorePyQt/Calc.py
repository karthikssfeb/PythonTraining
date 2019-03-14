from PyQt5.QtCore import QDate,QTime,QDateTime, Qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMainWindow, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont 
from calcUI import Ui_Form
import re, string, os
import traceback

class calcWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.expr = ''
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon(os.path.abspath('Calc.ico'))) 
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def setOperations(self):
        self.ui.num1.clicked.connect(self.updateDisplay)
        self.ui.num2.clicked.connect(self.updateDisplay)
        self.ui.num3.clicked.connect(self.updateDisplay)
        self.ui.num4.clicked.connect(self.updateDisplay)
        self.ui.num5.clicked.connect(self.updateDisplay)
        self.ui.num6.clicked.connect(self.updateDisplay)
        self.ui.num7.clicked.connect(self.updateDisplay)
        self.ui.num8.clicked.connect(self.updateDisplay)
        self.ui.num9.clicked.connect(self.updateDisplay)
        self.ui.num0.clicked.connect(self.updateDisplay)
        self.ui.addButton.clicked.connect(self.updateDisplay)
        self.ui.subtractButton.clicked.connect(self.updateDisplay)
        self.ui.multiplyButton.clicked.connect(self.updateDisplay)
        self.ui.divideButton.clicked.connect(self.updateDisplay)
        self.ui.moduloButton.clicked.connect(self.updateDisplay)
        self.ui.equalButton.clicked.connect(self.findexpr)
        self.ui.decimalButton.clicked.connect(self.updateDisplay)
        self.ui.reciprocalButton.clicked.connect(self.reciprocal)
        self.ui.clearButton.clicked.connect(self.clear)

    def updateDisplay(self): 
        
        '''isOnlyNums = re.compile('^[0-9]+$').search
        if isOnlyNums(self.ui.display.text())
            self.ui.display.setText('')
        else:'''
        sender = self.sender()
        self.ui.display.setText(self.ui.display.text() + sender.text())
        #print (self.ui.display.text() + '1')
    
    def findexpr(self):
        self.expr = self.ui.display.text()
        if  re.search('[\+\-\*/%]+$',self.expr):
            stripIndex = re.search('[\+\-\*/%]+$',self.expr).span()[0]
            self.expr = self.expr[:stripIndex]
        self.ui.display.setText(str (eval(self.expr)))
        
    def reciprocal(self):
        self.ui.display.setText('1/('+self.ui.display.text()+')')

    def clear(self):
        self.ui.display.setText('')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes | 
                                    QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 
        

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = calcWindow()
        window.setToolTip('This is a Calculator')
        window.setWindowTitle('Calculator')
        window.setOperations()
        
        window.show()
        
        sys.exit(app.exec_())

    except Exception as error:
        tb = traceback.format_exc()
        print ("There was an error: " + tb + "Close?")
        msgbox = QMessageBox.question(window, 'Message', "There was an error: " + tb + "Close?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes )
        if msgbox == QMessageBox.Yes:
            window.close()
        else:
            pass
