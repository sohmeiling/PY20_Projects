from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QGroupBox,QRadioButton,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QButtonGroup)
from random import shuffle, randint

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle("Memory Card")
my_win.resize(400,300)

class Question():
    def __init__(self,question,right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []

question_list.append(Question("Who own Los Pollos Hermanos?","Gustavo Fring","Walter White","Hank Schrader","Lalo Salamanca"))
question_list.append(Question("What is 9*9?","81","420","911","234543"))
question_list.append(Question("What is the temperature of the boiling point of water?","100","0","-34567","9000"))
question_list.append(Question("Who is the most handsome man in the universe?","Rizzard of Oz","Chin Yi Kai","You","John Pork"))
question_list.append(Question("Who sang 'Die very Rough'?","Mario Judah","Rick Astley","Dwayne Johnson","GigaNigga"))


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Answer')
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

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_Correct.setText("The correct answer is:" + q.right_answer)
    show_question()

def test():
    if btn_ok.text() == "Answer":
        show_result()
    else:
        show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct("Correct!")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Incorrect!")

question_order = list(range(0, len(question_list)))

def next_question():
    my_win.total += 1
    my_win.cur_question = my_win.cur_question + 1 
    if my_win.cur_question >= len(question_list):
        shuffle(question_order)
        my_win.cur_question = 0 
        my_win.score = 0
        my_win.total = 1
    pick = question_order[my_win.cur_question]
    q = question_list[pick]
    ask(q)

def click_OK():
    ''' This determines whether to show another question or check the answer to this question. '''
    if btn_ok.text() == 'Answer':
        check_answer() # check the answer
    else:
        next_question() # next question

lb_question = QLabel('SUS')
btn_ok = QPushButton('Answer')

RadioGroupBox = QGroupBox("Answer options") # group on the screen for radio buttons with answers
rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Chulyums')
rbtn_3 = QRadioButton('Smurfs')
rbtn_4 = QRadioButton('Aluets')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

box_layout = QHBoxLayout()
column_1 = QVBoxLayout()
column_2 = QVBoxLayout()
column_1.addWidget(rbtn_1)
column_1.addWidget(rbtn_2)
column_2.addWidget(rbtn_3)
column_2.addWidget(rbtn_4)
box_layout.addLayout(column_1)
box_layout.addLayout(column_2)
RadioGroupBox.setLayout(box_layout)


#my_win.setLayout(main_layout)

AnsGroupBox = QGroupBox("Test Result")
lb_Result = QLabel("True/False")
lb_Correct = QLabel("The correct answer is ...")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
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

# -------------------------------Window setup -----------------------------
my_win.score = 0
my_win.total = 0
my_win.cur_question = -1  

btn_ok.clicked.connect(click_OK)
next_question()

my_win.show()
app.exec_()