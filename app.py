from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

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


app = QApplication([])

win1 = QWidget()
win1.resize(win_width, win_height) #Первое окно

def win2show():
    win2.show()



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
age = QLineEdit(txt_hinttest1)
text32 = QLabel(txt_hinttest1)
test1startbttn = QPushButton(txt_starttest1)
test1result = QLineEdit(txt_hinttest2)
text42 = QLabel(txt_test2)
test2startbttn = QPushButton(txt_starttest2)
text52 = QLabel(txt_test3)
test3startbttn = QPushButton(txt_starttest3)
test3result1 = QLineEdit(txt_hinttest2)
test3result2 = QLineEdit(txt_hinttest3)
mainline2 = QVBoxLayout()
mainline22 = QVBoxLayout() #для таймера
mainlineh = QHBoxLayout()
timer = QLabel(txt_timer, alignment= Qt.AlignCenter)
mainline22.addWidget(timer,)
mainline2.addWidget(text12, alignment= Qt.AlignCenter)
mainline2.addWidget(fio, alignment= Qt.AlignCenter)
mainline2.addWidget(text22, alignment= Qt.AlignCenter)
mainline2.addWidget(age, alignment= Qt.AlignCenter)
mainline2.addWidget(text32, alignment= Qt.AlignCenter)
mainline2.addWidget(test1startbttn, alignment= Qt.AlignCenter)
mainline2.addWidget(test1result, alignment= Qt.AlignCenter)
mainline2.addWidget(text42, alignment= Qt.AlignCenter)
mainline2.addWidget(test2startbttn, alignment= Qt.AlignCenter)
mainline2.addWidget(text52, alignment= Qt.AlignCenter)
mainline2.addWidget(test3startbttn, alignment= Qt.AlignCenter)
mainline2.addWidget(test3result1, alignment= Qt.AlignCenter)
mainline2.addWidget(test3result2, alignment= Qt.AlignCenter)
mainlineh.addLayout(mainline2)
mainlineh.addLayout(mainline22)

win2.setLayout(mainlineh)










    


app.exec_()