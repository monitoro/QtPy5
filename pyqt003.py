import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5 import uic

CalUI = '_uiFiles/calculator.ui'

class MainDialog(QDialog):
    def __init__(self): 
        QDialog.__init__(self,None)
        uic.loadUi(CalUI,self)

        # self.num_pushButton_1.clicked.connect(self.NumClicked) // 1번 버튼만 쓸때
        # self.num_pushButton_1.clicked.connect(self.NumClicked(button=self.num_pushButton_1))
        #  위 줄처럼 ()안에 들어갈 것은 함수자체여야 하는데.. ()button=self.num_pushButton_1가 다시 들어가면 실행을 의미한다.

        # 버튼 함수를 변수를 만들기 위해서 connect(.....())이렇게 넣었지만 에러 발생 따라서 lambda 함수 사용한다.
        # ()가 들어가면 함수가 실행되는 것이므로.. ()안에 넣어야하는 것은 실행된 함수가 아닌 함수 자체이기 때문에 이렇게 넣으면 안된다. 따라서..
        
        #  lambda 함수는 한줄로 함수를 만드는 역할을 한다. connect 뒤에 ()를 못쓴다. 왜?? 함수의 끝에 괄호를 붙이는건 함수의 실행을 의미함.
        self.num_pushButton_1.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        # 실행시 1번 버튼 클릭하면 멈춘다. 일단 'state'라는 변수를 추가해 준다.

        self.num_pushButton_2.clicked.connect(lambda state, button = self.num_pushButton_2 : self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button = self.num_pushButton_3 : self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button = self.num_pushButton_4 : self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button = self.num_pushButton_5 : self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button = self.num_pushButton_6 : self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button = self.num_pushButton_7 : self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button = self.num_pushButton_8 : self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button = self.num_pushButton_9 : self.NumClicked(state, button))
        self.num_pushButton_0.clicked.connect(lambda state, button = self.num_pushButton_0 : self.NumClicked(state, button))

        self.sign_pushButton_1.clicked.connect(lambda state, button = self.sign_pushButton_1 : self.NumClicked(state, button))
        self.sign_pushButton_2.clicked.connect(lambda state, button = self.sign_pushButton_2 : self.NumClicked(state, button))
        self.sign_pushButton_3.clicked.connect(lambda state, button = self.sign_pushButton_3 : self.NumClicked(state, button))
        self.sign_pushButton_4.clicked.connect(lambda state, button = self.sign_pushButton_4 : self.NumClicked(state, button))

        self.result_pushButton.clicked.connect(self.MakeResult)
        self.reset_pushButton.clicked.connect(self.Reset)
        self.del_pushButton.clicked.connect(self.Delete)

    def NumClicked(self, state, button):
        # print("나 클릭됐다!!")
        # print(self.num_pushButton_1.text())

        exist_line_text = self.q_lineEdit.text()
        now_num_text = button.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text )
 
    # def NumClicked2(self):
    #     # print("나 클릭됐다!!")
    #     # print(self.num_pushButton_1.text())

    #     exist_line_text = self.q_lineEdit.text()
    #     now_num_text = self.num_pushButton_2.text()
    #     self.q_lineEdit.setText(exist_line_text + now_num_text )

    def MakeResult(self):
        try:
            # eval 함수는 문자열의 수식을
            result = eval(self.q_lineEdit.text())
            print(result)
            print(type(result))
            self.a_lineEdit.setText(str(result))
        except Exception as e:
            print(e)
            pass
    def Reset(self):
        self.q_lineEdit.clear()
        self.a_lineEdit.setText('0')

    def Delete(self):
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

app.exec_()