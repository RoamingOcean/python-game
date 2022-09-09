import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from inventory_frame import inventory_management_ui

class inventory_management(QMainWindow, inventory_management_ui):
    def __init__(self, parent=None):
        super(inventory_management, self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.add_button.clicked.connect(self.add_item)
        self.remove_button.clicked.connect(self.remove_item)
        self.edit_item.clicked.connect(self.edit_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    inventory_management = inventory_management()
    inventory_management.show()
    sys.exit(app.exec_())       
