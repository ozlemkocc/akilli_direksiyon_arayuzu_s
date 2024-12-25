import sys
from PyQt5.QtGui import QMovie, QMouseEvent, QPixmap, QFont
import typing
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, Qt, QThread , pyqtSignal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from interface import Ui_MainWindow
import serial

class WorkerThread(QThread):
    resultReady = pyqtSignal(dict)

    def __init__(self):
        super().__init__()   
        self.ser = serial.Serial('/dev/ttyUSB0', 115200)
        self.is_running = True
        self.data = []
    def run(self):
        print(1)
        try:
            data = self.ser.read()
            print(f"WorkerThread data: {data}")
            result_data = {'data': data}
            self.resultReady.emit(result_data)
        except Exception as a:
            raise a

    def stop(self):
        #fself.master.__del__()
        pass
    def get_master(self):
        return self.ser   
    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_red = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.toggle_background)
        self.timer.start(500)  # 0.5 saniyede bir arka planı değiştir
        self.worker_thread = WorkerThread()
        self.worker_thread.resultReady.connect(self.control)
        self.worker_thread.start()
    def toggle_background(self):
        # Arka plan rengini kırmızıya değiştir veya temizle
        if self.is_red:
            self.ui.warning_widget.setStyleSheet("background-color: none;")
        else:
            self.ui.warning_widget.setStyleSheet("background-color: red;")
        self.is_red = not self.is_red

    def control(self, data):
        print(data)

    def closeEvent(self, event):
        # Uygulama kapatılırken thread'i durdur
        self.worker_thread.stop()
        self.worker_thread.wait()
        event.accept()