from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QGroupBox,
 QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский',
 'Английский', 'Мспанский','Бразильский'))
question_list.append(Question('Какого цвета нет на флаге Росии?', 'Зелёный',
'Белый', 'Красный', 'Синий'))
question_list.append(Question('Национальная хижина якутов', 'Ураса',
 'Юрта', 'Иглу','Хата'))

app = QApplication([])
window = QWidget()

btn_OK = QPushButton("Ответить")
Ib_Question = QLabel("Какой национальности не существует?")

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чульмы")
rbtn_4 = QRadioButton("Алеуты")

RadioGroupBox = QButtonGroup()
RadioGroupBox.addButton(rbtn_1)
RadioGroupBox.addButton(rbtn_2)
RadioGroupBox.addButton(rbtn_3)
RadioGroupBox.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
Ib_Result = QLabel("Правильно или неправильно")
Ib_Correct = QLabel("Правильный ответ")

layout_res = QVBoxLayout()
layout_res.addWidget(Ib_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Ib_Correct, alignment=Qt.AlignHCenter)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addwidget(Ib_Question, alignment=(Qt.AlignHCenter | Qt.AlignvCenter))
layout_line2.addwidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.Widget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, strench=2)
layout_card.addLayout(layout_line2, strench=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, strench=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    ansGroupBox.show()
    btn_OK.setText("Следующий вопрос")

def show_question():
    RadioGroupBox.show()
    ansGroupBox.hide()
    btn_OK.setText("Ответить")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(question, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    Ib_Question.setText(question)
    Ib_Correct.setText(right_answer)
    show_question()



def show_correct(res):
    Ib_Result.setText(res)
    show_result()  

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
        window.score += 1
        print(f"Рейтинг: {round(window.score/window.total*100, 2)}%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно!")
            print(f"Рейтинг: {window.score/window.total*100}%")

def next_question():
    if len(question_list) > 0:
        cur_question = randint(0, len(question_list) - 1)
        q = question_list (cur_question)
        ask(g)
        question_list.pop(cur_question)
    else:
        victory_win = QMessageBox()
        victory_win.setText('ВЫ ОТВЕТИЛИ НА ВСЕ ВОПРОСЫ')
        victory_win.exec_()

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.setLayout(layout_card)
window.setWindowTitle("Memory Card")
ask("Государственный язык Бразилии", 'Португальский', 'Бразильский', 'Испанский','Маямский')
btn_OK.connnect(check_answer)
window.show()
app.exec_()