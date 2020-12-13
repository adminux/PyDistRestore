# -*- coding: utf-8 -*-
__author__ = 'user1'

import PyQt5
from PyQt5 import (QtWidgets, QtGui, QtCore)
from datetime import datetime
from PyQt5.QtWidgets import (QMessageBox, QTreeWidget, QTreeWidgetItem, QTreeWidgetItemIterator, QAction)
from os.path import basename

import design   # импорт формы
import constants as const   # импорт глобальных констант

class GUI(QtWidgets.QMainWindow, design.Ui_MainWindow):
    """
    Класс взаимодействия графического интерфейса с пользователем
    """

    def __init__(self) -> None:
        """
        Конструктор класса
        """

        super().__init__()
        self.setupUi(self)

    def __del__(self)-> None:
        """
        Деструктор класса
        """

        pass

    def showMessage(self, message):
        """
        Отображение информационного сообщения
        """

        if message == "" :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка вывода пустого сообщения, метод showMessage, класс GUI приложения " + const.project_name + " !")
            msg.setWindowTitle(const.critical_info_message_label)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return -1
        else:
            self.textEdit.append(" " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " : " +  message + " ;"); 


