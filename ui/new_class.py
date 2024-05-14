# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_class.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(397, 528)
        Dialog.setStyleSheet(u"background-color: rgb(0,104,77);")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(237,253,246);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_add = QLabel(self.frame)
        self.lbl_add.setObjectName(u"lbl_add")
        self.lbl_add.setStyleSheet(u"color: rgb(0,104,77);\n"
"font-weight: bold;\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_add.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_add)

        self.lbl_class = QLineEdit(self.frame)
        self.lbl_class.setObjectName(u"lbl_class")
        self.lbl_class.setStyleSheet(u"background-color: rgba(0,104,77, 50);\n"
"font-size: 15pt;\n"
"color: rgb(0,104,77);\n"
"padding: 5px 10px;\n"
"")

        self.verticalLayout.addWidget(self.lbl_class)

        self.lbl_name_class = QLineEdit(self.frame)
        self.lbl_name_class.setObjectName(u"lbl_name_class")
        self.lbl_name_class.setStyleSheet(u"background-color: rgba(0,104,77, 50);\n"
"font-size: 15pt;\n"
"color: rgb(0,104,77);\n"
"padding: 5px 10px;")

        self.verticalLayout.addWidget(self.lbl_name_class)

        self.lbl_descriprion = QLineEdit(self.frame)
        self.lbl_descriprion.setObjectName(u"lbl_descriprion")
        self.lbl_descriprion.setStyleSheet(u"background-color: rgba(0,104,77, 50);\n"
"font-size: 15pt;\n"
"color: rgb(0,104,77);\n"
"padding: 5px 10px;")

        self.verticalLayout.addWidget(self.lbl_descriprion)

        self.lbl_height = QLineEdit(self.frame)
        self.lbl_height.setObjectName(u"lbl_height")
        self.lbl_height.setStyleSheet(u"background-color: rgba(0,104,77, 50);\n"
"font-size: 15pt;\n"
"color: rgb(0,104,77);\n"
"padding: 5px 10px;")

        self.verticalLayout.addWidget(self.lbl_height)

        self.lbl_age = QLineEdit(self.frame)
        self.lbl_age.setObjectName(u"lbl_age")
        self.lbl_age.setStyleSheet(u"background-color: rgba(0,104,77, 50);\n"
"font-size: 15pt;\n"
"color: rgb(0,104,77);\n"
"padding: 5px 10px;")

        self.verticalLayout.addWidget(self.lbl_age)

        self.lbl_radius_root_system = QLineEdit(self.frame)
        self.lbl_radius_root_system.setObjectName(u"lbl_radius_root_system")
        self.lbl_radius_root_system.setStyleSheet(u"background-color: rgba(0,104,77, 50);\n"
"font-size: 15pt;\n"
"color: rgb(0,104,77);\n"
"padding: 5px 10px;")

        self.verticalLayout.addWidget(self.lbl_radius_root_system)

        self.lbl_water_consumption = QLineEdit(self.frame)
        self.lbl_water_consumption.setObjectName(u"lbl_water_consumption")
        self.lbl_water_consumption.setStyleSheet(u"background-color: rgba(0,104,77, 50);\n"
"font-size: 15pt;\n"
"color: rgb(0,104,77);\n"
"padding: 5px 10px;")

        self.verticalLayout.addWidget(self.lbl_water_consumption)

        self.lbl_trunc_girth = QLineEdit(self.frame)
        self.lbl_trunc_girth.setObjectName(u"lbl_trunc_girth")
        self.lbl_trunc_girth.setStyleSheet(u"background-color: rgba(0,104,77, 50);\n"
"font-size: 15pt;\n"
"color: rgb(0,104,77);\n"
"padding: 5px 10px;")

        self.verticalLayout.addWidget(self.lbl_trunc_girth)

        self.lbl_volume_wood = QLineEdit(self.frame)
        self.lbl_volume_wood.setObjectName(u"lbl_volume_wood")
        self.lbl_volume_wood.setStyleSheet(u"background-color: rgba(0,104,77, 50);\n"
"font-size: 15pt;\n"
"color: rgb(0,104,77);\n"
"padding: 5px 10px;")

        self.verticalLayout.addWidget(self.lbl_volume_wood)

        self.lbl_flowering_season = QLineEdit(self.frame)
        self.lbl_flowering_season.setObjectName(u"lbl_flowering_season")
        self.lbl_flowering_season.setStyleSheet(u"background-color: rgba(0,104,77, 50);\n"
"font-size: 15pt;\n"
"color: rgb(0,104,77);\n"
"padding: 5px 10px;")

        self.verticalLayout.addWidget(self.lbl_flowering_season)

        self.btm_add_class = QPushButton(self.frame)
        self.btm_add_class.setObjectName(u"btm_add_class")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.btm_add_class.setFont(font)
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

        self.verticalLayout.addWidget(self.btm_add_class)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_add.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043a\u043b\u0430\u0441\u0441", None))
        self.lbl_class.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u0430\u0441\u0441", None))
        self.lbl_name_class.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u0430\u0441\u0441\u0430", None))
        self.lbl_descriprion.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.lbl_height.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0440\u0435\u0434\u043d\u0438\u044e \u0432\u044b\u0441\u043e\u0442\u0443", None))
        self.lbl_age.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0440\u0435\u0434\u043d\u0438\u0439 \u0432\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.lbl_radius_root_system.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0440\u0435\u0434\u043d\u0438\u0439 \u0440\u0430\u0434\u0438\u0443\u0441 \u043a\u043e\u0440\u043d\u0435\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u044b", None))
        self.lbl_water_consumption.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u043f\u043e\u0442\u0440\u0435\u0431\u043b\u0435\u043d\u0438\u0435 \u0432\u043e\u0434\u044b", None))
        self.lbl_trunc_girth.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0440\u0435\u0434\u043d\u0438\u0439 \u043e\u0431\u0445\u0432\u0430\u0442 \u0434\u0435\u0440\u0435\u0432\u0430", None))
        self.lbl_volume_wood.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0440\u0435\u0434\u043d\u0438\u0439 \u043e\u0431\u044a\u0451\u043c \u0434\u0440\u0435\u0432\u0435\u0441\u0438\u043d\u044b", None))
        self.lbl_flowering_season.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0435\u0437\u043e\u043d \u0446\u0432\u0435\u0442\u0435\u043d\u0438\u044f", None))
        self.btm_add_class.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

