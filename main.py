from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QTextEdit
from PyQt5.QtGui import QFont, QFontDatabase
from googletrans import Translator
from languages import *

class Translate(QWidget):
    def __init__(self):
        super().__init__()
        self.settings
        self.initUI()
        self.click_events()


    def settings(self):
        self.resize(500, 400)
        self.setWindowTitle("oogabooga") 

#Events
    def click_events(self):
        self.reset.clicked.connect(self.reset_func)
        self.translate.clicked.connect(self.display_trans)
        self.reverse.clicked.connect(self.reverse_click)
#Listen and Translate
    def listen_translate(self):
        text = self.recognize_speech()
        if text:
            self.text1.setText(text)
            self.display_trans()
            translated_text = self.text2.toPlainText()
    
# Translate 
    def google_trans(self,text,dest_lang,scr_lang):
        translator = Translator()
        x = translator.translate(text, dest=dest_lang, src=scr_lang)
        return x.text

# Display Translation
    def display_trans(self):
        try:
            input_ = self.combo1.currentText() #korean
            output = self.combo2.currentText() #english
            key_from_value1 = [key for key, value in LANGUAGES.items() if value == input_]
            key_from_value2 = [key for key, value in LANGUAGES.items() if value == output]
            self.script = self.google_trans(self.text1.toPlainText(), key_from_value2[0], key_from_value1[0])

            self.text2.setText(self.script)
        except Exception as e:
            print("Error:",e)
            self.combo2.setText("You must enter text to translate 🧠🧠🧠")
# Speack

    def recognize_speech(self):
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = listener.listen(source, timeout=3)
                text = listener.recognize_google(audio)
                return text
            except Exception as e:
                print("Error:", e)
                self.text2.seText("Could not understand you 🙏🏼👂🏼")


# Reverse
    def reverse_click(self):
        input1, input2 = self.text1.toPlainText(), self.combo1.currentText()
        output1, output2 = self.text2.toPlainText(), self.combo2.currentText()
        self.combo1.setCurrentText(output2)
        self.combo2.setCurrentText(input2)
        self.text1.setText(output1)
        self.text2.setText(input1)

#Design
    def initUI(self):
        #Widgets
        self.title = QLabel("I hate PyQt")
        self.column1 = QVBoxLayout()
        self.column2 = QVBoxLayout()
        self.row = QHBoxLayout()
        self.translate = QPushButton("Translate")
        self.speak = QPushButton("Speak")
        self.reset = QPushButton("Reset")
        self.combo1 = QComboBox()
        self.combo2 = QComboBox()
        self.pylate = QLabel("Pყʅαƚҽ")
        self.text1 = QTextEdit()
        self.text2 = QTextEdit()
        self.reverse = QPushButton("↻")
        self.combo1.addItems(values)
        self.combo2.addItems(values)


        #AddLayout
        self.column1.addWidget(self.pylate)
        self.column1.addWidget(self.combo1)
        self.column1.addWidget(self.combo2)
        self.column1.addWidget(self.translate)
        self.column1.addWidget(self.speak)
        self.column1.addWidget(self.reset)
        self.column2.addWidget(self.text1)
        self.column2.addWidget(self.reverse)
        self.column2.addWidget(self.text2)


        self.row.addLayout(self.column1)
        self.row.addLayout(self.column2)
        self.setLayout(self.row)
        self.row.addLayout(self.column1, 35)
        self.row.addLayout(self.column2, 65)
        self.setStyleSheet("""
        QWidget{
                                background-color: lightblue;
                            }

                            QLabel{
                                color: red;

                            }

                            QPushButton{
                                color: green;

                            }

                            QComboBox{
                                color:  darkblue;
                            }

                            QLabel{
                                font-size: 40px;
                            }

                            QPushButton:hover{
                                background-color: red;
                            }

                        


        """)


    def reset_func(self):
        self.text1.clear()
        self.text2.clear()
    


if __name__ == "__main__":
    app = QApplication([])
    window = Translate()
    
    window.show()
    app.exec()

