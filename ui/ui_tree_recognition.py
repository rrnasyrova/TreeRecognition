# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tree_recognition.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QPushButton, QSizePolicy,
                               QSpacerItem, QStackedWidget, QTableView, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 674)
        MainWindow.setMaximumSize(QSize(1000, 16777215))
        MainWindow.setStyleSheet(u"background-color: #f0fcf6;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1100, 16777215))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(-1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_for_widget = QWidget(self.centralwidget)
        self.icon_only_for_widget.setObjectName(u"icon_only_for_widget")
        self.icon_only_for_widget.setMinimumSize(QSize(0, 0))
        self.icon_only_for_widget.setMaximumSize(QSize(16777215, 16777215))
        self.icon_only_for_widget.setStyleSheet(u"QWidget{\n"
"	background-color: #22664f;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: white;\n"
"	height: 40px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(237,253,246);\n"
"	color: rgb(0,104,77);\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_only_for_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 20, 12, 12)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.how_1 = QPushButton(self.icon_only_for_widget)
        self.how_1.setObjectName(u"how_1")
        self.how_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"images/how.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"images/how2.png", QSize(), QIcon.Normal, QIcon.On)
        self.how_1.setIcon(icon)
        self.how_1.setIconSize(QSize(37, 37))
        self.how_1.setCheckable(True)
        self.how_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.how_1)

        self.tree_1 = QPushButton(self.icon_only_for_widget)
        self.tree_1.setObjectName(u"tree_1")
        self.tree_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"images/tree.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u"images/tree2.png", QSize(), QIcon.Normal, QIcon.On)
        self.tree_1.setIcon(icon1)
        self.tree_1.setIconSize(QSize(35, 35))
        self.tree_1.setCheckable(True)
        self.tree_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.tree_1)

        self.database_1 = QPushButton(self.icon_only_for_widget)
        self.database_1.setObjectName(u"database_1")
        self.database_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"images/database.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"images/database2.png", QSize(), QIcon.Normal, QIcon.On)
        self.database_1.setIcon(icon2)
        self.database_1.setIconSize(QSize(35, 35))
        self.database_1.setCheckable(True)
        self.database_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.database_1)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(30, 338, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.icon_only_for_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setMaximumSize(QSize(16777215, 16777215))
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: #22664f;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(237,253,246);\n"
"	text-align: left;\n"
"	height: 40px;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(237,253,246);\n"
"	color: rgb(0,104,77);\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 20, 0, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, 20, -1)
        self.how_2 = QPushButton(self.icon_name_widget)
        self.how_2.setObjectName(u"how_2")
        font = QFont()
        font.setPointSize(16)
        font.setWeight(QFont.Medium)
        self.how_2.setFont(font)
        self.how_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.how_2.setIcon(icon)
        self.how_2.setIconSize(QSize(37, 37))
        self.how_2.setCheckable(True)
        self.how_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.how_2)

        self.tree_2 = QPushButton(self.icon_name_widget)
        self.tree_2.setObjectName(u"tree_2")
        self.tree_2.setFont(font)
        self.tree_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.tree_2.setIcon(icon1)
        self.tree_2.setIconSize(QSize(35, 35))
        self.tree_2.setCheckable(True)
        self.tree_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.tree_2)

        self.database_2 = QPushButton(self.icon_name_widget)
        self.database_2.setObjectName(u"database_2")
        self.database_2.setFont(font)
        self.database_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.database_2.setIcon(icon2)
        self.database_2.setIconSize(QSize(35, 35))
        self.database_2.setCheckable(True)
        self.database_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.database_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 351, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setMinimumSize(QSize(0, 0))
        self.main_menu.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu = QPushButton(self.main_menu)
        self.menu.setObjectName(u"menu")
        self.menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu.setStyleSheet(u"border: none;")
        icon3 = QIcon()
        icon3.addFile(u"images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon3)
        self.menu.setIconSize(QSize(45, 45))
        self.menu.setCheckable(True)
        self.menu.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.menu)

        self.horizontalSpacer_4 = QSpacerItem(288, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"background-color: white;")
        self.tree = QWidget()
        self.tree.setObjectName(u"tree")
        font1 = QFont()
        font1.setPointSize(15)
        self.tree.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.tree)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.load_photo = QLabel(self.tree)
        self.load_photo.setObjectName(u"load_photo")
        self.load_photo.setMaximumSize(QSize(400, 400))
        self.load_photo.setScaledContents(True)
        self.load_photo.setAlignment(Qt.AlignCenter)
        self.load_photo.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.load_photo)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_description = QLabel(self.tree)
        self.lbl_description.setObjectName(u"lbl_description")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.lbl_description.setFont(font2)
        self.lbl_description.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.lbl_description)

        self.horizontalSpacer = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.description = QLabel(self.tree)
        self.description.setObjectName(u"description")
        self.description.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(14)
        self.description.setFont(font3)
        self.description.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.description.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.description)


        self.gridLayout_2.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(38, 28, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.results_analisys = QLabel(self.tree)
        self.results_analisys.setObjectName(u"results_analisys")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.results_analisys.setFont(font4)
        self.results_analisys.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.results_analisys)

        self.horizontalSpacer_6 = QSpacerItem(28, 28, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.type_tree_final_2 = QLabel(self.tree)
        self.type_tree_final_2.setObjectName(u"type_tree_final_2")
        self.type_tree_final_2.setFont(font2)

        self.horizontalLayout_6.addWidget(self.type_tree_final_2)

        self.horizontalSpacer_3 = QSpacerItem(138, 28, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.type_tree_final = QLabel(self.tree)
        self.type_tree_final.setObjectName(u"type_tree_final")
        self.type_tree_final.setFont(font3)

        self.horizontalLayout_7.addWidget(self.type_tree_final)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_charateristics = QLabel(self.tree)
        self.lbl_charateristics.setObjectName(u"lbl_charateristics")
        self.lbl_charateristics.setFont(font2)

        self.horizontalLayout_8.addWidget(self.lbl_charateristics)

        self.horizontalSpacer_2 = QSpacerItem(38, 28, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_height = QLabel(self.tree)
        self.lbl_height.setObjectName(u"lbl_height")
        self.lbl_height.setMaximumSize(QSize(60, 16777215))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.lbl_height.setFont(font5)

        self.horizontalLayout_9.addWidget(self.lbl_height)

        self.height = QLabel(self.tree)
        self.height.setObjectName(u"height")
        self.height.setFont(font3)

        self.horizontalLayout_9.addWidget(self.height)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.explanation_1 = QLabel(self.tree)
        self.explanation_1.setObjectName(u"explanation_1")
        self.explanation_1.setMaximumSize(QSize(16777209, 11))
        font6 = QFont()
        font6.setPointSize(11)
        self.explanation_1.setFont(font6)
        self.explanation_1.setStyleSheet(u"color: #808080;")

        self.verticalLayout_8.addWidget(self.explanation_1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_age = QLabel(self.tree)
        self.lbl_age.setObjectName(u"lbl_age")
        self.lbl_age.setMaximumSize(QSize(70, 16777215))
        self.lbl_age.setFont(font5)

        self.horizontalLayout_10.addWidget(self.lbl_age)

        self.age = QLabel(self.tree)
        self.age.setObjectName(u"age")
        self.age.setFont(font3)

        self.horizontalLayout_10.addWidget(self.age)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.explanation_2 = QLabel(self.tree)
        self.explanation_2.setObjectName(u"explanation_2")
        self.explanation_2.setMaximumSize(QSize(16777209, 11))
        self.explanation_2.setFont(font6)
        self.explanation_2.setStyleSheet(u"color: #808080;")

        self.verticalLayout_8.addWidget(self.explanation_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_root_system = QLabel(self.tree)
        self.lbl_root_system.setObjectName(u"lbl_root_system")
        self.lbl_root_system.setMaximumSize(QSize(200, 16777215))
        self.lbl_root_system.setFont(font5)

        self.horizontalLayout_11.addWidget(self.lbl_root_system)

        self.root_system = QLabel(self.tree)
        self.root_system.setObjectName(u"root_system")
        self.root_system.setFont(font3)

        self.horizontalLayout_11.addWidget(self.root_system)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.explanation_3 = QLabel(self.tree)
        self.explanation_3.setObjectName(u"explanation_3")
        self.explanation_3.setMaximumSize(QSize(16777209, 11))
        self.explanation_3.setFont(font6)
        self.explanation_3.setStyleSheet(u"color: #808080;")

        self.verticalLayout_8.addWidget(self.explanation_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lbl_water_consumption = QLabel(self.tree)
        self.lbl_water_consumption.setObjectName(u"lbl_water_consumption")
        self.lbl_water_consumption.setMaximumSize(QSize(192, 16777215))
        self.lbl_water_consumption.setFont(font5)

        self.horizontalLayout_12.addWidget(self.lbl_water_consumption)

        self.water_consumption = QLabel(self.tree)
        self.water_consumption.setObjectName(u"water_consumption")
        self.water_consumption.setFont(font3)

        self.horizontalLayout_12.addWidget(self.water_consumption)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.explanation_4 = QLabel(self.tree)
        self.explanation_4.setObjectName(u"explanation_4")
        self.explanation_4.setMaximumSize(QSize(16777209, 11))
        self.explanation_4.setFont(font6)
        self.explanation_4.setStyleSheet(u"color: #808080;")

        self.verticalLayout_8.addWidget(self.explanation_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lbl_trunk_girth = QLabel(self.tree)
        self.lbl_trunk_girth.setObjectName(u"lbl_trunk_girth")
        self.lbl_trunk_girth.setMaximumSize(QSize(178, 16777215))
        self.lbl_trunk_girth.setFont(font5)

        self.horizontalLayout_13.addWidget(self.lbl_trunk_girth)

        self.trunk_girth = QLabel(self.tree)
        self.trunk_girth.setObjectName(u"trunk_girth")
        self.trunk_girth.setFont(font3)

        self.horizontalLayout_13.addWidget(self.trunk_girth)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lbl_volume_wood = QLabel(self.tree)
        self.lbl_volume_wood.setObjectName(u"lbl_volume_wood")
        self.lbl_volume_wood.setMaximumSize(QSize(135, 16777215))
        self.lbl_volume_wood.setFont(font5)

        self.horizontalLayout_14.addWidget(self.lbl_volume_wood)

        self.volume_wood = QLabel(self.tree)
        self.volume_wood.setObjectName(u"volume_wood")
        self.volume_wood.setFont(font3)

        self.horizontalLayout_14.addWidget(self.volume_wood)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lbl_flowering = QLabel(self.tree)
        self.lbl_flowering.setObjectName(u"lbl_flowering")
        self.lbl_flowering.setMaximumSize(QSize(120, 16777215))
        self.lbl_flowering.setFont(font5)
        self.lbl_flowering.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.lbl_flowering)

        self.flowering = QLabel(self.tree)
        self.flowering.setObjectName(u"flowering")
        self.flowering.setFont(font3)

        self.horizontalLayout_15.addWidget(self.flowering)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)


        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.open_image = QPushButton(self.tree)
        self.open_image.setObjectName(u"open_image")
        self.open_image.setEnabled(True)
        self.open_image.setFont(font2)
        self.open_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_image.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0,104,77);\n"
"	color: rgb(237,253,246);\n"
"	border: 1px solid rgba(237,253,246, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,104,77, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(0,104,77, 250);\n"
"}")
        self.open_image.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.open_image)

        self.determine_type = QPushButton(self.tree)
        self.determine_type.setObjectName(u"determine_type")
        self.determine_type.setFont(font2)
        self.determine_type.setCursor(QCursor(Qt.PointingHandCursor))
        self.determine_type.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0,104,77);\n"
"	color: rgb(237,253,246);\n"
"	border: 1px solid rgba(237,253,246, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,104,77, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(0,104,77, 250);\n"
"}")

        self.horizontalLayout_2.addWidget(self.determine_type)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.tree)
        self.database = QWidget()
        self.database.setObjectName(u"database")
        self.verticalLayout_7 = QVBoxLayout(self.database)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btm_add_class = QPushButton(self.database)
        self.btm_add_class.setObjectName(u"btm_add_class")
        self.btm_add_class.setFont(font5)
        self.btm_add_class.setCursor(QCursor(Qt.PointingHandCursor))
        self.btm_add_class.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0,104,77);\n"
"	color: rgb(237,253,246);\n"
"	border: 1px solid rgba(237,253,246, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,104,77, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(0,104,77, 250);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"images/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btm_add_class.setIcon(icon4)
        self.btm_add_class.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btm_add_class)

        self.btm_edit_class = QPushButton(self.database)
        self.btm_edit_class.setObjectName(u"btm_edit_class")
        self.btm_edit_class.setFont(font5)
        self.btm_edit_class.setCursor(QCursor(Qt.PointingHandCursor))
        self.btm_edit_class.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0,104,77);\n"
"	color: rgb(237,253,246);\n"
"	border: 1px solid rgba(237,253,246, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,104,77, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(0,104,77, 250);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"images/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btm_edit_class.setIcon(icon5)
        self.btm_edit_class.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btm_edit_class)

        self.delete_class = QPushButton(self.database)
        self.delete_class.setObjectName(u"delete_class")
        self.delete_class.setFont(font5)
        self.delete_class.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_class.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0,104,77);\n"
"	color: rgb(237,253,246);\n"
"	border: 1px solid rgba(237,253,246, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,104,77, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(0,104,77, 250);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"images/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_class.setIcon(icon6)
        self.delete_class.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.delete_class)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.database_table = QTableView(self.database)
        self.database_table.setObjectName(u"database_table")
        self.database_table.setStyleSheet(u"QTableView{\n"
"	background-color: rgb(237,253,246);\n"
"	border: 1px solid rgb(0,104,77);\n"
"	border-bottom-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section{\n"
"	background-color: rgb(0,104,77);\n"
"	color:  rgb(237,253,246);\n"
"	border: none;\n"
"	height: 100px;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item{\n"
"	border-style: none;\n"
"	border-bottom: rgb(0,104,77);\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(237,253,246);\n"
"	background-color: rgba(0,104,77, 250);\n"
"}")
        self.database_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.database_table.horizontalHeader().setVisible(False)
        self.database_table.horizontalHeader().setDefaultSectionSize(87)
        self.database_table.verticalHeader().setVisible(False)

        self.verticalLayout_6.addWidget(self.database_table)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.database)
        self.how = QWidget()
        self.how.setObjectName(u"how")
        self.gridLayout_3 = QGridLayout(self.how)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.label = QLabel(self.how)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_9)

        self.label_2 = QLabel(self.how)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_10)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.label_4 = QLabel(self.how)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_4)

        self.label_3 = QLabel(self.how)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_3)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_11)

        self.label_5 = QLabel(self.how)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_5)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_12)


        self.verticalLayout_10.addLayout(self.horizontalLayout_18)

        self.label_6 = QLabel(self.how)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_6)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_13)

        self.label_7 = QLabel(self.how)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_7)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_14)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.label_8 = QLabel(self.how)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_8)


        self.gridLayout_3.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.how)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_for_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.database_1.toggled.connect(self.database_2.setChecked)
        self.tree_1.toggled.connect(self.tree_2.setChecked)
        self.how_1.toggled.connect(self.how_2.setChecked)
        self.database_2.toggled.connect(self.database_1.setChecked)
        self.tree_2.toggled.connect(self.tree_1.setChecked)
        self.how_2.toggled.connect(self.how_1.setChecked)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.how_1.setText("")
        self.tree_1.setText("")
        self.database_1.setText("")
        self.how_2.setText(QCoreApplication.translate("MainWindow", u"  \u041a\u0430\u043a \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c?", None))
        self.tree_2.setText(QCoreApplication.translate("MainWindow", u"  \u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0432\u0438\u0434\u0430    ", None))
        self.database_2.setText(QCoreApplication.translate("MainWindow", u"   \u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.menu.setText("")
        self.load_photo.setText("")
        self.lbl_description.setText("")
        self.description.setText("")
        self.results_analisys.setText("")
        self.type_tree_final_2.setText("")
        self.type_tree_final.setText("")
        self.lbl_charateristics.setText("")
        self.lbl_height.setText("")
        self.height.setText("")
        self.explanation_1.setText("")
        self.lbl_age.setText("")
        self.age.setText("")
        self.explanation_2.setText("")
        self.lbl_root_system.setText("")
        self.root_system.setText("")
        self.explanation_3.setText("")
        self.lbl_water_consumption.setText("")
        self.water_consumption.setText("")
        self.explanation_4.setText("")
        self.lbl_trunk_girth.setText("")
        self.trunk_girth.setText("")
        self.lbl_volume_wood.setText("")
        self.volume_wood.setText("")
        self.lbl_flowering.setText("")
        self.flowering.setText("")
        self.open_image.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.determine_type.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0432\u0438\u0434", None))
        self.btm_add_class.setText(QCoreApplication.translate("MainWindow", u"  \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043b\u0430\u0441\u0441", None))
        self.btm_edit_class.setText(QCoreApplication.translate("MainWindow", u"  \u041e\u0442\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u043b\u0430\u0441\u0441", None))
        self.delete_class.setText(QCoreApplication.translate("MainWindow", u"  \u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u043b\u0430\u0441\u0441", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0441 \u0441\u0438\u0441\u0442\u0435\u043c\u043e\u0439?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043a\u043e\u0432\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e \u0434\u043b\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439, \u043a\u043e\u0442\u043e\u0440\u044b\u043c <span style=\" font-weight:700;\">\u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u043e \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0432\u0438\u0434 \u0434\u0435\u0440\u0435\u0432\u0430</span> \u0438 \u0435\u0433\u043e <span style=\" font-weight:700;\">\u043e\u0441\u043d\u043e\u0432\u044b\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438</span>. \u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0435\u0442 <span style=\" font-weight:700;\">39 \u0432\u0438\u0434\u043e\u0432 \u0434\u0435\u0440\u0435\u0432\u044c"
                        "\u0435\u0432</span>.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438 \u0435\u0441\u0442\u044c <span style=\" font-weight:700;\">3 \u043e\u0441\u043d\u043e\u0432\u044b\u0445 \u044d\u043a\u0440\u0430\u043d\u0430</span>: </p><p>\u2013 <span style=\" font-family:'YS Text','-apple-system','system-ui','Arial','Helvetica','sans-serif'; font-size:14px; font-weight:700; color:#333333; background-color:#ffffff;\">\u00ab</span><span style=\" font-weight:700;\">\u041a\u0430\u043a \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c?</span><span style=\" font-family:'YS Text','-apple-system','system-ui','Arial','Helvetica','sans-serif'; font-size:14px; font-weight:700; color:#333333; background-color:#ffffff;\">\u00bb</span> \u2013 <span style=\" font-weight:700;\">\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f</span> \u043f\u043e \u0440\u0430\u0431\u043e\u0442\u0435 \u0441 \u0441\u0438\u0441\u0442\u0435\u043c\u043e\u0439</p><p>\u2013 <span style=\" font-family:'YS Text','-apple-system','syst"
                        "em-ui','Arial','Helvetica','sans-serif'; font-weight:700; color:#333333; background-color:#ffffff;\">\u00ab</span><span style=\" font-weight:700;\">\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0432\u0438\u0434\u0430</span><span style=\" font-family:'YS Text','-apple-system','system-ui','Arial','Helvetica','sans-serif'; font-weight:700; color:#333333; background-color:#ffffff;\">\u00bb</span> \u2013 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430, \u0432 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u043c\u043e\u0436\u043d\u043e <span style=\" font-weight:700;\">\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435</span> \u0438 <span style=\" font-weight:700;\">\u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e</span> \u043e \u043d\u0435\u043c</p><p>\u2013 <span style=\" font-family:'YS Text','-apple-system','system-ui','Arial','Helvetica','sans-serif'; font-weig"
                        "ht:700; color:#333333; background-color:#ffffff;\">\u00ab</span><span style=\" font-weight:700;\">\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445</span><span style=\" font-family:'YS Text','-apple-system','system-ui','Arial','Helvetica','sans-serif'; font-weight:700; color:#333333; background-color:#ffffff;\">\u00bb</span> \u2013 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0434\u043b\u044f \u043f\u0440\u043e\u0444. \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f, \u0433\u0434\u0435 \u043c\u043e\u0436\u043d\u043e <span style=\" font-weight:700;\">\u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0442\u044c, \u0443\u0434\u0430\u043b\u044f\u0442\u044c \u0438 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c</span> \u0432 \u0411\u0414 \u043e \u0434\u0435\u0440\u0435\u0432\u044c\u044f\u0445</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0432\u0438\u0434\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">1) \u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0437\u0430\u0439\u0442\u0438 \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439 \u0440\u0430\u0437\u0434\u0435\u043b <span style=\" font-family:'YS Text','-apple-system','system-ui','Arial','Helvetica','sans-serif'; font-size:14px; font-weight:700; color:#333333; background-color:#ffffff;\">\u00ab\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0432\u0438\u0434\u0430\u00bb</span> .</p><p align=\"justify\">2) \u041d\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-family:'YS Text','-apple-system','system-ui','Arial','Helvetica','sans-serif'; font-size:14px; font-weight:700; color:#333333; background-color:#ffffff;\">\u00ab\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435\u00bb</span>, \u043e\u0442\u043a\u0440\u043e\u0435\u0442\u0441"
                        "\u044f \u043f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a \u0438 \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b (\u043c\u043e\u0436\u043d\u043e \u0437\u0430\u0433\u0440\u0443\u0436\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e .png, .jpg, .jpeg).</p><p align=\"justify\">3) \u0417\u0430\u0442\u0435\u043c \u043d\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-family:'YS Text','-apple-system','system-ui','Arial','Helvetica','sans-serif'; font-size:14px; font-weight:700; color:#333333; background-color:#ffffff;\">\u00ab\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u044c \u0432\u0438\u0434\u00bb</span>.</p><p>\u0414\u043b\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0445 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0439 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e <span style=\" font-weight:700;\">\u043f\u043e\u0432\u0442\u043e\u0440\u044f\u0442\u044c \u0442\u043e\u0442"
                        " \u0436\u0435 \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439</span>.</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">\u0414\u0430\u043d\u043d\u044b\u0439 \u0440\u0430\u0437\u0434\u0435\u043b \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c \u043f\u0440\u043e\u0444. \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c.</p><p align=\"justify\">\u2013 \u0427\u0442\u043e\u0431\u044b <span style=\" font-weight:700;\">\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0437\u0430\u043f\u0438\u0441\u044c \u0432 \u0411\u0414</span>, \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043d\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u00ab\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043b\u0430\u0441\u0441\u00bb \u0438 \u0437\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044f \u0432 \u043c\u043e\u0434\u0430\u043b\u044c\u043d\u043e\u043c \u043e\u043a\u043d\u0435.</p><p align=\"justify\">\u2013 \u0427\u0442\u043e\u0431\u044b <span style=\" font-weight:700;\">\u0440\u0435\u0434\u0430\u043a\u0442"
                        "\u0438\u0440\u043e\u0432\u0430\u0442\u044c </span>\u0438<span style=\" font-weight:700;\"> \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c \u0432 \u0411\u0414</span>, \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u043d\u0443\u0436\u043d\u044b\u0439 id \u0437\u0430\u043f\u0438\u0441\u0438 \u0438 \u043d\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0443\u044e \u043a\u043d\u043e\u043f\u043a\u0443.</p></body></html>", None))
    # retranslateUi

