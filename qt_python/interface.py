# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(927, 630)
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wheel_widget = QtWidgets.QWidget(self.frame_2)
        self.wheel_widget.setMinimumSize(QtCore.QSize(200, 300))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wheel_widget.setFont(font)
        self.wheel_widget.setStyleSheet("image: url(:/nnew/dogru_direksiyon.png);")
        self.wheel_widget.setObjectName("wheel_widget")
        self.verticalLayout_3.addWidget(self.wheel_widget)
        self.warning_widget = QtWidgets.QWidget(self.frame_2)
        self.warning_widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.warning_widget.setObjectName("warning_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.warning_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.warning_widget)
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.warning_widget, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.temperature_label = QtWidgets.QLabel(self.frame_2)
        self.temperature_label.setFont(QtGui.QFont("Arial", 16))
        self.temperature_label.setStyleSheet("color: white;")
        self.temperature_label.setText("Sıcaklık: Bekleniyor...")
        self.verticalLayout_3.addWidget(self.temperature_label)

        self.heart_rate_label = QtWidgets.QLabel(self.frame_2)
        self.heart_rate_label.setFont(QtGui.QFont("Arial", 16))
        self.heart_rate_label.setStyleSheet("color: white;")
        self.heart_rate_label.setText("Nabız: Bekleniyor...")
        self.verticalLayout_3.addWidget(self.heart_rate_label)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LÜTFEN ELLERİNİZİ DOĞRU KONUMA KOYUNUZ"))

    def update_warning_message(self, message: str):
        """Uyarı mesajını güncelleyen fonksiyon"""
        self.label.setText(message)
    
 
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
