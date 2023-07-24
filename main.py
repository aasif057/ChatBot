from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import ChatBot
import threading

  
class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = ChatBot()
        self.setMinimumSize(700, 500)
        
        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10,10,680,430)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,450,500,40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(590,450,100,40)
        self.button.setStyleSheet('QPushButton {background-color: #A3C1DA}')
        self.button.clicked.connect(self.send_message)
        
        # Add a new button
        self.button1 = QPushButton("Mic",self)
        self.button1.setGeometry(520,450,60,40) 
        self.button1.setStyleSheet('QPushButton {background-color: #A3C1DA}')
        self.button1.clicked.connect(self.foo)


        self.show()
    def foo(self):
        input = self.chatbot.take_commands()
        self.chat_area.append(f"<p style='color:#333333'>Me: {input}</p>")
        thread = threading.Thread(target=self.get_bot_response,args=(input, ))        
        thread.start()
    
    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response,args=(user_input, ))        
        thread.start()

    def get_bot_response(self,user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot:  {response}</p>")
        self.chatbot.speak(response)
        self.chatbot.close_speak()
app = QApplication(sys.argv)
main_window = ChatBotWindow()
main_window.setStyleSheet("QMainWindow {background: 'grey';}")
sys.exit(app.exec())
