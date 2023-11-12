from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
import time 

app = QApplication([])

window = QWidget()
window.setWindowTitle("Тренування друку")
window.resize(700,500)


start_test = QPushButton("Почати тест")
restart_test = QPushButton("Спробувати знову")
choose_text = QPushButton("Обрати текст")


window.show()
app.exec_()