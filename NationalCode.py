from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
# I used these two libraries to shorten and to define shortcuts
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
import codecs


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 200)
        MainWindow.setMinimumSize(QtCore.QSize(424, 200))
        MainWindow.setMaximumSize(QtCore.QSize(424, 200))
        font = QtGui.QFont()
        font.setFamily("B Nasim")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 10, 421, 91))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.NationalCode_entery = QtWidgets.QLineEdit(self.frame)
        self.NationalCode_entery.setEnabled(True)
        self.NationalCode_entery.setGeometry(QtCore.QRect(80, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.NationalCode_entery.setFont(font)
        self.NationalCode_entery.setCursor(
            QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.NationalCode_entery.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NationalCode_entery.setStyleSheet("QLineEdit{\n"
                                               "    border: 1px solid black;\n"
                                               "    border-radius: 8px;\n"
                                               "    \n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 249, 0, 255), stop:0.772816 rgba(255, 255, 255, 255));\n"
                                               "    padding: 2px\n"
                                               "}\n"
                                               "QLineEdit{\n"
                                               "    border-color: white;\n"
                                               "}")
        self.NationalCode_entery.setText("")
        self.NationalCode_entery.setFrame(False)
        self.NationalCode_entery.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.NationalCode_entery.setReadOnly(False)
        self.NationalCode_entery.setObjectName("NationalCode_entery")
        self.NationalCodeL = QtWidgets.QLabel(self.frame)
        self.NationalCodeL.setGeometry(QtCore.QRect(200, -10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.NationalCodeL.setFont(font)
        self.NationalCodeL.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.NationalCodeL.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.NationalCodeL.setWordWrap(True)
        self.NationalCodeL.setObjectName("NationalCodeL")
        self.Sehatsanji_Button = QtWidgets.QPushButton(self.frame)
        self.Sehatsanji_Button.setGeometry(QtCore.QRect(170, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("B Kamran")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Sehatsanji_Button.setFont(font)
        self.Sehatsanji_Button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Sehatsanji_Button.setObjectName("Sehatsanji_Button")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(9, 100, 411, 81))
        self.frame_2.setMaximumSize(QtCore.QSize(550, 500))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Sehat_Tozihat = QtWidgets.QLineEdit(self.frame_2)
        self.Sehat_Tozihat.setGeometry(QtCore.QRect(20, 30, 381, 31))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Sehat_Tozihat.setFont(font)
        self.Sehat_Tozihat.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Sehat_Tozihat.setStyleSheet("QLineEdit{\n"
                                         "    border: 1px solid black;\n"
                                         "    border-radius: 8px;\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 249, 0, 255), stop:0.772816 rgba(255, 255, 255, 255));\n"
                                         "}\n"
                                         "QLineEdit{\n"
                                         "    border-color: white;\n"
                                         "}")
        self.Sehat_Tozihat.setInputMask("")
        self.Sehat_Tozihat.setText("")
        self.Sehat_Tozihat.setFrame(False)
        self.Sehat_Tozihat.setAlignment(QtCore.Qt.AlignCenter)
        self.Sehat_Tozihat.setReadOnly(True)
        self.Sehat_Tozihat.setObjectName("Sehat_Tozihat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # Button activity definition and shortcut definition for A
        self.Sehatsanji_Button.setShortcut(QKeySequence(Qt.Key_Enter))
        self.Sehatsanji_Button.clicked.connect(
            self.NationalCode)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.NationalCode_entery,
                               self.Sehatsanji_Button)
        MainWindow.setTabOrder(self.Sehatsanji_Button, self.Sehat_Tozihat)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "صحت سنجی کدملی (حقیقی)"))
        self.NationalCodeL.setText(_translate(
            "MainWindow", "کد ملی مورد نظر را وارد نمایید ⬅️"))
        self.Sehatsanji_Button.setText(
            _translate("MainWindow", "صحت سنجی"))

    def NationalCode(self):
        try:

            try:
                a = str (self.NationalCode_entery.text())
                # Checking for the number of digits of the national code entered
                if len(a) != 10:
                    a = self.Sehat_Tozihat.setText("کد ملی باید 10 رقم باشد ")

                # Checking so that the entered numbers of the national code are not duplicated
                if a == "000000000" or a == "1111111111" or a == "2222222222" or a == "3333333333" or a == "4444444444" or a == "5555555555" or a == "6666666666" or a == "7777777777" or a == "8888888888" or a == "9999999999"  or a == 9876543219:
                    
                    a = self.Sehat_Tozihat.setText("کد ملی وارد شده صحیح نیست")

                # The main formula for calculating the national code

                if len(a)==10:
                    x=[int(a[0])*10,int(a[1])*9,int(a[2])*8,int(a[3])*7,int(a[4])*6,int(a[5])*5,int(a[6])*4,int(a[7])*3,int(a[8])*2]
                    end=(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8])%11
                    
                    if (end == int(a[9])) or ((11-end) == int(a[-1])):
                        a = self.Sehat_Tozihat.setText("کد ملی وارد شده صحیح است")
                    else:
                        a = self.Sehat_Tozihat.setText("کد ملی وارد شده صحیح نیست")

            # This error is for when the user does not enter the national code
            except Exception as e:
                print(e)
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText(
                    "لطفا کد ملی را وارد نمایید!")
                msgBox.setWindowTitle("خطا")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
