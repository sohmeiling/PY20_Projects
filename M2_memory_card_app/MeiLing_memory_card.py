#import modules
"""
For Python-14_2 class (Saturday, 11.30am)
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, #for app and window
    QLabel, QRadioButton, QPushButton, #Widgets
    QVBoxLayout, QHBoxLayout, #layout
    QGroupBox, QButtonGroup) #for grouping
from random import shuffle, randint

my_app = QApplication([])
my_win = QWidget()

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

"""
Set window properties
"""
my_win.setWindowTitle("Memory Card") #for title
my_win.resize(400, 300) #for size of the window
my_win.move (600, 300) #where the window appears
my_win.setStyleSheet("font: bold 14px; background-color: #D8BFD8;")

"""
Add widgets
"""
question = QLabel("Which nationality does not exist?")
question.setStyleSheet("font: Arial; bold 18px; color: white;")
optionA = QRadioButton("Enets")
optionB = QRadioButton("Chulyms")
optionC = QRadioButton("Smurfs")
optionD = QRadioButton("Aleuts")
button = QPushButton("Answer")

rating = QLabel("Rating score")
rating.setStyleSheet("font: bold 14px; color: red;")

"""
Create grouped Button (QButtonGroup)
"""
RadioGroup = QButtonGroup() 
RadioGroup.addButton(optionA)
RadioGroup.addButton(optionB)
RadioGroup.addButton(optionC)
RadioGroup.addButton(optionD)


"""
Create grouped answer panel
"""
ans_panel = QGroupBox("Answer options:")
ans_panel.setStyleSheet("font: bold 14px; color: black;")

ans_layout = QVBoxLayout()
ans_line1 = QHBoxLayout()
ans_line2 = QHBoxLayout()

ans_line1.addWidget(optionA, alignment= Qt.AlignLeft)
ans_line1.addWidget(optionB, alignment= Qt.AlignLeft)
ans_line2.addWidget(optionC, alignment= Qt.AlignLeft)
ans_line2.addWidget(optionD, alignment= Qt.AlignLeft)
ans_layout.addLayout(ans_line1)
ans_layout.addLayout(ans_line2)

ans_panel.setLayout(ans_layout)
"""
Create result panel
"""
lb_result = QLabel("True/False")
lb_correct = QLabel("Correct answer")

result_panel = QGroupBox("Test result")
result_panel.setStyleSheet("background-color: #00FF00;")

result_layout = QVBoxLayout()
result_layout.addWidget(lb_result, alignment= Qt.AlignLeft)
result_layout.addWidget(lb_correct, alignment= Qt.AlignCenter)

result_panel.setLayout(result_layout)


"""
The main layout for the card
"""
card_layout = QVBoxLayout()
line_1 = QHBoxLayout() # for question
line_2 = QHBoxLayout() # for grouped answer
line_3 = QHBoxLayout() # for rating scores
line_4 = QHBoxLayout() # for answer button

line_1.addWidget(question, alignment= Qt.AlignCenter)
line_2.addWidget(ans_panel)
line_2.addWidget(result_panel)
result_panel.hide() # hide the result panel because the question panel must be visible first
line_3.addWidget(rating, alignment= Qt.AlignLeft)
rating.hide() #hide ratings

line_4.addStretch(1)
line_4.addWidget(button, stretch= 1)
line_4.addStretch(1)

card_layout.addLayout(line_1)
card_layout.addStretch(1)
card_layout.addLayout(line_2)
card_layout.addLayout(line_3)
card_layout.addStretch(1)
card_layout.addLayout(line_4)
card_layout.addStretch(1)

my_win.setLayout(card_layout)

"""
Create functions for showing question and answers
"""
def show_result():
    ''' show answer panel '''
    ans_panel.hide()
    result_panel.show()
    rating.setText(f"Total correct = {my_win.score}/{len(questions_list)}")
    rating.show()
    button.setText('Next question')

def show_question():
    ''' show question panel '''
    ans_panel.show()
    result_panel.hide()
    rating.hide()
    button.setText('Answer')
    # clear selected radio button
    RadioGroup.setExclusive(False) # remove the limits so we can reset the radio buttons 
    optionA.setChecked(False)
    optionB.setChecked(False)
    optionC.setChecked(False)
    optionD.setChecked(False)
    RadioGroup.setExclusive(True) # reset the limits so that only one radio button can be selected at a time 

# def test():
#     ''' a temporary function that makes it possible to press a button to call up alternating
#     show_result() or show_question() '''
#     if button.text() == "Answer":
#         show_result()
#     else:
#         show_question()

"""
Functions to write the value of the question and answers in the corresponding widgets. The answer options are distributed randomly. 
"""
answers = [optionA, optionB, optionC, optionD]

def ask (q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.questions) #question
    lb_correct.setText(q.right_answer) #answer
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        my_win.score +=1
        show_correct('Correct!')
        print('Statistics\n-Total questions: ', my_win.total, '\n-Right answers: ', my_win.score)
        print('Rating: ', (my_win.score/my_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')
            print('Rating: ', (my_win.score/my_win.total*100), '%')

"""
Functions to generate new questions
"""

question_order = list(range(0, len(questions_list)))

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

def click_OK():
    if button.text() == "Answer":
        if my_win.cur_question == 0:
            shuffle(question_order)
        check_answer()
    else:
        next_question()

"""
Execute the window
"""
my_win.cur_question = -1  
my_win.score = 0
my_win.total = 0


button.clicked.connect(click_OK)
next_question()

my_win.show()
my_app.exec()
