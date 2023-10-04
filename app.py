from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
from PyQt5.QtGui import QFont

win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_next = 'Начать'
txt_instruction = ('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'   
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.' )
txt_title = 'Здоровье'
txt_name = 'Введите Ф.И.О.:'
txt_hintname = "Ф.И.О."
txt_hintage = "0"
txt_test1 = 'Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.'
txt_test2 = 'Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.'
txt_test3 = 'Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.'
txt_sendresults = 'Отправить результаты'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Начать первый тест'
txt_starttest2 = 'Начать делать приседания'
txt_starttest3 = 'Начать финальный тест'
txt_timer = ''


txt_age = 'Полных лет:'
txt_finalwin = 'Результаты'
txt_index = 'Индекс Руфье: '
txt_workheart = 'Работоспособность сердца: '


txt_res1 = "низкая. Срочно обратитесь к врачу!"
txt_res2 = "удовлетворительная. Обратитесь к врачу!"
txt_res3 = "средняя. Возможно, стоит дополнительно обследоваться у врача."
txt_res4 = "выше среднего"
txt_res5 = "высокая"


app = QApplication([])

win1 = QWidget()
win1.resize(win_width, win_height) #Первое окно

win3 = QWidget()
win3.resize(win_width, win_height)





def win2show():
    win2.show()
def win3show():
    win3.show()
win3text1 = QLabel(txt_finalwin)
win3line = QVBoxLayout()
win3line.addWidget(win3text1, alignment= Qt.AlignHCenter)



win3.setLayout(win3line)



def timer1():
    global timer___1
    timer___1 = QTimer()
    global time
    time = QTime(0, 0, 15)
    timer___1.timeout.connect(timer1event)
    timer___1.start(1000)

def timer1event():
    global time
    time = time.addSecs(-1)
    timer.setText(time.toString('hh:mm:ss'))
    timer.setFont(QFont('Times', 36, QFont.Bold))
    if time.toString('hh:mm:ss') == '00:00:00':
        timer___1.stop()        

def timer2():
    global timer___1
    timer___1 = QTimer()
    global time2
    time2 = QTime(0, 0, 45)
    timer___1.timeout.connect(timer2event)
    timer___1.start(1000)

def timer2event():
    global time2
    time2 = time2.addSecs(-1)
    timer.setText(time2.toString('hh:mm:ss')[6:8])
    timer.setFont(QFont('Times', 36, QFont.Bold))
    if time2.toString('hh:mm:ss') == '00:00:00':
        timer___1.stop()

def timer3():
    global timer___1
    timer___1 = QTimer()
    global time3
    time3 = QTime(0, 0, 59)
    timer___1.timeout.connect(timer3event)
    timer___1.start(1000)

def timer3event():
    global time3
    time3 = time3.addSecs(-1)
    timer.setText(time3.toString('hh:mm:ss'))
    timer.setFont(QFont('Times', 36, QFont.Bold))
    a1 = time3.toString('hh:mm:ss')
    
    if 45 < int(a1[6:8]) <= 59:
        timer.setStyleSheet('color: rgb(0,255,0)')
    if 15 < int(time3.toString('hh:mm:ss')[6:8]) <= 45:
        timer.setStyleSheet('color: rgb(0,0,0)')
    if 0 < int(time3.toString('hh:mm:ss')[6:8]) <= 15:
        timer.setStyleSheet('color: rgb(0,255,0)')
    if time3.toString('hh:mm:ss') == '00:00:00':
        timer___1.stop()



mainline = QVBoxLayout()
text1 = QLabel(txt_hello)
text2 = QLabel(txt_instruction)
startbttn = QPushButton(txt_next)

mainline = QVBoxLayout()
mainline.addWidget(text1, alignment= Qt.AlignHCenter)
mainline.addWidget(text2, alignment= Qt.AlignHCenter)
mainline.addWidget(startbttn, alignment= Qt.AlignHCenter)

startbttn.clicked.connect(win2show)

win1.setLayout(mainline)
win1.show()


win2 = QWidget() #Второе окно
win2.resize(win_width, win_height)
text12 = QLabel(txt_name)
fio = QLineEdit(txt_hintname)
text22 = QLabel(txt_age)
age1 = QLineEdit(txt_hinttest1)
text32 = QLabel(txt_test1)
test1startbttn = QPushButton(txt_starttest1) #начинает тест 1
test1startbttn.clicked.connect(timer1)
test1result = QLineEdit(txt_hinttest2)
text42 = QLabel(txt_test2)
test2startbttn = QPushButton(txt_starttest2)
test2startbttn.clicked.connect(timer2)
text52 = QLabel(txt_test3)
test3startbttn = QPushButton(txt_starttest3)
test3startbttn.clicked.connect(timer3)
test3result1 = QLineEdit(txt_hinttest2)
test3result2 = QLineEdit(txt_hinttest3)


mainline2 = QVBoxLayout()
mainline22 = QVBoxLayout() #для таймера
mainlineh = QHBoxLayout()


timer = QLabel(txt_timer, alignment= Qt.AlignCenter)
checkresults = QPushButton('Отправить результаты')
checkresults.clicked.connect(win3show)
mainline22.addWidget(timer,alignment= Qt.AlignCenter)
mainline2.addWidget(text12, alignment= Qt.AlignLeft)
mainline2.addWidget(fio, alignment= Qt.AlignLeft)
mainline2.addWidget(text22, alignment= Qt.AlignLeft)
mainline2.addWidget(age1, alignment= Qt.AlignLeft)
mainline2.addWidget(text32, alignment= Qt.AlignLeft)
mainline2.addWidget(test1startbttn, alignment= Qt.AlignLeft)
mainline2.addWidget(test1result, alignment= Qt.AlignLeft)
mainline2.addWidget(text42, alignment= Qt.AlignLeft)
mainline2.addWidget(test2startbttn, alignment= Qt.AlignLeft)
mainline2.addWidget(text52, alignment= Qt.AlignLeft)
mainline2.addWidget(test3startbttn, alignment= Qt.AlignLeft)
mainline2.addWidget(test3result1, alignment= Qt.AlignLeft)
mainline2.addWidget(test3result2, alignment= Qt.AlignLeft)
mainline2.addWidget(checkresults, alignment= Qt.AlignCenter)
mainlineh.addLayout(mainline2)
mainlineh.addLayout(mainline22)

win2.setLayout(mainlineh)

age = int(age1.text()) 
res1 = int(test1result.text())
res2 = int(test3result1.text())
res3 = int(test3result2.text())

def results123(age, res1, res2, res3):
       global index
       index = (4*(res1 + res2 + res3) - 200)/10
       if age < 7:
           index = 0
           return "нет данных для такого возраста"
       
       if age == 7 or age == 8:
           if index >= 21:
               return txt_res1
           elif index < 21 and index >= 17:
               return txt_res2
           elif index < 17 and index >= 12:
               return txt_res3
           elif index < 12 and index >= 6.5:
               return txt_res4
           else:
               return txt_res5
       if age == 9 or age == 10:
           if index >= 19.5:
               return txt_res1
           elif index < 19.5 and index >= 15.5:
               return txt_res2
           elif index < 15.5 and index >= 10.5:
               return txt_res3
           elif index < 10.5 and index >= 5:
               return txt_res4
           else:
               return txt_res5
       if age == 11 or age == 12:
           if index >= 18:
               return txt_res1
           elif index < 18 and index >= 14:
               return txt_res2
           elif index < 14 and index >= 9:
               return txt_res3
           elif index < 9 and index >= 3.5:
               return txt_res4
           else:
               return txt_res5
       if age == 13 or age == 14:
           if index >= 16.5:
               return txt_res1
           elif index < 16.5 and index >= 12.5:
               return txt_res2
           elif index < 12.5 and index >= 7.5:
               return txt_res3
           elif index < 7.5 and index >= 2:
               return txt_res4
           else:
               return txt_res5
       if age >= 15:
           if index >= 15:
               return txt_res1
           elif index < 15 and index >= 11:
               return txt_res2
           elif index < 11 and index >= 6:
               return txt_res3
           elif index < 6 and index >= 0.5:
               return txt_res4
           else:
               return txt_res5

win3text2 = QLabel(str(txt_index))
win3text3 = QLabel(str(txt_workheart))
final_results = results123(age, res1, res2, res3)
workheart = QLabel(str(final_results))
index_text = QLabel(str(index))
win3line.addWidget(win3text2, alignment= Qt.AlignHCenter)
win3line.addWidget(index_text, alignment= Qt.AlignHCenter)
win3line.addWidget(win3text3, alignment= Qt.AlignHCenter)
win3line.addWidget(workheart, alignment= Qt.AlignHCenter)


 






app.exec_()