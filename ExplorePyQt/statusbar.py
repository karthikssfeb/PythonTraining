import sys
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QApplication, QAction, QMenu, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
import os
from PyQt5.uic.Compiler.qtproxies import QtGui

class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab1,"Tab 1")
        self.tabs.addTab(self.tab2,"Tab 2")
        self.tabs.resize(300,200)
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.setLayout(self.tab1.layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    
    def contextMenuEvent(self, event):
       
        cmenu = QMenu(self)
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos())) 

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

                
    def initUI(self):   
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        exitAct = QAction(QIcon(os.path.abspath('Calc.ico')), '&Exit', self)
        #exitAct.setIcon(self,self,QIcon(os.path.abspath('Calc.ico')))
        print (exitAct.isIconVisibleInMenu())
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(QApplication.quit)   

     
        self.statusBar().showMessage('Ready')
        #self.statusBar().setVisible(False)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self) 
        impMenu.addAction(impAct)

        newAct = QAction('New', self)  

        viewMenu = menubar.addMenu('View')
        
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        #viewStatAct.setChecked(True)
        viewStatAct.toggled.connect(self.toggleMenu)
        viewStatAct.hovered.connect(self.hoverMenu)
        
        viewMenu.addAction(viewStatAct)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        self.show()
        
   

    def hoverMenu(self):
        #print ("hovered")
        pass
    
    def toggleMenu(self, state):
        
        if state:
            self.statusBar().show()
            print ('yes')
        else:
            self.statusBar().hide()
            


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())