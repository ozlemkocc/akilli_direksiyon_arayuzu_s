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
import pyttsx3
import random
import json
import time
import struct


class WorkerThread(QThread):
    resultReady = pyqtSignal(list)  # Ayrıştırılmış veriyi iletmek için sinyal
    def __init__(self):
        super().__init__()
        self.is_running = True  # Thread'in çalışmasını kontrol eden bayrak
        self.ser = serial.Serial('/dev/ttyUSB0', 115200)

    def run(self):
        if self.ser is None:
            print("Seri port açılmadı, veri okumaya başlanamaz.")
            return
    
        while self.is_running:
            try:
                while True:
                    data = self.ser.read(9) 
                    unpacked = list(struct.unpack('<ffB', data))
                    self.resultReady.emit(unpacked)
            except Exception as e:
                print(f"Veri okuma hatası: {e}")
            finally:
                if not self.is_running:
                    print("WorkerThread döngüsü sonlandırıldı.")

    def stop(self):
        self.is_running = False  # Döngüyü durdurmak için bayrağı güncelle

    def get_master(self):
        return self.ser  # Seri port nesnesini döndür



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
        self.temperature = 0
        self.BPM = 0
        self.cursorpos = 0
        self.figure = plt.Figure(figsize=(5, 3), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout(self.ui.nabz_widget)
        layout.addWidget(self.canvas)

        
        self.x_data = [] 
        self.y_data = [] 

        # Grafik çizim fonksiyonunu çağır
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Gerçek Zamanlı Veri Grafiği')
        self.ax.set_xlabel('Zaman (s)')
        self.ax.set_ylabel('Veri Değeri')
        self.ax.grid(True)

        # Timer ile verileri güncelle
        self.pulse_timer = QTimer(self)
        self.pulse_timer.timeout.connect(self.update_graph)
        self.pulse_timer.start(100)  # Her saniye veriyi güncelle

    def toggle_background(self):
        # Arka plan rengini kırmızıya değiştir veya temizle
        if self.is_red:
            self.ui.warnin_widget.setStyleSheet("background-color: none;")
        else:
            self.ui.warnin_widget.setStyleSheet("background-color: red;")
        self.is_red = not self.is_red

    def speak_warning(self, message):
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()
    
    def control(self, data):
        print(f"Alınan veri: {data}")  # Gelen veriyi kontrol et
        try:
            self.temperature = data[1] 
            self.BPM = data[2]
             # Veriyi float'a dönüştür
            print(self.temperature)  # Dönüştürülen veriyi yazdır
            self.ui.temperature_label.setText(f"Sıcaklık: {self.temperature:.1f} °C")
            if self.temperature > 38.0:
                print("Ateş yüksek!")
        except ValueError:
            print(f"Geçersiz veri alındı: {data}")  # Eğer float'a dönüştürülemezse hata yazdır

    def update_graph(self):
        self.cursorpos += 1
        self.x_data.append(self.cursorpos * 1)  # Zaman: artan sayılar
        self.y_data.append(self.BPM)  # Yeni veri değeri

        # Grafiği güncelle
        self.ax.clear()  # Önceki grafiği temizle
        self.line, = self.ax.plot(self.x_data, self.y_data, label='Kalp atışı', color='r')
        self.line.set_xdata(self.x_data)
        self.line.set_ydata(self.y_data)
        self.ax.set_title('Kalp atış hızı')
        self.ax.set_xlabel('Zaman (s)')
        self.ax.set_ylabel('Kalp Atışı')
        self.ax.legend()

        # Çizimi güncelle
        self.canvas.draw()
        if self.cursorpos == 20:
            self.x_data = []
            self.y_data = []
            self.cursorPos = 0
            self.line.remove()
            self.line = None

    def closeEvent(self, event):
        # Uygulama kapatılırken thread'i durdur
        self.worker_thread.stop()
        self.worker_thread.wait()
        event.accept()
