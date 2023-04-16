from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QVBoxLayout, QHBoxLayout)

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle("Memory Card")
my_win.resize(400,300)

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

def test():
    if btn_ok.text() == "Answer":
        show_result()
    else:
        show_question()

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
btn_ok.clicked.connect(test)
my_win.show()
app.exec_()