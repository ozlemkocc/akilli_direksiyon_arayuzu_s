
from functions import MainWindow
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
app = QApplication([])
pencere = MainWindow()
pencere.show()
app.exec_()
