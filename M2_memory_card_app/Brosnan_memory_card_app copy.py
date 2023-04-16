from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, 
                             QButtonGroup, QRadioButton, QPushButton, 
                             QLabel, QVBoxLayout, QHBoxLayout)
from random import shuffle, randint

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle("Memory Card")
my_win.resize(400,300)

# Create a class for question
class Question():
    def __init__(self, questions, right_answer, wrong1, wrong2, wrong3):
        self.questions = questions
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

#Questions
questions_list = []
questions_list.append(Question("What is the national language for Malaysia?", "Malay", "English", "Mandarin", "Tamil"))
questions_list.append(Question('Official language of Brazil', 'Portuguese', 'English', 'Spanish', 'Brazilian'))
questions_list.append(Question('Which color does not appear on the American flag?', 'Green', 'Red', 'White', 'Blue'))
questions_list.append(Question('A traditional residence of the Yakut people', 'Urasa', 'Yurt', 'Igloo', 'Hut')) 

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("Answer")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Next question")

def show_correct(res):
    Ib_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        my_win.score +=1
        show_correct('Correct!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')

question_order = list(range(0, len(questions_list)))

def click_OK():
    if btn_ok.text() == "Answer":
        if my_win.cur_question == 0:
            shuffle(question_order)
        check_answer()
    else:
        next_question()

def ask (q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.questions) #question
    Ib_Correct.setText(q.right_answer) #answer
    show_question()

def next_question():
    my_win.total += 1
    my_win.cur_question = my_win.cur_question + 1 
    if my_win.cur_question >= len(questions_list):
        shuffle(question_order)
        my_win.cur_question = 0 
        my_win.score = 0
        my_win.total = 1
    pick = question_order[my_win.cur_question]
    q = questions_list[pick]
    ask(q)

lb_question = QLabel("When was the first play button given too?")
btn_ok = QPushButton("Answer")

RadioGroupBox= QGroupBox("Answer options")
rbtn_1 = QRadioButton('2009')
rbtn_2 = QRadioButton('2016')
rbtn_3 = QRadioButton('2015')
rbtn_4 = QRadioButton('2012')
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

box_layout = QHBoxLayout()
colum_left = QVBoxLayout()
colum_right = QVBoxLayout()
colum_left.addWidget(rbtn_1)
colum_left.addWidget(rbtn_3)
colum_right.addWidget(rbtn_2)
colum_right.addWidget(rbtn_4)
box_layout.addLayout(colum_left)
box_layout.addLayout(colum_right)
RadioGroupBox.setLayout(box_layout)


#my_win.setlayout(main_layout)
AnsGroupBox = QGroupBox("Test result")
Ib_Result = QLabel("True/False")
Ib_Correct = QLabel("The correct answer is 2012")

layout_res = QVBoxLayout()
layout_res.addWidget(Ib_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Ib_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_card = QVBoxLayout()
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))  
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

my_win.setLayout(layout_card)
# ------------------ Main ------------------
my_win.cur_question = -1  
my_win.score = 0
my_win.total = 0

btn_ok.clicked.connect(click_OK)
next_question()

my_win.show()
app.exec_()