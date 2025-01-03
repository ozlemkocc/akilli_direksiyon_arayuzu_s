from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication
from functions import MainWindow

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

app = QApplication([])
pencere = MainWindow()
pencere.show()
app.exec_()

def closeEvent(self, event):
    self.worker_thread.stop()  # Döngüyü durdur
    self.worker_thread.wait()  # Thread'in tamamen kapanmasını bekle
    event.accept()