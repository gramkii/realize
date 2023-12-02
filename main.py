from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import *
import time 

app = QApplication([])

#window = QWidget()
#window.setWindowTitle("Тренування друку")
#window.resize(700,500)


start_test = QPushButton("Почати тест")
restart_test = QPushButton("Спробувати знову")

user_input = QLineEdit()
word_label = QLabel("")
result = QLabel()

class Trainer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_Gui()
    
    def init_Gui(self):
        self.start_test = QPushButton("Почати тест", self)
        self.restart_test = QPushButton("Спробувати знову", self)

        self.user_input = QLineEdit(self)
        self.word_label = QLabel("", self)
        self.result = QLabel("", self)
        layout = QVBoxLayout()
        layout.addWidget(self.start_test)
        layout.addWidget(self.restart_test)
        layout.addWidget(self.user_input)
        layout.addWidget(self.word_label)
        layout.addWidget(self.result)
        self.setLayout(layout)
        self.resize(700, 500)
        self.show()

    def choose_word(self):
        choosed_word = choice(["skoro.txt", "skoro2.txt", "skoro3.txt", "skoro4.txt"])
        with open (choosed_word, "r", encoding="UTF-8") as file:
            word = file.read()

        return word

    def start_training(self):
        self.word_type = self.choose_word()
        self.word_label.setText(self.word_type)
        self.user_input.clear()
        self.result_label.clear()
        self.start_test(False)


trainer = Trainer()






#window.show()
app.exec_()