from PySide2.QtWidgets import QMainWindow
from ui_tarea import Ui_MainWindow
from PySide2.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)