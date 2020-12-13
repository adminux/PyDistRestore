# -*- coding: utf-8 -*-
__author__ = 'adminux'

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import GUI
import constants as const   # импорт глобальных констант

def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = GUI.GUI()
        window.resize(1200, 800)
        window.show()
        app.exec_()
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка запуска приложения " + const.project_name + " !")
        msg.setWindowTitle(const.critical_info_message_label)
        msg.setDetailedText(str(e))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        return -1

if __name__ == '__main__':
    main()

