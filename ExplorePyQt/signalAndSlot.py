from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class PunchingBag(QObject):
    punched = pyqtSignal()
    updated = pyqtSignal(int)


    def __init__(self):
        QObject.__init__(self)
        self.__count = 0

    
    def punch(self):
        self.punched.emit()

    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, inCount):
        self.__count = inCount
        self.updated.emit(inCount)



    
@pyqtSlot()
def say_punched():
    print ('Bag was punched')

@pyqtSlot()
def say_updated(updatedCount):
    #print("testupdate")
    if updatedCount > 5:
        print ('Bag was updated')

bag = PunchingBag()
bag.punched.connect(say_punched)
bag.updated.connect(say_updated)

for i in range (10):
    bag.punch()
    bag.count = i
    print (bag.count)