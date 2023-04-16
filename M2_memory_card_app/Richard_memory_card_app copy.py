#pt1 :)))))))))))))))))))))))))))))))))))))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QGroupBox, QRadioButton, 
                             QVBoxLayout, QHBoxLayout, 
                             QLabel, QButtonGroup)
from random import shuffle, randint

app = QApplication([])
mywindow = QWidget()
mywindow.setWindowTitle("Memory Card")
mywindow.resize(400,300)
mywindow.setStyleSheet("font: bold 14px; background-color: #D8BFD8;")
mywindow.move(600,300)

#Create a class for question
class Question():
    def __init__(self, question, right_ans, wrong1,wrong2,wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2 
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Which element does not exist?','Nivonium','Argon','Radium','Ferrum'))
question_list.append(Question("Which is the answer to 10 to the power of -3?",'0.001','0.0001','0.01','1.00'))
question_list.append(Question("What is the scientific name for a pig?",'Sus','Porkedecues','Bos taurus','Scorpius Domesticus'))
question_list.append(Question('What is East in Bahasa Melayu?','Timur','Timur Laut','Tenggara','Barat'))
question_list.append(Question('What is number 4 in binary?','100','001','010','011'))
question_list.append(Question('Whichword is spelled correctly?','osmosis','ocmosic','ossmosis','ossmocis'))
question_list.append(Question('How old is Najib in 2023?','70','69','68','67'))

#fucntion
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('answer')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Next question')

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_Correct.setText('The correct answer is '+ q.right_ans)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Correct!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')

def show_correct(res):
    lb_Result.setText(res)
    show_result()

mywindow.cur_question = -1 
question_order = list(range(0, len(question_list)))

def next_question():
    mywindow.total += 1
    mywindow.cur_question = mywindow.cur_question + 1
    if mywindow.cur_question >= len(question_list):
        shuffle(question_order)
        mywindow.cur_question = 0 
        mywindow.score = 0
        mywindow.total = 1
    pick = question_order[mywindow.cur_question]
    q = question_list[pick]
    ask(q)

def click_OK():
    ''' This determines whether to show another question or check the answer to this question. '''
    if btn_ok.text() == 'Answer':
        check_answer() # check the answer
    else:
        next_question() # next question


def test():
    if btn_ok.text() == 'answer':
        if mywindow.cur_question == 0:
            shuffle(question_order)
        check_answer()
    else:
        show_question()

lb_question = QLabel('Which element does not exist?')
btn_ok = QPushButton('Answer')

RadioGroupBox = QGroupBox("Answer options")
rbtn_1 = QRadioButton("Radium")
rbtn_2 = QRadioButton("Argon")
rbtn_3 = QRadioButton("Rubidium")
rbtn_4 = QRadioButton("Nivovium")

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

box_layout = QHBoxLayout()
column_left = QVBoxLayout()
column_right = QVBoxLayout()
column_left.addWidget(rbtn_1)
column_left.addWidget(rbtn_3)
column_right.addWidget(rbtn_2)
column_right.addWidget(rbtn_4)
box_layout.addLayout(column_left)
box_layout.addLayout(column_right)
RadioGroupBox.setLayout(box_layout)

#day 2 :l
AnsGroupBox = QGroupBox("Correct Answer:")
lb_Result = QLabel('Nivovium')
lb_Correct = QLabel('Nivovium is not an element.')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch =2)
AnsGroupBox.setLayout(layout_res)

layout_card = QVBoxLayout()
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(AnsGroupBox)
layout_line2.addWidget(RadioGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok)
layout_line3.addStretch(1)

layout_card.addLayout(layout_line1)
layout_card.addStretch(1)
layout_card.addLayout(layout_line2)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3)

mywindow.setLayout(layout_card)

#program_run

mywindow.cur_question = -1  
mywindow.score = 0
mywindow.total = 0

btn_ok.clicked.connect(click_OK)
mywindow.show()
app.exec()