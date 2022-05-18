from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import re
import math


class Ui_FunctionPlotter(object):
    def setupUi(self, FunctionPlotter):
        FunctionPlotter.setObjectName("FunctionPlotter")
        FunctionPlotter.resize(1005, 703)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FunctionPlotter.setWindowIcon(icon)
        FunctionPlotter.setStyleSheet("QToolTip\n"
                                      "{\n"
                                      "     border: 1px solid black;\n"
                                      "     background-color: #ffa02f;\n"
                                      "     padding: 1px;\n"
                                      "     border-radius: 3px;\n"
                                      "     opacity: 100;\n"
                                      "}\n"
                                      "\n"
                                      "QWidget\n"
                                      "{\n"
                                      "    color: #b1b1b1;\n"
                                      "    background-color: #323232;\n"
                                      "}\n"
                                      "\n"
                                      "QTreeView, QListView\n"
                                      "{\n"
                                      "    background-color: silver;\n"
                                      "    margin-left: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QWidget:item:hover\n"
                                      "{\n"
                                      "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
                                      "    color: #000000;\n"
                                      "}\n"
                                      "\n"
                                      "QWidget:item:selected\n"
                                      "{\n"
                                      "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                      "}\n"
                                      "\n"
                                      "QMenuBar::item\n"
                                      "{\n"
                                      "    background: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "QMenuBar::item:selected\n"
                                      "{\n"
                                      "    background: transparent;\n"
                                      "    border: 1px solid #ffaa00;\n"
                                      "}\n"
                                      "\n"
                                      "QMenuBar::item:pressed\n"
                                      "{\n"
                                      "    background: #444;\n"
                                      "    border: 1px solid #000;\n"
                                      "    background-color: QLinearGradient(\n"
                                      "        x1:0, y1:0,\n"
                                      "        x2:0, y2:1,\n"
                                      "        stop:1 #212121,\n"
                                      "        stop:0.4 #343434/*,\n"
                                      "        stop:0.2 #343434,\n"
                                      "        stop:0.1 #ffaa00*/\n"
                                      "    );\n"
                                      "    margin-bottom:-1px;\n"
                                      "    padding-bottom:1px;\n"
                                      "}\n"
                                      "\n"
                                      "QMenu\n"
                                      "{\n"
                                      "    border: 1px solid #000;\n"
                                      "}\n"
                                      "\n"
                                      "QMenu::item\n"
                                      "{\n"
                                      "    padding: 2px 20px 2px 20px;\n"
                                      "}\n"
                                      "\n"
                                      "QMenu::item:selected\n"
                                      "{\n"
                                      "    color: #000000;\n"
                                      "}\n"
                                      "\n"
                                      "QWidget:disabled\n"
                                      "{\n"
                                      "    color: #808080;\n"
                                      "    background-color: #323232;\n"
                                      "}\n"
                                      "\n"
                                      "QAbstractItemView\n"
                                      "{\n"
                                      "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
                                      "}\n"
                                      "\n"
                                      "QWidget:focus\n"
                                      "{\n"
                                      "    /*border: 1px solid darkgray;*/\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit\n"
                                      "{\n"
                                      "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
                                      "    padding: 1px;\n"
                                      "    border-style: solid;\n"
                                      "    border: 1px solid #1e1e1e;\n"
                                      "    border-radius: 5;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton\n"
                                      "{\n"
                                      "    color: #b1b1b1;\n"
                                      "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                                      "    border-width: 1px;\n"
                                      "    border-color: #1e1e1e;\n"
                                      "    border-style: solid;\n"
                                      "    border-radius: 6;\n"
                                      "    padding: 3px;\n"
                                      "    font-size: 12px;\n"
                                      "    padding-left: 5px;\n"
                                      "    padding-right: 5px;\n"
                                      "    min-width: 40px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed\n"
                                      "{\n"
                                      "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox\n"
                                      "{\n"
                                      "    selection-background-color: #ffaa00;\n"
                                      "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                                      "    border-style: solid;\n"
                                      "    border: 1px solid #1e1e1e;\n"
                                      "    border-radius: 5;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox:hover,QPushButton:hover\n"
                                      "{\n"
                                      "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QComboBox:on\n"
                                      "{\n"
                                      "    padding-top: 3px;\n"
                                      "    padding-left: 4px;\n"
                                      "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                      "    selection-background-color: #ffaa00;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox QAbstractItemView\n"
                                      "{\n"
                                      "    border: 2px solid darkgray;\n"
                                      "    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::drop-down\n"
                                      "{\n"
                                      "     subcontrol-origin: padding;\n"
                                      "     subcontrol-position: top right;\n"
                                      "     width: 15px;\n"
                                      "\n"
                                      "     border-left-width: 0px;\n"
                                      "     border-left-color: darkgray;\n"
                                      "     border-left-style: solid; /* just a single line */\n"
                                      "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                      "     border-bottom-right-radius: 3px;\n"
                                      " }\n"
                                      "\n"
                                      "QComboBox::down-arrow\n"
                                      "{\n"
                                      "     image: url(:/dark_orange/img/down_arrow.png);\n"
                                      "}\n"
                                      "\n"
                                      "QGroupBox\n"
                                      "{\n"
                                      "    border: 1px solid darkgray;\n"
                                      "    margin-top: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QGroupBox:focus\n"
                                      "{\n"
                                      "    border: 1px solid darkgray;\n"
                                      "}\n"
                                      "\n"
                                      "QTextEdit:focus\n"
                                      "{\n"
                                      "    border: 1px solid darkgray;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar:horizontal {\n"
                                      "     border: 1px solid #222222;\n"
                                      "     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                                      "     height: 7px;\n"
                                      "     margin: 0px 16px 0 16px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:horizontal\n"
                                      "{\n"
                                      "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
                                      "      min-height: 20px;\n"
                                      "      border-radius: 2px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-line:horizontal {\n"
                                      "      border: 1px solid #1b1b19;\n"
                                      "      border-radius: 2px;\n"
                                      "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                      "      width: 14px;\n"
                                      "      subcontrol-position: right;\n"
                                      "      subcontrol-origin: margin;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::sub-line:horizontal {\n"
                                      "      border: 1px solid #1b1b19;\n"
                                      "      border-radius: 2px;\n"
                                      "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                      "      width: 14px;\n"
                                      "     subcontrol-position: left;\n"
                                      "     subcontrol-origin: margin;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
                                      "{\n"
                                      "      border: 1px solid black;\n"
                                      "      width: 1px;\n"
                                      "      height: 1px;\n"
                                      "      background: white;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                      "{\n"
                                      "      background: none;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar:vertical\n"
                                      "{\n"
                                      "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                                      "      width: 7px;\n"
                                      "      margin: 16px 0 16px 0;\n"
                                      "      border: 1px solid #222222;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:vertical\n"
                                      "{\n"
                                      "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
                                      "      min-height: 20px;\n"
                                      "      border-radius: 2px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-line:vertical\n"
                                      "{\n"
                                      "      border: 1px solid #1b1b19;\n"
                                      "      border-radius: 2px;\n"
                                      "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                      "      height: 14px;\n"
                                      "      subcontrol-position: bottom;\n"
                                      "      subcontrol-origin: margin;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::sub-line:vertical\n"
                                      "{\n"
                                      "      border: 1px solid #1b1b19;\n"
                                      "      border-radius: 2px;\n"
                                      "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
                                      "      height: 14px;\n"
                                      "      subcontrol-position: top;\n"
                                      "      subcontrol-origin: margin;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
                                      "{\n"
                                      "      border: 1px solid black;\n"
                                      "      width: 1px;\n"
                                      "      height: 1px;\n"
                                      "      background: white;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
                                      "{\n"
                                      "      background: none;\n"
                                      "}\n"
                                      "\n"
                                      "QTextEdit\n"
                                      "{\n"
                                      "    background-color: #242424;\n"
                                      "}\n"
                                      "\n"
                                      "QPlainTextEdit\n"
                                      "{\n"
                                      "    background-color: #242424;\n"
                                      "}\n"
                                      "\n"
                                      "QHeaderView::section\n"
                                      "{\n"
                                      "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
                                      "    color: white;\n"
                                      "    padding-left: 4px;\n"
                                      "    border: 1px solid #6c6c6c;\n"
                                      "}\n"
                                      "\n"
                                      "QCheckBox:disabled\n"
                                      "{\n"
                                      "color: #414141;\n"
                                      "}\n"
                                      "\n"
                                      "QDockWidget::title\n"
                                      "{\n"
                                      "    text-align: center;\n"
                                      "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                      "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                                      "}\n"
                                      "\n"
                                      "QDockWidget::close-button, QDockWidget::float-button\n"
                                      "{\n"
                                      "    text-align: center;\n"
                                      "    spacing: 1px; /* spacing between items in the tool bar */\n"
                                      "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                                      "}\n"
                                      "\n"
                                      "QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
                                      "{\n"
                                      "    background: #242424;\n"
                                      "}\n"
                                      "\n"
                                      "QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
                                      "{\n"
                                      "    padding: 1px -1px -1px 1px;\n"
                                      "}\n"
                                      "\n"
                                      "QMainWindow::separator\n"
                                      "{\n"
                                      "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                                      "    color: white;\n"
                                      "    padding-left: 4px;\n"
                                      "    border: 1px solid #4c4c4c;\n"
                                      "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                      "}\n"
                                      "\n"
                                      "QMainWindow::separator:hover\n"
                                      "{\n"
                                      "\n"
                                      "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
                                      "    color: white;\n"
                                      "    padding-left: 4px;\n"
                                      "    border: 1px solid #6c6c6c;\n"
                                      "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                      "}\n"
                                      "\n"
                                      "QToolBar::handle\n"
                                      "{\n"
                                      "     spacing: 3px; /* spacing between items in the tool bar */\n"
                                      "     background: url(:/dark_orange/img/handle.png);\n"
                                      "}\n"
                                      "\n"
                                      "QMenu::separator\n"
                                      "{\n"
                                      "    height: 2px;\n"
                                      "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                                      "    color: white;\n"
                                      "    padding-left: 4px;\n"
                                      "    margin-left: 10px;\n"
                                      "    margin-right: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QProgressBar\n"
                                      "{\n"
                                      "    border: 2px solid grey;\n"
                                      "    border-radius: 5px;\n"
                                      "    text-align: center;\n"
                                      "}\n"
                                      "\n"
                                      "QProgressBar::chunk\n"
                                      "{\n"
                                      "    background-color: #d7801a;\n"
                                      "    width: 2.15px;\n"
                                      "    margin: 0.5px;\n"
                                      "}\n"
                                      "\n"
                                      "QTabBar::tab {\n"
                                      "    color: #b1b1b1;\n"
                                      "    border: 1px solid #444;\n"
                                      "    border-bottom-style: none;\n"
                                      "    background-color: #323232;\n"
                                      "    padding-left: 10px;\n"
                                      "    padding-right: 10px;\n"
                                      "    padding-top: 3px;\n"
                                      "    padding-bottom: 2px;\n"
                                      "    margin-right: -1px;\n"
                                      "}\n"
                                      "\n"
                                      "QTabWidget::pane {\n"
                                      "    border: 1px solid #444;\n"
                                      "    top: 1px;\n"
                                      "}\n"
                                      "\n"
                                      "QTabBar::tab:last\n"
                                      "{\n"
                                      "    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
                                      "    border-top-right-radius: 3px;\n"
                                      "}\n"
                                      "\n"
                                      "QTabBar::tab:first:!selected\n"
                                      "{\n"
                                      " margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
                                      "\n"
                                      "\n"
                                      "    border-top-left-radius: 3px;\n"
                                      "}\n"
                                      "\n"
                                      "QTabBar::tab:!selected\n"
                                      "{\n"
                                      "    color: #b1b1b1;\n"
                                      "    border-bottom-style: solid;\n"
                                      "    margin-top: 3px;\n"
                                      "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
                                      "}\n"
                                      "\n"
                                      "QTabBar::tab:selected\n"
                                      "{\n"
                                      "    border-top-left-radius: 3px;\n"
                                      "    border-top-right-radius: 3px;\n"
                                      "    margin-bottom: 0px;\n"
                                      "}\n"
                                      "\n"
                                      "QTabBar::tab:!selected:hover\n"
                                      "{\n"
                                      "    /*border-top: 2px solid #ffaa00;\n"
                                      "    padding-bottom: 3px;*/\n"
                                      "    border-top-left-radius: 3px;\n"
                                      "    border-top-right-radius: 3px;\n"
                                      "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
                                      "}\n"
                                      "\n"
                                      "QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
                                      "    color: #b1b1b1;\n"
                                      "    background-color: #323232;\n"
                                      "    border: 1px solid #b1b1b1;\n"
                                      "    border-radius: 6px;\n"
                                      "}\n"
                                      "\n"
                                      "QRadioButton::indicator:checked\n"
                                      "{\n"
                                      "    background-color: qradialgradient(\n"
                                      "        cx: 0.5, cy: 0.5,\n"
                                      "        fx: 0.5, fy: 0.5,\n"
                                      "        radius: 1.0,\n"
                                      "        stop: 0.25 #ffaa00,\n"
                                      "        stop: 0.3 #323232\n"
                                      "    );\n"
                                      "}\n"
                                      "\n"
                                      "QCheckBox::indicator{\n"
                                      "    color: #b1b1b1;\n"
                                      "    background-color: #323232;\n"
                                      "    border: 1px solid #b1b1b1;\n"
                                      "    width: 9px;\n"
                                      "    height: 9px;\n"
                                      "}\n"
                                      "\n"
                                      "QRadioButton::indicator\n"
                                      "{\n"
                                      "    border-radius: 6px;\n"
                                      "}\n"
                                      "\n"
                                      "QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
                                      "{\n"
                                      "    border: 1px solid #ffaa00;\n"
                                      "}\n"
                                      "\n"
                                      "QCheckBox::indicator:checked\n"
                                      "{\n"
                                      "    image:url(:/dark_orange/img/checkbox.png);\n"
                                      "}\n"
                                      "\n"
                                      "QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
                                      "{\n"
                                      "    border: 1px solid #444;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QSlider::groove:horizontal {\n"
                                      "    border: 1px solid #3A3939;\n"
                                      "    height: 8px;\n"
                                      "    background: #201F1F;\n"
                                      "    margin: 2px 0;\n"
                                      "    border-radius: 2px;\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::handle:horizontal {\n"
                                      "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
                                      "    border: 1px solid #3A3939;\n"
                                      "    width: 14px;\n"
                                      "    height: 14px;\n"
                                      "    margin: -4px 0;\n"
                                      "    border-radius: 2px;\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::groove:vertical {\n"
                                      "    border: 1px solid #3A3939;\n"
                                      "    width: 8px;\n"
                                      "    background: #201F1F;\n"
                                      "    margin: 0 0px;\n"
                                      "    border-radius: 2px;\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::handle:vertical {\n"
                                      "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
                                      "      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
                                      "    border: 1px solid #3A3939;\n"
                                      "    width: 14px;\n"
                                      "    height: 14px;\n"
                                      "    margin: 0 -4px;\n"
                                      "    border-radius: 2px;\n"
                                      "}\n"
                                      "\n"
                                      "QAbstractSpinBox {\n"
                                      "    padding-top: 2px;\n"
                                      "    padding-bottom: 2px;\n"
                                      "    border: 1px solid darkgray;\n"
                                      "\n"
                                      "    border-radius: 2px;\n"
                                      "    min-width: 50px;\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.show_MessageBox()
        self.centralwidget = QtWidgets.QWidget(FunctionPlotter)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 7, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.MinValSpinBox = QtWidgets.QSpinBox(self.splitter_2)
        self.MinValSpinBox.setMinimum(-1000)
        self.MinValSpinBox.setMaximum(1000)
        self.MinValSpinBox.setObjectName("MinValSpinBox")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.MaxValSpinBox = QtWidgets.QSpinBox(self.splitter_2)
        self.MaxValSpinBox.setMinimum(-1000)
        self.MaxValSpinBox.setMaximum(1000)
        self.MaxValSpinBox.setObjectName("MaxValSpinBox")
        self.gridLayout.addWidget(self.splitter_2, 5, 2, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.oneBtn = QtWidgets.QPushButton(
            self.layoutWidget, clicked=lambda: self.press_it("1"))
        self.oneBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.oneBtn.setMaximumSize(QtCore.QSize(300, 16777215))
        self.oneBtn.setAccessibleName("")
        self.oneBtn.setObjectName("oneBtn")
        self.verticalLayout.addWidget(self.oneBtn)
        self.FourBtn = QtWidgets.QPushButton(
            self.layoutWidget, clicked=lambda: self.press_it("4"))
        self.FourBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.FourBtn.setMaximumSize(QtCore.QSize(300, 16777215))
        self.FourBtn.setObjectName("FourBtn")
        self.verticalLayout.addWidget(self.FourBtn)
        self.SevenBtn = QtWidgets.QPushButton(
            self.layoutWidget, clicked=lambda: self.press_it("7"))
        self.SevenBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.SevenBtn.setMaximumSize(QtCore.QSize(300, 16777215))
        self.SevenBtn.setObjectName("SevenBtn")
        self.verticalLayout.addWidget(self.SevenBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TwoBtn = QtWidgets.QPushButton(
            self.layoutWidget, clicked=lambda: self.press_it("2"))
        self.TwoBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.TwoBtn.setObjectName("TwoBtn")
        self.verticalLayout_2.addWidget(self.TwoBtn)
        self.FiveBtn = QtWidgets.QPushButton(
            self.layoutWidget, clicked=lambda: self.press_it("5"))
        self.FiveBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.FiveBtn.setObjectName("FiveBtn")
        self.verticalLayout_2.addWidget(self.FiveBtn)
        self.EigthBtn = QtWidgets.QPushButton(
            self.layoutWidget, clicked=lambda: self.press_it("8"))
        self.EigthBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.EigthBtn.setObjectName("EigthBtn")
        self.verticalLayout_2.addWidget(self.EigthBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ThreeBtn = QtWidgets.QPushButton(
            self.layoutWidget, clicked=lambda: self.press_it("3"))
        self.ThreeBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.ThreeBtn.setObjectName("ThreeBtn")
        self.verticalLayout_3.addWidget(self.ThreeBtn)
        self.SixBtn = QtWidgets.QPushButton(
            self.layoutWidget, clicked=lambda: self.press_it("6"))
        self.SixBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.SixBtn.setObjectName("SixBtn")
        self.verticalLayout_3.addWidget(self.SixBtn)
        self.NineBtn = QtWidgets.QPushButton(
            self.layoutWidget, clicked=lambda: self.press_it("9"))
        self.NineBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.NineBtn.setObjectName("NineBtn")
        self.verticalLayout_3.addWidget(self.NineBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.pushButton_10 = QtWidgets.QPushButton(
            self.layoutWidget, clicked=lambda: self.press_it("0"))
        self.pushButton_10.setMinimumSize(QtCore.QSize(52, 60))
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_4.addWidget(self.pushButton_10)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.MulBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.press_it("*"))
        self.MulBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.MulBtn.setObjectName("MulBtn")
        self.verticalLayout_7.addWidget(self.MulBtn)
        self.ExpBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.press_it("exp("))
        self.ExpBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.ExpBtn.setObjectName("ExpBtn")
        self.verticalLayout_7.addWidget(self.ExpBtn)
        self.OpenBracketBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.press_it("("))
        self.OpenBracketBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.OpenBracketBtn.setObjectName("OpenBracketBtn")
        self.verticalLayout_7.addWidget(self.OpenBracketBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.PlusBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.press_it("+"))
        self.PlusBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.PlusBtn.setObjectName("PlusBtn")
        self.verticalLayout_5.addWidget(self.PlusBtn)
        self.MinusBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.press_it("-"))
        self.MinusBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.MinusBtn.setObjectName("MinusBtn")
        self.verticalLayout_5.addWidget(self.MinusBtn)
        self.ClosedBracketBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.press_it(")"))
        self.ClosedBracketBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.ClosedBracketBtn.setObjectName("ClosedBracketBtn")
        self.verticalLayout_5.addWidget(self.ClosedBracketBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.DivBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.press_it("/"))
        self.DivBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.DivBtn.setObjectName("DivBtn")
        self.verticalLayout_6.addWidget(self.DivBtn)
        self.PowerBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.press_it("^"))
        self.PowerBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.PowerBtn.setObjectName("PowerBtn")
        self.verticalLayout_6.addWidget(self.PowerBtn)
        self.XBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.press_it("x"))
        self.XBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.XBtn.setObjectName("XBtn")
        self.verticalLayout_6.addWidget(self.XBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DelBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.press_it("Del"))
        self.DelBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.DelBtn.setObjectName("DelBtn")
        self.horizontalLayout_3.addWidget(self.DelBtn)
        self.ClrBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.press_it("Clr"))
        self.ClrBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.ClrBtn.setObjectName("ClrBtn")
        self.horizontalLayout_3.addWidget(self.ClrBtn)
        self.DrawBtn = QtWidgets.QPushButton(
            self.layoutWidget1, clicked=lambda: self.Draw())
        self.DrawBtn.setMinimumSize(QtCore.QSize(52, 60))
        self.DrawBtn.setObjectName("DrawBtn")
        self.horizontalLayout_3.addWidget(self.DrawBtn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.splitter, 8, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 2, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 11, 2, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 5, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 2, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout.addWidget(self.line_11, 1, 4, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout.addWidget(self.line_12, 1, 3, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 8, 4, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout.addWidget(self.line_13, 9, 2, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 8, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 1, 1, 1, 1)
        self.EquationTaker = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.EquationTaker.setMinimumSize(QtCore.QSize(700, 0))
        self.EquationTaker.setMaximumSize(QtCore.QSize(700, 30))
        self.EquationTaker.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.EquationTaker.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EquationTaker.setReadOnly(True)
        self.EquationTaker.setCenterOnScroll(False)
        self.EquationTaker.setObjectName("EquationTaker")
        self.gridLayout.addWidget(
            self.EquationTaker, 3, 2, 1, 3, QtCore.Qt.AlignHCenter)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.gridLayout.addWidget(self.line_14, 10, 0, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout.addWidget(self.line_15, 10, 1, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout.addWidget(self.line_16, 10, 3, 1, 1)
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.gridLayout.addWidget(self.line_17, 10, 4, 1, 1)
        FunctionPlotter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FunctionPlotter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 26))
        self.menubar.setObjectName("menubar")
        self.menuFunction_Plotter = QtWidgets.QMenu(self.menubar)
        self.menuFunction_Plotter.setObjectName("menuFunction_Plotter")
        FunctionPlotter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FunctionPlotter)
        self.statusbar.setObjectName("statusbar")
        FunctionPlotter.setStatusBar(self.statusbar)
        self.icon = QtWidgets.QAction(FunctionPlotter)
        self.icon.setIcon(icon)
        self.icon.setObjectName("icon")
        self.menubar.addAction(self.menuFunction_Plotter.menuAction())

        self.retranslateUi(FunctionPlotter)
        QtCore.QMetaObject.connectSlotsByName(FunctionPlotter)

    def retranslateUi(self, FunctionPlotter):
        _translate = QtCore.QCoreApplication.translate
        FunctionPlotter.setWindowTitle(_translate(
            "FunctionPlotter", "FunctionPlotter"))
        self.label_3.setText(_translate("FunctionPlotter", "Function Plotter"))
        self.label.setText(_translate("FunctionPlotter", "Minimum Value"))
        self.MinValSpinBox.setStatusTip(_translate(
            "FunctionPlotter", "Minimum Value must be less than Maximum Value"))
        self.label_2.setText(_translate("FunctionPlotter", "Maximum Value"))
        self.MaxValSpinBox.setStatusTip(_translate(
            "FunctionPlotter", "Minimum Value must be less than Maximum Value"))
        self.oneBtn.setText(_translate("FunctionPlotter", "1"))
        self.FourBtn.setText(_translate("FunctionPlotter", "4"))
        self.SevenBtn.setText(_translate("FunctionPlotter", "7"))
        self.TwoBtn.setText(_translate("FunctionPlotter", "2"))
        self.FiveBtn.setText(_translate("FunctionPlotter", "5"))
        self.EigthBtn.setText(_translate("FunctionPlotter", "8"))
        self.ThreeBtn.setText(_translate("FunctionPlotter", "3"))
        self.SixBtn.setText(_translate("FunctionPlotter", "6"))
        self.NineBtn.setText(_translate("FunctionPlotter", "9"))
        self.pushButton_10.setText(_translate("FunctionPlotter", "0"))
        self.MulBtn.setStatusTip(_translate("FunctionPlotter", "multiply"))
        self.MulBtn.setText(_translate("FunctionPlotter", "*"))
        self.ExpBtn.setStatusTip(_translate("FunctionPlotter", "exponential"))
        self.ExpBtn.setText(_translate("FunctionPlotter", "e"))
        self.OpenBracketBtn.setStatusTip(_translate(
            "FunctionPlotter", "Don\'t forget to close the bracket"))
        self.OpenBracketBtn.setText(_translate("FunctionPlotter", "("))
        self.PlusBtn.setStatusTip(_translate("FunctionPlotter", "plus"))
        self.PlusBtn.setText(_translate("FunctionPlotter", "+"))
        self.MinusBtn.setStatusTip(_translate("FunctionPlotter", "minus"))
        self.MinusBtn.setText(_translate("FunctionPlotter", "-"))
        self.ClosedBracketBtn.setStatusTip(_translate(
            "FunctionPlotter", "Don\'t forget to open the bracket"))
        self.ClosedBracketBtn.setText(_translate("FunctionPlotter", ")"))
        self.DivBtn.setStatusTip(_translate("FunctionPlotter", "divide"))
        self.DivBtn.setText(_translate("FunctionPlotter", "/"))
        self.PowerBtn.setStatusTip(_translate("FunctionPlotter", "power"))
        self.PowerBtn.setText(_translate("FunctionPlotter", "^"))
        self.XBtn.setText(_translate("FunctionPlotter", "X"))
        self.DelBtn.setStatusTip(_translate(
            "FunctionPlotter", "Delete last char"))
        self.DelBtn.setText(_translate("FunctionPlotter", "DEL"))
        self.ClrBtn.setStatusTip(_translate(
            "FunctionPlotter", "Clear the whole Equation"))
        self.ClrBtn.setText(_translate("FunctionPlotter", "CLR"))
        self.DrawBtn.setStatusTip(_translate(
            "FunctionPlotter", "Plot the function"))
        self.DrawBtn.setText(_translate("FunctionPlotter", "DRAW"))
        self.EquationTaker.setStatusTip(_translate(
            "FunctionPlotter", "Enter the equation in this form: 2*x not 2x "))
        self.EquationTaker.setPlaceholderText(_translate(
            "FunctionPlotter", "Enter The Equation Using the buttons"))
        self.menuFunction_Plotter.setTitle(
            _translate("FunctionPlotter", "Function Plotter"))
        self.icon.setText(_translate("FunctionPlotter", "plotter"))

##################################################################################
    # my code
    def press_it(self, pressed):
        if(pressed == "Clr"):
            self.EquationTaker.clear()
            self.EquationTaker.setPlaceholderText(
                "Enter The equation using the Buttons")
        elif(pressed == "Del"):
            newText = self.EquationTaker.toPlainText()
            newText = newText[:len(newText) - 1]
            self.EquationTaker.clear()
            self.EquationTaker.insertPlainText(newText)
        else:
            self.EquationTaker.insertPlainText(pressed)
        pass

    replacements = {
        'exp': 'np.exp',
        '^': '**',
    }

    allowed_words = [
        'x',
        'exp',
    ]

    def string2func(self, string):
        ''' evaluates the string and returns a function of x '''
        # replace the user input into python expression
        for old, new in self.replacements.items():
            string = string.replace(old, new)

        def func(x):
            l = eval(string)
            # check for infinity if divide by zero
            idx = np.argwhere(l == math.inf)
            if(l[idx] == math.inf):
                self.statusbar.showMessage("Your range has a division by zero")
            return l

        return func

    def Draw(self):
        string = self.EquationTaker.toPlainText()
        if string != "Enter The equation using the Buttons" or string == ' ':  # entries must be not empty
            try:
                func = self.string2func(string)
                mn = self.MinValSpinBox.value()
                mx = self.MaxValSpinBox.value()
                if mn >= mx:
                    self.statusbar.showMessage(
                        "Minimum value must  be less than maximum value")
                    return
                x = np.arange(mn, mx, .5)
                plt.grid()
                plt.plot(x, func(x))
                plt.xlim(mn, mx)

                plt.show()
            except:
                self.statusbar.showMessage(
                    "Wrong Formate!")

        else:
            self.statusbar.showMessage(
                "Please insert an equation and make sure that the min val is less than max val")

    def show_MessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setWindowTitle("Tips")
        msg.setText(
            "   Please read the following instructions carefully\n\n- All Warnings will be shown in the status bar down the screen\n\n- You can't type in the program, you should use the buttons displayed to insert your equation\n\n- the equation formate must contain x\n\n- if you want to plot 2x you should insert it in this formate 2*x not 2x\n\n- you must take care of the brackets\n\n- minimum values must be less than maximum values")
        x = msg.exec_()
###################################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FunctionPlotter = QtWidgets.QMainWindow()
    ui = Ui_FunctionPlotter()
    ui.setupUi(FunctionPlotter)

    FunctionPlotter.show()
    sys.exit(app.exec_())
