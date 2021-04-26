from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QMessageBox, QPushButton
from PyQt5.QtWidgets import QTextBrowser, QTextEdit, QInputDialog
from PyQt5.QtGui import QColor, QFont
import requests
import datetime
from PyQt5.QtCore import QTimer, QUrl
from random import choices
import os.path
import os
from F_Registration import Ui_Registration
from F_Enter import Ui_Enter
from F_Messenger import Ui_Messenger
from F_Start import Ui_Start


# https://final-server-flask.herokuapp.com/ - это ссылка, на которую я загрузил свой flask-сервер.
URL = 'http://127.0.0.1:8080/'


class Main(QWidget, Ui_Messenger):
    def __init__(self):
        super().__init__()
        self.number_chats = 1
        self.all_chats = {}
        self.setupUi(self)
        self.setFixedSize(501, 460)
        self.sendButton.clicked.connect(self.send_message)
        self.tabWidget.removeTab(1)
        with open('unique_name.txt', mode='r') as f:
            self.private_info1 = eval(f.read())
        self.private_info = requests.get(URL + 'checking',
                                         params={'password': self.private_info1['password'],
                                                 'mail': self.private_info1['mail']}).json()['']
        if type(self.private_info) == str:
            QMessageBox.warning(self, 'Внимание!', 'Либо вы залезли в файл unique_name.txt, либо\
зарегестрировались на уже зарегестрированную почту. Перезайдите или\
перезарегестрируйтесь!')
            os.remove('unique_name.txt')
            raise SystemExit      
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)
        self.after = 0        
        self.pushButton.clicked.connect(self.search)
        
    def create_chat(self, number, user):
        exec('self.tab{} = QWidget()'.format(number))
        exec('self.tabWidget.addTab(self.tab{}, user)'.format(number))
        exec('self.messages{} = QTextBrowser(self.tab{})'.format(number, number))
        exec('self.messages{}.resize(391, 241)'.format(number))
        exec('self.messages{}.move(30, 20)'.format(number))
        exec('self.messages{}.setStyleSheet("background-color: " + QColor(255, 255, 255).name())'
             .format(number))
        exec('self.sendButton{} = QPushButton("{}", self.tab{})'.format(number, number, number))
        exec('self.sendButton{}.resize(75, 61)'.format(number))
        exec('self.sendButton{}.move(350, 270)'.format(number))
        exec('self.sendButton{}.setStyleSheet("background-color: " + QColor(255, 255, 255).name())'
             .format(number))
        exec('self.sendButton{}.setFont(QFont("Arial", 20))'.format(number))
        exec('self.text_input{} = QTextEdit(self.tab{})'.format(number, number))
        exec('self.text_input{}.resize(311, 61)'.format(number))
        exec('self.text_input{}.move(30, 270)'.format(number))
        exec('self.text_input{}.setStyleSheet("background-color: " + QColor(255, 255, 255).name())'
             .format(number))
        exec('self.text_input{}.setPlaceholderText("Введите текст...")'.format(number))
        exec('self.sendButton{}.clicked.connect(self.hello)'.format(number))
        exec('self.after{} = 0'.format(number))
        
    def hello(self):
        number = int(self.sender().text())
        text = eval('self.text_input{}.toPlainText()'.format(number))
        id_chat = self.all_chats[number]
        if text != '':
            requests.post(URL + 'chat/' + id_chat,
                          json={'text': text, 'name': self.private_info['name']
                                + ' ' + self.private_info['surname']})
        else:
            QMessageBox.warning(self, 'Внимание!', 'Вы не ввели текст!')
        exec("self.text_input{}.setPlainText('')".format(number))
        
    def update_messages(self):
        a = requests.get(URL + 'get', params={'after': str(self.after)})
        db = a.json()['']
        if db != []:
            self.after = db[-1]['time']
            for i in db:
                dt = datetime.datetime.fromtimestamp(i['time'])
                dt = dt.strftime('%H:%M:%S')
                self.messages.append('')
                self.messages.append('{} {}'.format(i['name'], dt))
                self.messages.append('{}'.format(i['text']))
        self.last_private_info = list(self.private_info)[:]
        self.private_info = requests.get(URL + 'checking',
                                         params={'password': self.private_info1['password'],
                                                 'mail': self.private_info1['mail']}).json()['']
        if type(self.private_info) != str:
            for i in self.private_info['chats']:
                if i not in list(self.all_chats.values()):
                    self.number_chats += 1
                    names = list(requests.get(URL + 'users_in_chat',
                                              params={'id_chat': i}).json()[''])
                    own_name = self.private_info['name'] + ' ' + self.private_info['surname']
                    chats_name = names[names.index(own_name) - 1]
                    self.all_chats[self.number_chats] = i
                    self.create_chat(self.number_chats, chats_name)
            for i in range(2, self.number_chats + 1):
                a = requests.get(URL + 'get_info_in_chat/' + self.all_chats[i],
                                 params={'after': str(eval('self.after{}'.format(i)))})
                db = a.json()['']
                if db != []:
                    exec("self.after{}".format(i) + " = float(db[-1]['time'])")
                    for j in db:
                        dt = datetime.datetime.fromtimestamp(j['time'])
                        dt = dt.strftime('%H:%M:%S')
                        exec("self.messages{}.append('')".format(i))
                        eval('self.messages{}'.format(i)).append('{} {}'.format(j['name'], dt))
                        eval("self.messages{}".format(i)).append('{}'.format(j['text']))
        else:
            self.private_info = self.last_private_info[:]
        
    def send_message(self):
        try:
            text = self.messageInput.toPlainText()
            if text != '':
                requests.post(URL + 'send',
                              json={'text': text, 'name': self.private_info['name']
                                    + ' ' + self.private_info['surname']})
            else:
                QMessageBox.warning(self, 'Внимание!', 'Вы не ввели имя и/или текст!')
        except:
            QMessageBox.warning(self, 'Внимание!', 'Сервер в данный момент не работает. Повторите \
 попытку позже. Просим прощения за неудобства.')
        self.messageInput.setPlainText('')
        
    def search(self):
        answer = QInputDialog.getText(self, '', 'Введите e-mail')
        if False in answer:
            pass
        else:
            e_mail = answer[0]
            a = requests.get(URL + 'checking_mail',
                             params={'own_mail': self.private_info['mail'], 'mail': e_mail})
            db = a.json()['']
            if db == 'error':
                QMessageBox.warning(self, 'Внимание!', 'Аккаунта с таким e-mail не существует.')
            else:
                db = db.split(', ')
                id_of_chat = db[0]
                name_of_user = db[1]
                self.number_chats += 1
                self.all_chats[self.number_chats] = id_of_chat
                self.create_chat(self.number_chats, name_of_user)

        
class Start(QWidget, Ui_Start):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(501, 460)
        self.login.clicked.connect(self.log)
        self.registration.clicked.connect(self.reg)
        
    def log(self):
        self.hide()
        self.ex2 = Login()
        self.ex2.show()
        
    def reg(self):
        self.hide()
        self.ex2 = Registration()
        self.ex2.show()
        
        
class Login(QWidget, Ui_Enter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(501, 460)
        self.log_in.clicked.connect(self.chats)
        
    def chats(self):
        password = self.password_input.text()
        mail = self.mail_input.text()
        answer = requests.get(URL + 'checking',
                              params={'password': password, 'mail': mail}).json()['']
        if type(answer) == dict:
            with open('unique_name.txt', mode='w') as f:
                f.write(str(answer))
            self.transition()
        else:
            QMessageBox.warning(self, 'Внимание!', str(answer))
        
    def transition(self):
        self.ex5 = Main()
        self.hide()
        self.ex5.show()
        
        
class Registration(QWidget, Ui_Registration):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(501, 460)
        self.pushButton.clicked.connect(self.chats)
        
    def chats(self):
        mail = self.mail_input.text()
        a = requests.get(URL + 'checking_mail', params={'own_mail': mail,
                                                        'mail': mail})
        db = a.json()['']
        if db == 'error':
            password = self.password_input.text()
            repeating_password = self.repeating_password.text()
            if password == repeating_password:
                name = self.name_input.text().capitalize()
                surname = self.surname_input.text().capitalize()
                country = self.country_input.text().capitalize()
                city = self.city_input.text().capitalize()
                bbb = "'mail': '{}','password': '{}','name': '{}','surname': '{}','country':\
'{}','city': '{}'".format(mail, password, name, surname, country, city)
                with open('unique_name.txt', mode='w') as f:
                    f.write('{' + bbb + '}')
                requests.post(URL + 'reg', json=eval('{' + bbb + '}'))
                self.transition()
            else:
                QMessageBox.warning(self, 'Внимание!', 'Некорректный ввод пароля')
        else:
            QMessageBox.warning(self, 'Внимание!', 'Аккаунт с таким e-mail уже существует!')
        
    def transition(self):
        self.ex4 = Main()
        self.hide()
        self.ex4.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    if os.path.exists('unique_name.txt'):
        ex = Main()
        ex.show()
    else:
        ex0 = Start()
        ex0.show()
    sys.exit(app.exec())