from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, 
                            QHBoxLayout, QWidget, 
                            QGroupBox, QRadioButton, 
                            QPushButton, QLabel,
                            QButtonGroup)
from random import shuffle, randint

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle("Memory Card")
my_win.resize(400, 300)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = list() #To create a list, you can also use square bracket

question_list.append(Question("What is 21 + 34?", "55", "54", "51", "65"))
question_list.append(Question("What is 12 x 11?", "132", "121", "1211", "144"))
question_list.append(Question("What is the cube root of 2197?", "13", "14", "12", "11"))
question_list.append(Question("What is 7² +  9²?", "130", "140", "170", "16²"))
question_list.append(Question("What is 3 to the power of 6?", "729", "829", "18", "829²"))
question_list.append(Question("What is 5 factorial (5!)?", "120", "110", "15", "5"))
question_list.append(Question("If the value of y is 20, find x while 2y + x = 72.", "32", "16", "2y", "20"))
question_list.append(Question("Expand the brackets: 2m(4m + 7) - 3m(2m - 4)", "2m² + 26m", "2m + 26m", "2m² - 26m", "2m - 26m"))

questions_order = randint(0, len(question_list) - 1)

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("Answer")
    RadioGroup.setExclusive(False) # removed the restrictions so as to reset the radio button choice
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # returned the restrictions, now only one radio button can be selected

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Next Question')

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question() # show question panel 

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Correct!')
        my_win.score +=1
        print('Statistics\n-Total questions: ', my_win.total, "/", len(question_list), '\n-Right answers: ', my_win.score)
        print('Rating: ', (my_win.score/my_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')
            print('Rating: ', (my_win.score/my_win.total*100), '%')


def next_question():
    my_win.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q) 

def click_OK():
    if btn_ok.text() == 'Answer':
        check_answer() 
    else:
        next_question() 

lb_question = QLabel("Which nationality does not exist?")
btn_ok = QPushButton("Answer")

RadioGroupBox = QGroupBox("Answer options") 
rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Chulyms')
rbtn_3 = QRadioButton('Smurfs')
rbtn_4 = QRadioButton('Aleuts')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

box_layout = QHBoxLayout()
columnleft = QVBoxLayout()
columnright = QVBoxLayout()

columnleft.addWidget(rbtn_1)
columnleft.addWidget(rbtn_3)
columnright.addWidget(rbtn_2)
columnright.addWidget(rbtn_4)

box_layout.addLayout(columnleft)
box_layout.addLayout(columnright)

RadioGroupBox.setLayout(box_layout)

#my_win.setLayout(main_layout)

AnsGroupBox = QGroupBox("Test result")
lb_result = QLabel("True/False")
lb_Correct = QLabel("The correct answer is...")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
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

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
my_win.score = 0
my_win.total = 0

next_question()
btn_ok.clicked.connect(click_OK)

my_win.show()
app.exec_()