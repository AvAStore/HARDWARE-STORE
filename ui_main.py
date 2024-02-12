# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
import Resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1642, 792)
        icon = QIcon()
        icon.addFile(u":/img/icon.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"background-color: rgb(32, 44, 51);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 0, 12, 0)
        self.label_37 = QLabel(self.frame_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(32, 32))
        self.label_37.setPixmap(QPixmap(u":/img/icon.jpeg"))
        self.label_37.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_37)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.horizontalSpacer = QSpacerItem(921, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(100, 0))
        self.frame_6.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(157, 169, 176);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(157, 169, 176);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/img/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/img/power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(22, 31, 37);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(250, 0))
        self.frame_7.setMaximumSize(QSize(250, 16777215))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"background-color: rgb(17, 27, 33);\n"
"border-right: 1px solid rgb(38, 61, 75);\n"
"}\n"
"QPushButton{\n"
"border-top: 1px solid rgb(38, 61, 75);\n"
"border-bottom: 1px solid rgb(38, 61, 75);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 66);\n"
"border-left: 3px solid rgb(255, 61, 75);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 60))
        font1 = QFont()
        font1.setFamilies([u"Horyzen"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/img/cash-register.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 60))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"border-top: 1px solid rgb(38, 61, 75);\n"
"border-bottom: 1px solid rgb(38, 61, 75);")
        icon4 = QIcon()
        icon4.addFile(u":/img/ballot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 60))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"border-top: 1px solid rgb(38, 61, 75);\n"
"border-bottom: 1px solid rgb(38, 61, 75);")
        icon5 = QIcon()
        icon5.addFile(u":/img/sort-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 60))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"border-top: 1px solid rgb(38, 61, 75);\n"
"border-bottom: 1px solid rgb(38, 61, 75);")
        icon6 = QIcon()
        icon6.addFile(u":/img/chat-arrow-grow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 30))
        self.frame_13.setStyleSheet(u"QPushButton{\n"
"border-radius:30px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 66);\n"
"border: 3px solid rgb(255, 61, 75);\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_8 = QPushButton(self.frame_13)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy2)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/img/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.frame_13)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)
        self.pushButton_7.setMinimumSize(QSize(64, 64))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/img/lock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.pushButton_7)


        self.verticalLayout_3.addWidget(self.frame_13)


        self.horizontalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(42, 57, 66);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_6 = QHBoxLayout(self.page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_9 = QFrame(self.page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setLayoutDirection(Qt.LeftToRight)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setMaximumSize(QSize(16777215, 80))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Horyzen"])
        font2.setPointSize(16)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(124, 124, 124, 246), stop:0.329545 rgba(49, 65, 77, 255), stop:0.659091 rgba(49, 65, 77, 255), stop:1 rgba(124, 124, 124, 255));")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_10 = QFrame(self.frame_12)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(400, 500))
        self.frame_10.setStyleSheet(u"#frame_10{\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"QFrame{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius:8px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 200))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_14)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.frame_14)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setFamilies([u"Horyzen Light"])
        font3.setPointSize(12)
        self.comboBox.setFont(font3)
        self.comboBox.setContextMenuPolicy(Qt.CustomContextMenu)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"border-bottom: 3px solid rgb(255, 61, 75);\n"
"background-color: rgb(42, 57, 66);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4px;\n"
"padding:10px;\n"
"	selection-background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(False)

        self.verticalLayout_6.addWidget(self.comboBox)

        self.lineEdit = QLineEdit(self.frame_14)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setFont(font3)
        self.lineEdit.setToolTipDuration(-1)
        self.lineEdit.setStyleSheet(u"border-bottom: 3px solid rgb(255, 61, 75);\n"
"background-color: rgb(42, 57, 66);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4px;\n"
"")
        self.lineEdit.setFrame(False)
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.lineEdit)

        self.pushButton_9 = QPushButton(self.frame_14)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setFamilies([u"Horyzen"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.pushButton_9.setFont(font4)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(63, 86, 99);\n"
"border: 2px solid rgb(255, 61, 75);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/img/key.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon9)
        self.pushButton_9.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.pushButton_9)


        self.gridLayout_2.addWidget(self.frame_14, 2, 1, 1, 1)

        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_15)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.frame_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 200))
        self.label_3.setMaximumSize(QSize(200, 200))
        self.label_3.setStyleSheet(u"border-radius:100px;\n"
"background-color: rgb(42, 57, 66);")
        self.label_3.setPixmap(QPixmap(u":/img/circle-user.png"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame_15)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setMaximumSize(QSize(16777215, 20))
        font5 = QFont()
        font5.setFamilies([u"Horyzen"])
        font5.setPointSize(18)
        font5.setBold(True)
        self.label_4.setFont(font5)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_15, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_10, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_12)


        self.horizontalLayout_6.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_16 = QFrame(self.page_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 80))
        self.frame_16.setMaximumSize(QSize(16777215, 80))
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_18)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"padding-left:10px;\n"
"border-bottom: 3px solid rgb(255, 61, 75);")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_5)


        self.horizontalLayout_8.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_19)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"padding-left:5px;\n"
"padding-right:10px;\n"
"border-bottom: 3px solid rgb(255, 61, 75);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 0))
        font6 = QFont()
        font6.setFamilies([u"Horyzen"])
        font6.setPointSize(11)
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"padding-left:10px;\n"
"border-bottom: 3px solid rgb(255, 61, 75);")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_8)


        self.horizontalLayout_8.addWidget(self.frame_19)


        self.verticalLayout_7.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.page_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"#frame_20{\n"
"background-color: rgba(255, 255, 255, 50);\n"
"padding-left:10px;\n"
"}\n"
"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy3)
        self.frame_22.setStyleSheet(u"QLabel{\n"
"padding-left:4px;\n"
"padding-bottom:0px;\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.frame_22)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_10)

        self.comboBox_2 = QComboBox(self.frame_22)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(300, 40))
        font7 = QFont()
        font7.setFamilies([u"Horyzen"])
        font7.setPointSize(14)
        self.comboBox_2.setFont(font7)
        self.comboBox_2.setEditable(True)

        self.verticalLayout_10.addWidget(self.comboBox_2)


        self.horizontalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_20 = QLabel(self.frame_22)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.verticalLayout_26.addWidget(self.label_20)

        self.lineEdit_12 = QLineEdit(self.frame_22)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setEnabled(True)
        self.lineEdit_12.setMinimumSize(QSize(0, 40))
        self.lineEdit_12.setFont(font4)
        self.lineEdit_12.setFrame(False)

        self.verticalLayout_26.addWidget(self.lineEdit_12)


        self.horizontalLayout_12.addLayout(self.verticalLayout_26)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.frame_22)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_11)

        self.lineEdit_4 = QLineEdit(self.frame_22)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 40))
        self.lineEdit_4.setFont(font4)
        self.lineEdit_4.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_4.setFrame(False)

        self.verticalLayout_11.addWidget(self.lineEdit_4)


        self.horizontalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.frame_22)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_12)

        self.lineEdit_5 = QLineEdit(self.frame_22)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setMinimumSize(QSize(0, 40))
        self.lineEdit_5.setFont(font4)
        self.lineEdit_5.setFrame(False)

        self.verticalLayout_12.addWidget(self.lineEdit_5)


        self.horizontalLayout_12.addLayout(self.verticalLayout_12)

        self.pushButton_11 = QPushButton(self.frame_22)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy4)
        self.pushButton_11.setMinimumSize(QSize(64, 40))
        self.pushButton_11.setMaximumSize(QSize(1000, 1000))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(255,61,35);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/img/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon10)
        self.pushButton_11.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.pushButton_11)


        self.verticalLayout_9.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_23)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, -1, 0)
        self.tableWidget = QTableWidget(self.frame_23)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        font8 = QFont()
        font8.setFamilies([u"Horyzen"])
        font8.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font8);
        __qtablewidgetitem.setBackground(QColor(0, 0, 0, 0));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font8);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font8);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font8);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font8);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font8);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 220);")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_13.addWidget(self.tableWidget)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 20))
        font9 = QFont()
        font9.setFamilies([u"Horyzen"])
        font9.setPointSize(10)
        self.frame_24.setFont(font9)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)

        self.label_25 = QLabel(self.frame_24)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font8)

        self.horizontalLayout_14.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_24)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font8)

        self.horizontalLayout_14.addWidget(self.label_26)

        self.line = QFrame(self.frame_24)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(10)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout_14.addWidget(self.line)

        self.label_21 = QLabel(self.frame_24)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font8)

        self.horizontalLayout_14.addWidget(self.label_21)

        self.label_24 = QLabel(self.frame_24)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font8)

        self.horizontalLayout_14.addWidget(self.label_24)

        self.line_2 = QFrame(self.frame_24)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(10)
        self.line_2.setFrameShape(QFrame.VLine)

        self.horizontalLayout_14.addWidget(self.line_2)

        self.label_23 = QLabel(self.frame_24)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font8)

        self.horizontalLayout_14.addWidget(self.label_23)

        self.label_22 = QLabel(self.frame_24)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font8)

        self.horizontalLayout_14.addWidget(self.label_22)


        self.verticalLayout_13.addWidget(self.frame_24)


        self.verticalLayout_9.addWidget(self.frame_23)


        self.horizontalLayout_11.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_17)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(450, 0))
        self.frame_21.setMaximumSize(QSize(500, 16777215))
        self.frame_21.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"padding-left:2px;\n"
"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_21)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.frame_21)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font8)
        self.label_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_8.addWidget(self.label_7)

        self.lineEdit_2 = QLineEdit(self.frame_21)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setMinimumSize(QSize(0, 50))
        self.lineEdit_2.setFont(font8)
        self.lineEdit_2.setStyleSheet(u"	background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_8.addWidget(self.lineEdit_2)

        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font8)
        self.label_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_8.addWidget(self.label_9)

        self.lineEdit_3 = QLineEdit(self.frame_21)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 50))
        self.lineEdit_3.setFont(font8)
        self.lineEdit_3.setStyleSheet(u"	background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_8.addWidget(self.lineEdit_3)

        self.label_27 = QLabel(self.frame_21)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font8)
        self.label_27.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_8.addWidget(self.label_27)

        self.lineEdit_13 = QLineEdit(self.frame_21)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setEnabled(False)
        self.lineEdit_13.setMinimumSize(QSize(0, 50))
        self.lineEdit_13.setFont(font8)
        self.lineEdit_13.setStyleSheet(u"	background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_8.addWidget(self.lineEdit_13)

        self.frame_31 = QFrame(self.frame_21)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_31)

        self.pushButton_10 = QPushButton(self.frame_21)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 40))
        self.pushButton_10.setFont(font4)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(63, 86, 99);\n"
"border: 2px solid rgb(255, 61, 75);\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_10)

        self.frame_29 = QFrame(self.frame_21)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_29)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_28 = QLabel(self.frame_29)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font8)
        self.label_28.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_28.addWidget(self.label_28)

        self.textEdit = QTextEdit(self.frame_29)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setFont(font8)

        self.verticalLayout_28.addWidget(self.textEdit)


        self.verticalLayout_8.addWidget(self.frame_29)

        self.pushButton_15 = QPushButton(self.frame_21)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(0, 40))
        self.pushButton_15.setFont(font4)
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(63, 86, 99);\n"
"border: 2px solid rgb(255, 61, 75);\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_15)


        self.horizontalLayout_11.addWidget(self.frame_21)


        self.verticalLayout_7.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_14 = QVBoxLayout(self.page_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_25 = QFrame(self.page_3)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_25)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy3.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy3)
        self.frame_26.setStyleSheet(u"QLabel{\n"
"padding-left:4px;\n"
"padding-bottom:0px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"#frame_26{\n"
"background-color: rgba(255, 255, 255, 50);\n"
"padding-left:10px;\n"
"border-bottom: 3px solid rgb(255, 61, 75);\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_13 = QLabel(self.frame_26)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_13)

        self.comboBox_3 = QComboBox(self.frame_26)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy2.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy2)
        self.comboBox_3.setMinimumSize(QSize(300, 40))
        self.comboBox_3.setFont(font7)
        self.comboBox_3.setEditable(True)

        self.verticalLayout_15.addWidget(self.comboBox_3)


        self.horizontalLayout_13.addLayout(self.verticalLayout_15)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_17 = QLabel(self.frame_26)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.verticalLayout_20.addWidget(self.label_17)

        self.lineEdit_9 = QLineEdit(self.frame_26)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_9.setMinimumSize(QSize(0, 40))
        self.lineEdit_9.setFont(font4)
        self.lineEdit_9.setFrame(False)

        self.verticalLayout_20.addWidget(self.lineEdit_9)


        self.horizontalLayout_13.addLayout(self.verticalLayout_20)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.frame_26)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_14)

        self.lineEdit_6 = QLineEdit(self.frame_26)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 40))
        self.lineEdit_6.setFont(font4)
        self.lineEdit_6.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_6.setFrame(False)

        self.verticalLayout_16.addWidget(self.lineEdit_6)


        self.horizontalLayout_13.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_15 = QLabel(self.frame_26)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.verticalLayout_17.addWidget(self.label_15)

        self.lineEdit_7 = QLineEdit(self.frame_26)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_7.setMinimumSize(QSize(0, 40))
        self.lineEdit_7.setFont(font4)
        self.lineEdit_7.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_7.setFrame(False)

        self.verticalLayout_17.addWidget(self.lineEdit_7)


        self.horizontalLayout_13.addLayout(self.verticalLayout_17)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_16 = QLabel(self.frame_26)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_19.addWidget(self.label_16)

        self.lineEdit_8 = QLineEdit(self.frame_26)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setEnabled(True)
        self.lineEdit_8.setMinimumSize(QSize(0, 40))
        self.lineEdit_8.setFont(font4)
        self.lineEdit_8.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_8.setFrame(False)

        self.verticalLayout_19.addWidget(self.lineEdit_8)


        self.horizontalLayout_13.addLayout(self.verticalLayout_19)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_18 = QLabel(self.frame_26)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.verticalLayout_21.addWidget(self.label_18)

        self.lineEdit_10 = QLineEdit(self.frame_26)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setEnabled(True)
        self.lineEdit_10.setMinimumSize(QSize(0, 40))
        self.lineEdit_10.setFont(font4)
        self.lineEdit_10.setFrame(False)

        self.verticalLayout_21.addWidget(self.lineEdit_10)


        self.horizontalLayout_13.addLayout(self.verticalLayout_21)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_19 = QLabel(self.frame_26)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.verticalLayout_24.addWidget(self.label_19)

        self.lineEdit_11 = QLineEdit(self.frame_26)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setEnabled(True)
        self.lineEdit_11.setMinimumSize(QSize(0, 40))
        self.lineEdit_11.setFont(font4)
        self.lineEdit_11.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.lineEdit_11.setFrame(False)

        self.verticalLayout_24.addWidget(self.lineEdit_11)


        self.horizontalLayout_13.addLayout(self.verticalLayout_24)

        self.pushButton_12 = QPushButton(self.frame_26)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy4)
        self.pushButton_12.setMinimumSize(QSize(64, 40))
        self.pushButton_12.setMaximumSize(QSize(1000, 1000))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(255,61,35);\n"
"}")
        self.pushButton_12.setIcon(icon10)
        self.pushButton_12.setIconSize(QSize(32, 32))

        self.horizontalLayout_13.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frame_26)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy4.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy4)
        self.pushButton_13.setMinimumSize(QSize(64, 40))
        self.pushButton_13.setMaximumSize(QSize(1000, 1000))
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(255,61,35);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/img/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon11)
        self.pushButton_13.setIconSize(QSize(32, 32))

        self.horizontalLayout_13.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_26)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy4.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy4)
        self.pushButton_14.setMinimumSize(QSize(64, 40))
        self.pushButton_14.setMaximumSize(QSize(1000, 1000))
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(255,61,35);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/img/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon12)
        self.pushButton_14.setIconSize(QSize(32, 32))

        self.horizontalLayout_13.addWidget(self.pushButton_14)


        self.verticalLayout_18.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"#frame_27{\n"
"background-color: rgba(255, 255, 255, 50);\n"
"padding-left:10px;\n"
"border-bottom: 3px solid rgb(255, 61, 75);\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_27)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.tableWidget_2 = QTableWidget(self.frame_27)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font8);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font8);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font8);
        __qtablewidgetitem8.setBackground(QColor(0, 0, 0, 0));
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font8);
        __qtablewidgetitem9.setBackground(QColor(0, 0, 0, 0));
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font8);
        __qtablewidgetitem10.setBackground(QColor(0, 0, 0, 0));
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font8);
        __qtablewidgetitem11.setBackground(QColor(0, 0, 0, 0));
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font8);
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font8);
        __qtablewidgetitem13.setBackground(QColor(0, 0, 0, 0));
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 220);")
        self.tableWidget_2.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_25.addWidget(self.tableWidget_2)


        self.verticalLayout_18.addWidget(self.frame_27)


        self.verticalLayout_14.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_23 = QVBoxLayout(self.page_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_28 = QFrame(self.page_4)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"#frame_27{\n"
"background-color: rgba(255, 255, 255, 50);\n"
"padding-left:10px;\n"
"border-bottom: 3px solid rgb(255, 61, 75);\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_28)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_29 = QLabel(self.frame_28)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 40))
        self.label_29.setMaximumSize(QSize(16777215, 40))
        self.label_29.setFont(font7)
        self.label_29.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"padding-left:5px;\n"
"padding-right:10px;\n"
"border-bottom: 3px solid rgb(255, 61, 75);")

        self.verticalLayout_22.addWidget(self.label_29)

        self.tableWidget_4 = QTableWidget(self.frame_28)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font8);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font8);
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font8);
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font8);
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font8);
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        sizePolicy2.setHeightForWidth(self.tableWidget_4.sizePolicy().hasHeightForWidth())
        self.tableWidget_4.setSizePolicy(sizePolicy2)
        self.tableWidget_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 220);")

        self.verticalLayout_22.addWidget(self.tableWidget_4)

        self.line_3 = QFrame(self.frame_28)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_22.addWidget(self.line_3)

        self.frame_32 = QFrame(self.frame_28)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy4.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy4)
        self.frame_32.setMaximumSize(QSize(16777215, 40))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_32)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 40))
        self.label_30.setMaximumSize(QSize(16777215, 40))
        self.label_30.setFont(font7)
        self.label_30.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"padding-left:5px;\n"
"padding-right:10px;\n"
"border-bottom: 3px solid rgb(255, 61, 75);")

        self.horizontalLayout_15.addWidget(self.label_30)

        self.line_4 = QFrame(self.frame_32)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_15.addWidget(self.line_4)

        self.label_32 = QLabel(self.frame_32)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 40))
        self.label_32.setFont(font7)
        self.label_32.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"padding-left:5px;\n"
"padding-right:10px;\n"
"border-bottom: 3px solid rgb(255, 61, 75);")

        self.horizontalLayout_15.addWidget(self.label_32)


        self.verticalLayout_22.addWidget(self.frame_32)

        self.tableWidget_3 = QTableWidget(self.frame_28)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font8);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font8);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font8);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font8);
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font8);
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        sizePolicy2.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy2)
        self.tableWidget_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 220);")

        self.verticalLayout_22.addWidget(self.tableWidget_3)


        self.verticalLayout_23.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 60);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.page_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_30 = QFrame(self.page_5)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_30)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.gridLayout_4.addWidget(self.frame_30, 1, 1, 1, 1)

        self.label_36 = QLabel(self.page_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 40))
        self.label_36.setMaximumSize(QSize(16777215, 40))
        self.label_36.setFont(font7)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_36, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_27 = QVBoxLayout(self.page_6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_36 = QFrame(self.page_6)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 16777215))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(400, 600))
        self.frame_37.setStyleSheet(u"#frame_37{\n"
"	background-color: rgba(255, 255, 255, 60);\n"
"}\n"
"*{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_37)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_31 = QLabel(self.frame_37)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 40))
        self.label_31.setFont(font7)
        self.label_31.setStyleSheet(u"padding-left:5px;\n"
"padding-right:10px;\n"
"border-bottom: 3px solid rgb(255, 61, 75);")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_31)

        self.groupBox = QGroupBox(self.frame_37)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font8)
        self.verticalLayout_31 = QVBoxLayout(self.groupBox)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.tableWidget_5 = QTableWidget(self.groupBox)
        if (self.tableWidget_5.columnCount() < 2):
            self.tableWidget_5.setColumnCount(2)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font8);
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font8);
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 220);")

        self.verticalLayout_31.addWidget(self.tableWidget_5)


        self.verticalLayout_30.addWidget(self.groupBox)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_38)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_33 = QLabel(self.frame_38)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 30))
        font10 = QFont()
        font10.setFamilies([u"Horyzen"])
        font10.setPointSize(9)
        self.label_33.setFont(font10)

        self.horizontalLayout_17.addWidget(self.label_33)

        self.lineEdit_14 = QLineEdit(self.frame_38)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(0, 30))
        self.lineEdit_14.setFont(font8)
        self.lineEdit_14.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.lineEdit_14)


        self.verticalLayout_32.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_34 = QLabel(self.frame_38)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 30))
        self.label_34.setFont(font10)

        self.horizontalLayout_18.addWidget(self.label_34)

        self.lineEdit_15 = QLineEdit(self.frame_38)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(0, 30))
        self.lineEdit_15.setFont(font8)
        self.lineEdit_15.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lineEdit_15.setEchoMode(QLineEdit.Password)
        self.lineEdit_15.setClearButtonEnabled(True)

        self.horizontalLayout_18.addWidget(self.lineEdit_15)


        self.verticalLayout_32.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_35 = QLabel(self.frame_38)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 30))
        self.label_35.setFont(font10)

        self.horizontalLayout_19.addWidget(self.label_35)

        self.lineEdit_16 = QLineEdit(self.frame_38)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 30))
        self.lineEdit_16.setFont(font8)
        self.lineEdit_16.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lineEdit_16.setEchoMode(QLineEdit.Password)
        self.lineEdit_16.setClearButtonEnabled(True)

        self.horizontalLayout_19.addWidget(self.lineEdit_16)


        self.verticalLayout_32.addLayout(self.horizontalLayout_19)

        self.groupBox_2 = QGroupBox(self.frame_38)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font9)
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font9)

        self.horizontalLayout_20.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font9)
        self.radioButton.setChecked(True)

        self.horizontalLayout_20.addWidget(self.radioButton)


        self.verticalLayout_32.addWidget(self.groupBox_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_2)

        self.pushButton_16 = QPushButton(self.frame_38)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 40))
        self.pushButton_16.setFont(font4)
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"	background-color: rgb(42, 57, 66);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(63, 86, 99);\n"
"border: 2px solid rgb(255, 61, 75);\n"
"}")

        self.verticalLayout_32.addWidget(self.pushButton_16)


        self.verticalLayout_30.addWidget(self.frame_38)


        self.horizontalLayout_16.addWidget(self.frame_37)


        self.verticalLayout_27.addWidget(self.frame_36)

        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setStyleSheet(u"background-color: rgb(32, 44, 51);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_6.setDefault(False)
        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_37.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u" SUMANASIRI HARDWARE", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"  Cashier", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"  Inventory", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"  Transactions", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"  Statistics", None))
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Please Login", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Passward", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"  Enter", None))
#if QT_CONFIG(shortcut)
        self.pushButton_9.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cash Invoice", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Invoice No :", None))
        self.label_8.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.comboBox_2.setCurrentText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Item Code", None))
        self.lineEdit_12.setPlaceholderText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.pushButton_11.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_11.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Item Code", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Unit Price", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Types Of Units :", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"All Quantity :", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Total Price :", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cash Recived", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Done", None))
#if QT_CONFIG(shortcut)
        self.pushButton_10.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Recommendation", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
#if QT_CONFIG(shortcut)
        self.pushButton_15.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Item Code", None))
        self.lineEdit_9.setPlaceholderText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Cost Price", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Sales Price", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Suplier Name", None))
        self.lineEdit_10.setPlaceholderText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Suplier Email", None))
        self.lineEdit_11.setPlaceholderText("")
        self.pushButton_12.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_12.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_13.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_13.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_14.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_14.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Item Code", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Stock Quantity", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Unit Buy Price", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Unit Sell Price", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Supplier Name", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Supplier E-mail", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Invoices", None))
        ___qtablewidgetitem14 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Invoice Number", None));
        ___qtablewidgetitem15 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem16 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem17 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Total Amount", None));
        ___qtablewidgetitem18 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Invoice Details", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Invoice Number", None))
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Iteam Code", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Iteam Name", None));
        ___qtablewidgetitem21 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem22 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Unit Sold price", None));
        ___qtablewidgetitem23 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Total Price", None));
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Profit Chart", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Users", None))
        ___qtablewidgetitem24 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"User Name", None));
        ___qtablewidgetitem25 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Priority", None));
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"New User Name", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Name Passward", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Reenter Passward", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Priority level", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Cashier", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Done", None))
#if QT_CONFIG(shortcut)
        self.pushButton_16.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

