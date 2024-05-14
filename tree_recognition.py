from ui.ui_tree_recognition import Ui_MainWindow
from ui.new_class import Ui_Dialog
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog
from PySide6.QtSql import QSqlTableModel
from PySide6.QtGui import QPixmap
from connection import Data
from PIL import Image
from prediction import Predictor
import torch

class MyTreeRecognition(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Tree Recognition Application")
        self.conn = Data()
        self.view_data()
        self.predictor = Predictor("full_model.pth")

        self.ui.btm_add_class.clicked.connect(self.open_new_class_window)
        self.ui.btm_edit_class.clicked.connect(self.open_new_class_window)
        self.ui.delete_class.clicked.connect(self.delete_current_class)

        self.button = self.findChild(QPushButton, "open_image")
        self.label = self.findChild(QLabel, "load_photo")
        self.button.clicked.connect(self.clicker)
        self.ui.determine_type.clicked.connect(self.upload_data_from_db)

        self.ui.icon_name_widget.setHidden(True)

        self.ui.how_1.clicked.connect(self.switch_to_howPage)
        self.ui.how_2.clicked.connect(self.switch_to_howPage)

        self.ui.tree_1.clicked.connect(self.switch_to_treePage)
        self.ui.tree_2.clicked.connect(self.switch_to_treePage)

        self.ui.database_1.clicked.connect(self.switch_to_databasePage)
        self.ui.database_2.clicked.connect(self.switch_to_databasePage)

    def upload_data_from_db(self):
        pixmap = self.label.pixmap()
        image = pixmap.toImage()
        pil_image = Image.fromqimage(image)

        class_probabilities = self.predictor.predict(pil_image)

        keys_list = list(class_probabilities.keys())
        class_id1 = keys_list[0]
        ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9 = self.conn.upload_data(class_id1)

        ans1, ans2, ans3 = self.conn.upload_data_about_name(keys_list[0], keys_list[1], keys_list[2])

        tree_names = [ans1, ans2, ans3]
        answer = ""
        for i in range(len(class_probabilities)):
            key_list = list(class_probabilities.keys())
            tree_name = tree_names[i]
            probability = class_probabilities.get(key_list[i], 0)
            answer += f"   –  {tree_name}: {probability:.0f}%\n"
        self.ui.lbl_description.setText("Описание:")
        self.ui.results_analisys.setText("Результаты анализа")
        self.ui.type_tree_final_2.setText("Вид дерева:")
        self.ui.lbl_charateristics.setText("Параметры и свойства:")
        self.ui.lbl_height.setText("Высота:")
        self.ui.lbl_age.setText("Возраст:")
        self.ui.lbl_root_system.setText("Радиус корневой системы:")
        self.ui.lbl_water_consumption.setText("Потребление воды в день:")
        self.ui.lbl_trunk_girth.setText("Средний обхват ствола:")
        self.ui.lbl_volume_wood.setText("Объём древесины:")
        self.ui.lbl_flowering.setText("Сезон цветения:")
        self.ui.explanation_1.setText("(Для взрослого дерева данного вида)")
        self.ui.explanation_2.setText("(Для взрослого дерева данного вида)")
        self.ui.explanation_3.setText("(Для взрослого дерева данного вида)")
        self.ui.explanation_4.setText("(Для взрослого дерева данного вида)")
        self.ui.type_tree_final.setText(answer)
        self.ui.description.setText(ans_2)
        self.ui.height.setText(ans_3)
        self.ui.age.setText(ans_4)
        self.ui.root_system.setText(ans_5)
        self.ui.water_consumption.setText(ans_6)
        self.ui.trunk_girth.setText(ans_7)
        self.ui.volume_wood.setText(ans_8)
        self.ui.flowering.setText(ans_9)

    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "PNG Files (*.png);; JPEG Files (*.jpeg);; JPG Files (*.jpg)")

        self.pixmap = QPixmap(fname[0])
        self.label.setPixmap(self.pixmap)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('trees')
        self.model.select()
        self.ui.database_table.setModel(self.model)

    def open_new_class_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        sender = self.sender()
        if sender.text() == "  Добавить класс":
            self.ui_window.btm_add_class.clicked.connect(self.add_new_class)
        else:
            self.ui_window.btm_add_class.clicked.connect(self.edit_current_class)

    def add_new_class(self):
        class_id = self.ui_window.lbl_class.text()
        class_name = self.ui_window.lbl_name_class.text()
        description = self.ui_window.lbl_descriprion.text()
        height = self.ui_window.lbl_height.text()
        age = self.ui_window.lbl_age.text()
        radius_root_system = self.ui_window.lbl_radius_root_system.text()
        water_consumption = self.ui_window.lbl_water_consumption.text()
        trunk_girth = self.ui_window.lbl_trunc_girth.text()
        volume_wood = self.ui_window.lbl_volume_wood.text()
        flowering_season = self.ui_window.lbl_flowering_season.text()

        self.conn.add_new_class_query(class_id, class_name, description, height, age,
                                      radius_root_system, water_consumption,
                                      trunk_girth, volume_wood, flowering_season)
        self.view_data()
        self.new_window.close()

    def edit_current_class(self):
        index = self.ui.database_table.selectedIndexes()[0]
        class_id = str(self.ui.database_table.model().data(index))

        class_name = self.ui_window.lbl_name_class.text()
        description = self.ui_window.lbl_descriprion.text()
        height = self.ui_window.lbl_height.text()
        age = self.ui_window.lbl_age.text()
        radius_root_system = self.ui_window.lbl_radius_root_system.text()
        water_consumption = self.ui_window.lbl_water_consumption.text()
        trunk_girth = self.ui_window.lbl_trunc_girth.text()
        volume_wood = self.ui_window.lbl_volume_wood.text()
        flowering_season = self.ui_window.lbl_flowering_season.text()

        self.conn.update_class_query(class_id, class_name, description, height, age, radius_root_system,
                                     water_consumption, trunk_girth, volume_wood, flowering_season)
        self.view_data()
        self.new_window.close()

    def delete_current_class(self):
        index = self.ui.database_table.selectedIndexes()[0]
        class_id = str(self.ui.database_table.model().data(index))

        self.conn.delete_class_query(class_id)
        self.view_data()
        self.new_window.close()

    def switch_to_howPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def switch_to_treePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def switch_to_databasePage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

