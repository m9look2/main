from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from random import shuffle, choice
from time import sleep

app = QApplication([])

from memoCardLayout import *
from menu_window import *

class Question:
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_ans1
        self.wrong_answer2 = wrong_ans2
        self.wrong_answer3 = wrong_ans3
        self.actual = True
        self.count_asked = 0
        self.count_right = 0

    def got_right(self):
        self.count_asked += 1
        self.count_right += 1

    def got_wrong(self):
        self.count_asked += 1


q1 = Question('Яблуко', 'apple', 'application', 'apex', 'alice')
q2 = Question('Будинок', 'house', 'hour', 'hellicopter', 'hero')
q3 = Question('Число', 'number', 'nubabwe', 'noob', 'minus')
q4 = Question('Сонце', 'sun', 'son', 'sunshine', 'smurf')
cur_q = ''  #!!!!!!!!!!!!!!!!!!!!!!!!

radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
question = [q1, q2, q3, q4]


def new_question():
    global cur_q
    cur_q = choice(question)
    lb_Question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)


new_question()
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                cur_q.got_right()
                lb_Result.setText('Вірно!')
                answer.setChecked(False)
                break
            else:
                lb_Result.setText('Не вірно!')
                cur_q.got_wrong()
    RadioGroup.setExclusive(True)


def click_ok():
    if btn_OK.text() == 'Відповісти':
        check()
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне запитання')
    else:
        new_question()
        AnsGroupBox.hide()
        RadioGroupBox.show()
        btn_OK.setText('Відповісти')

def rest():
    win_card.hide()
    n = box_Minutes.value() * 60
    sleep(n)
    win_card.show()

def menu_generation():
    win_card.hide()
    menu_win.show()

def back_menu():
    menu_win.hide()
    win_card.show()

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    question.append(new_q)
    clear()

btn_add_question.clicked.connect(add_question)
btn_clear.clicked.connect(clear)
btn_menu.clicked.connect(menu_generation)
btn_back.clicked.connect(back_menu)
btn_OK.clicked.connect(click_ok)
btn_Sleep.clicked.connect(rest)

win_card.show()
app.exec()