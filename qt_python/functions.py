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

class WorkerThread(QThread):
    resultReady = pyqtSignal(int)  # Ayrıştırılmış veriyi iletmek için sinyal
    def __init__(self):
        super().__init__()
        self.is_running = True  # Thread'in çalışmasını kontrol eden bayrak
        self.ser = serial.Serial('/dev/ttyUSB0', 115200)
    #def run(self):
    #    print("Simülasyon modu aktif. Test verileri gönderiliyor.")
    #    while self.is_running:
    #        try:
                # Simüle edilmiş veriler oluştur
    #            fake_data = {
    #                "temperature": round(random.uniform(35.0, 39.0), 1),  # Rastgele sıcaklık
    #                "heart_rate": random.randint(60, 120)  # Rastgele nabız
    #            }
    #            print(f"Simüle edilen veri: {fake_data}")
    #            self.resultReady.emit(fake_data)  # Veriyi sinyal ile gönder
    #            time.sleep(1)  # 1 saniye bekle
    #        except Exception as e:
    #            print(f"Simülasyon sırasında hata: {e}")

    #def stop(self):
    #    self.is_running = False  # Döngüyü durdur
    #    print("Simülasyon durduruldu.")
    # def __init__(self):
    #     super().__init__()
    #     try:
    #         self.ser = serial.Serial('/dev/ttyUSB0', 115200,timeout=1)  # Seri port ayarı
    #     except serial.SerialException as e:
    #         print(f"Seri port hatası: {e}")
    #         self.ser = None
    #     self.is_running = True

     
    def run(self):
        if self.ser is None:
            print("Seri port açılmadı, veri okumaya başlanamaz.")
            return
    
        while self.is_running:
            try:
                while True:
                    data = self.ser.readline() # Satır bazında veri okuyun
                    decoded_data = data.decode('utf-8').split('\n')[0].strip()
                    print(f"Alınan veri: {decoded_data}")
                    #parsed_data = self.parse_data(data)  # Veriyi ayrıştır
                    #if parsed_data:  # Ayrıştırma başarılıysa sinyal gönder
                    self.resultReady.emit(decoded_data)
            except Exception as e:
                print(f"Veri okuma hatası: {e}")
            finally:
                if not self.is_running:
                    print("WorkerThread döngüsü sonlandırıldı.")
            
     


    def parse_data(self, data: bytes):
        """Ham veriyi ayrıştırır ve bir float değer döndürür."""
        try:
            # Gelen bytes veriyi string'e çevir ve strip ile boşlukları temizle
            decoded_data = data.decode('utf-8').strip()
            # String veriyi float'a dönüştür
            value = float(decoded_data)
            return {'value': value}  # Sözlük formatında döndür
        except (ValueError, UnicodeDecodeError) as e:
            print(f"Veri ayrıştırma hatası: {e}, Gelen veri: {data}")
            return None  # Ayrıştırma başarısızsa None döndür



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

    def toggle_background(self):
        # Arka plan rengini kırmızıya değiştir veya temizle
        if self.is_red:
            self.ui.warning_widget.setStyleSheet("background-color: none;")
        else:
            self.ui.warning_widget.setStyleSheet("background-color: red;")
        self.is_red = not self.is_red

    def speak_warning(self, message):
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()
    
    def control(self, data):
        print(f"Alınan veri: {data}")  # Gelen veriyi kontrol et
        try:
            temperature = float(data)  # Veriyi float'a dönüştür
            print(f"Dönüştürülen sıcaklık: {temperature}")  # Dönüştürülen veriyi yazdır
            self.ui.temperature_label.setText(f"Sıcaklık: {temperature:.1f} °C")
            if temperature > 38.0:
                self.ui.update_warning_message("Ateş Yüksek!")
                self.speak_warning("Ateş yüksek!")
        except ValueError:
            print(f"Geçersiz veri alındı: {data}")  # Eğer float'a dönüştürülemezse hata yazdır


    def closeEvent(self, event):
        # Uygulama kapatılırken thread'i durdur
        self.worker_thread.stop()
        self.worker_thread.wait()
        event.accept()
