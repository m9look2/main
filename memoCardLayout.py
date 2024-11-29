''' Вікно для картки питання '''
from PyQt6.QtWidgets import (QWidget,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from PyQt6.QtCore import Qt

card_width, card_height = 600, 500
win_card = QWidget()



btn_menu = QPushButton('Меню')
btn_Sleep = QPushButton('Відпочити')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
lb_rest = QLabel('хвилин')
btn_OK = QPushButton('Відповісти')
lb_Question = QLabel('Питання') # текст питання

RadioGroupBox = QGroupBox('Варіанти відповіді')
RadioGroup = QButtonGroup()

rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

AnsGroupBox = QGroupBox('Результати тесту')
lb_Result = QLabel('') # рузультат правильно \ неправильно
lb_right_answer = QLabel('') # текст правльної відповіді


"""Layouts"""

# лайаут варінтів відповіді
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

# лайаут результатів
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop))
layout_res.addWidget(lb_right_answer, alignment= Qt.AlignmentFlag.AlignHCenter, stretch= 2)

AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

#Основний лайаут для вікна
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()


layout_line1.addWidget(btn_menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(lb_rest)


layout_line2.addWidget(lb_Question, alignment=(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter))


layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)


layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2)
layout_line4.addStretch(1)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch= 1)
layout_card.addLayout(layout_line2, stretch= 2)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch= 8)
layout_card.addLayout(layout_line4, stretch= 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

win_card.setLayout(layout_card)

win_card.resize(card_width, card_height)
win_card.move(500, 450)
win_card.setWindowTitle('Memory card')