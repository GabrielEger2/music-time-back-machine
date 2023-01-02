# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainQXGFIR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton)
import source

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 800))
        MainWindow.setMaximumSize(QSize(1000, 800))
        MainWindow.setStyleSheet(u"")
        self.actionHow_to_Configure = QAction(MainWindow)
        self.actionHow_to_Configure.setObjectName(u"actionHow_to_Configure")
        self.actionAdd_Spotify_Account = QAction(MainWindow)
        self.actionAdd_Spotify_Account.setObjectName(u"actionAdd_Spotify_Account")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: #181818;\n"
"	font-size : 20pt;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 951, 341))
        self.label.setStyleSheet(u"image: url(:/newPrefix/Time Back Machine Logo.png);\n"
"border-color: rgb(24, 24, 24);")
        self.calendar_wd = QCalendarWidget(self.centralwidget)
        self.calendar_wd.setObjectName(u"calendar_wd")
        self.calendar_wd.setGeometry(QRect(120, 330, 721, 431))
        self.calendar_wd.setStyleSheet(u"alternate-background-color: rgb(24, 24, 24);\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(136, 384, 81, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1000, 22))
        self.menuMenu = QMenu(self.menuBar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionHow_to_Configure)
        self.menuMenu.addAction(self.actionAdd_Spotify_Account)
        self.menuMenu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionHow_to_Configure.setText(QCoreApplication.translate("MainWindow", u"How to Configure", None))
        self.actionAdd_Spotify_Account.setText(QCoreApplication.translate("MainWindow", u"How to Add an Spotify Account", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Week</span></p></body></html>", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

class Ui_ErrorMassage(object):
    def setupUi(self, ErrorMassage):
        if not ErrorMassage.objectName():
            ErrorMassage.setObjectName(u"ErrorMassage")
        ErrorMassage.resize(400, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ErrorMassage.sizePolicy().hasHeightForWidth())
        ErrorMassage.setSizePolicy(sizePolicy)
        ErrorMassage.setMinimumSize(QSize(500, 150))
        ErrorMassage.setMaximumSize(QSize(500, 150))
        font = QFont()
        font.setBold(False)
        ErrorMassage.setFont(font)
        self.centralwidget = QWidget(ErrorMassage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #1e1e1e;\n"
"    font-size: 13pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"    background-color: #2d5bd4;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #2D5BD4;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #d8d8d8;\n"
"    font: 14pt;\n"
"    font-weight: bold;\n"
"    background-color: #404040;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #d8d8d8;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    background-color: #404040;\n"
"    padding: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.lb_ERROR = QLabel(self.centralwidget)
        self.lb_ERROR.setObjectName(u"lb_ERROR")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.lb_ERROR.setFont(font1)

        self.verticalLayout.addWidget(self.lb_ERROR)

        self.lb_em = QLabel(self.centralwidget)
        self.lb_em.setObjectName(u"lb_em")

        self.verticalLayout.addWidget(self.lb_em)

        ErrorMassage.setCentralWidget(self.centralwidget)

        self.retranslateUi(ErrorMassage)

        QMetaObject.connectSlotsByName(ErrorMassage)
    # setupUi

    def retranslateUi(self, ErrorMassage):
        ErrorMassage.setWindowTitle(QCoreApplication.translate("ErrorMassage", u"Error Massage", None))
        self.lb_ERROR.setText(QCoreApplication.translate("ErrorMassage", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">ERROR</span></p></body></html>", None))
        self.lb_em.setText(QCoreApplication.translate("ErrorMassage", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Error Massage</span></p></body></html>", None))
    # retranslateUi

class Ui_HowToConfigure(object):
    def setupUi(self, HowToConfigure):
        if not HowToConfigure.objectName():
            HowToConfigure.setObjectName(u"HowToConfigure")
        HowToConfigure.resize(550, 800)
        HowToConfigure.setMinimumSize(QSize(550, 800))
        HowToConfigure.setMaximumSize(QSize(550, 800))
        HowToConfigure.setStyleSheet(u"background-color: #181818;\n"
"")
        self.centralwidget = QWidget(HowToConfigure)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 531, 571))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 720, 531, 81))
        self.Hyperlink = QLabel(self.centralwidget)
        self.Hyperlink.setObjectName(u"Hyperlink")
        self.Hyperlink.setGeometry(QRect(10, 170, 391, 21))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 600, 511, 116))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.ID_et = QLineEdit(self.widget)
        self.ID_et.setObjectName(u"ID_et")
        self.ID_et.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.ID_et)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.US_et = QLineEdit(self.widget)
        self.US_et.setObjectName(u"US_et")
        self.US_et.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.US_et)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.Website_et = QLineEdit(self.widget)
        self.Website_et.setObjectName(u"Website_et")
        self.Website_et.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.Website_et)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.add_info_bt = QPushButton(self.widget)
        self.add_info_bt.setObjectName(u"add_info_bt")
        self.add_info_bt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 68, 68);")

        self.verticalLayout.addWidget(self.add_info_bt)

        HowToConfigure.setCentralWidget(self.centralwidget)

        self.retranslateUi(HowToConfigure)

        QMetaObject.connectSlotsByName(HowToConfigure)
    # setupUi

    def retranslateUi(self, HowToConfigure):
        HowToConfigure.setWindowTitle(QCoreApplication.translate("HowToConfigure", u"How to Configure", None))
        self.label.setText(QCoreApplication.translate("HowToConfigure", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">In order to configure this program, you must have,</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">for obvious reasons, an spotify account.</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">Furthermore, you will need to create an spotify app,</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">this can be done through this link:</span></p><p><br/></p><p><br/></p><p><span style=\" font-size:11pt; color:#ffffff;\">Once you logged in your spotify account through the link,</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">you will need to create a spotify app, This can be accomplished</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">by clicking on the &quot;create an app&quot; button.</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">With your spotify app created, you will have to create a logging website,</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">in order to d"
                        "o that, you will need to click in the &quot;edit settings&quot; button and</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">on the &quot;Redirect URIs&quot; section, provide a random url, exemple:</span></p><p><span style=\" font-size:11pt; text-decoration: underline; color:#637aff;\">http://exemple.com</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">Finally you will also have to copy your Client ID, and secret,</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">available in the main dashboard menu.</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">Once you finished, please paste the information here:</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">Don't forget to click in the add button.<br/></span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("HowToConfigure", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Please don't share your user ID and secret.</span></p><p><span style=\" font-size:11pt; color:#ffffff;\">Don't worry, this program has no way of stealing this data.</span></p></body></html>", None))
        self.Hyperlink.setText(QCoreApplication.translate("HowToConfigure", u"<html><head/><body><p><span style=\" font-size:11pt; text-decoration: underline; color:#637aff;\">https://developer.spotify.com/dashboard/applications</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("HowToConfigure", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">User ID:</span></p></body></html>", None))
        self.ID_et.setText("")
        self.label_3.setText(QCoreApplication.translate("HowToConfigure", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">User Secret:</span></p></body></html>", None))
        self.US_et.setText("")
        self.label_4.setText(QCoreApplication.translate("HowToConfigure", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">Website:</span></p></body></html>", None))
        self.Website_et.setText("")
        self.add_info_bt.setText(QCoreApplication.translate("HowToConfigure", u"Add", None))
    # retranslateUi

class Ui_HowAddSpotify(object):
    def setupUi(self, HowAddSpotify):
        if not HowAddSpotify.objectName():
            HowAddSpotify.setObjectName(u"HowAddSpotify")
        HowAddSpotify.resize(500, 250)
        HowAddSpotify.setMinimumSize(QSize(500, 250))
        HowAddSpotify.setMaximumSize(QSize(500, 250))
        HowAddSpotify.setStyleSheet(u"background-color: #181818;\n"
"")
        self.centralwidget = QWidget(HowAddSpotify)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 481, 231))
        HowAddSpotify.setCentralWidget(self.centralwidget)

        self.retranslateUi(HowAddSpotify)

        QMetaObject.connectSlotsByName(HowAddSpotify)
    # setupUi

    def retranslateUi(self, HowAddSpotify):
        HowAddSpotify.setWindowTitle(QCoreApplication.translate("HowAddSpotify", u"How to Add Your Spotify Account", None))
        self.label.setText(QCoreApplication.translate("HowAddSpotify", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">To add your Spotify account, all you have to do is log in the link </span></p><p><span style=\" font-size:12pt; color:#ffffff;\">you have been redirected to when you select a date for the first time.</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">Then, after sucessufuly logging with your spotify account, </span></p><p><span style=\" font-size:12pt; color:#ffffff;\">copy the url and paste in the terminal.</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">That's the only way that I found to verify an account with</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">the spotipy lib</span></p></body></html>", None))
    # retranslateUi

