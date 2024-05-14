from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import sys
from tree_recognition import MyTreeRecognition

app = QApplication(sys.argv)

window = MyTreeRecognition()

window.show()
app.exec()