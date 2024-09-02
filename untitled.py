from mtranslate import translate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
import requests
import json
import urllib.request
import pyperclip
from PyQt5.QtGui import QIcon

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # "항상 위" 속성을 설정합니다.
        Form.setWindowFlags(QtCore.Qt.WindowType.Window | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        Form.resize(700, 300)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pre = QtWidgets.QTextEdit(Form)
        self.pre.setObjectName("pre")
        self.horizontalLayout_2.addWidget(self.pre)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.pushButton.clicked.connect(self.ts) 
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def ts(self):
        # 버튼 비활성화
        self.pushButton.setEnabled(False)
        t = self.pre.toPlainText()

        try:
            result = translate(t, "en", "ko")

            self.textEdit_2.setText(result)
            pyperclip.copy(result)
        except Exception as e:
            print(e)  # 예외 메시지 출력
        finally:
            # 버튼을 다시 활성화
            self.pushButton.setEnabled(True)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "번역기"))
        Form.setWindowIcon(QIcon('web.png'))
        self.pushButton.setText(_translate("Form", "translate"))
        self.pushButton.setShortcut("Ctrl+F")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
