''' Вікно для карти питань '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo_app import app 

# Віджети, які будуть розміщені ?
btn_Menu = QPushButton('Меню') # Кнопка повернення в головне меню
btn_Sleep = QPushButton('Отдохнуть') # Кнопка прибирає вікно таймера
box_Minutes = QSpinBox() # к-ть хвилин
box_Minutes.setValue(30)
btn_OK = QPushButton('Ответить') # кнопка відповіді
lb_Question = QLabel('') # текст питання

# ----------------------------------------------------------
# Створюєм панель з варіантами відповідей
# ----------------------------------------------------------

# Створюєм віджети і об'єднуєм їх в групу
RadioGroupBox = QGroupBox("Варианты ответов") # група перемикачів з варіантами відповідей
RadioGroup = QButtonGroup() # а це для угруповання перемикачів, щоб керувати їхньою поведінкою

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Розміщуємо на панелі варіанти відповідей у ​​два стовпці всередині групи:
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальні будуть усередині горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # дві відповіді у перший стовпець
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # дві відповіді у другий стовпець
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # розмістили стовпці в одному рядку
RadioGroupBox.setLayout(layout_ans1) # готова "панель" з варіантами відповідей

# ----------------------------------------------------------
# Створюємо панель із результатом тесту:
# ----------------------------------------------------------

# Створюємо віджети та об'єднуємо їх у групи
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('') #тут розміщується напис "правильно" або "неправильно"
lb_Correct = QLabel('') # тут буде написано текст правильної відповіді

# Розміщуємо результат тесту:
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

# ----------------------------------------------------------
# Розміщуємо всі віджети у вікні:
# ----------------------------------------------------------

layout_line1 = QHBoxLayout() #кнопки для перемикання між режимами
layout_line2 = QHBoxLayout() # питання
layout_line3 = QHBoxLayout() # варіанти відповідей або результат тесту
layout_line4 = QHBoxLayout() # кнопка "Відповісти"

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1) # розрив між кнопками робимо по можливості довше
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилин'))

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2) # кнопка має бути великою
layout_line4.addStretch(1)

#Тепер створені 4 рядки розмістимо один під одним:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробіли між вмістом

#Результат роботи цього модуля: віджети розміщені всередині layout_card, який можна призначити вікну.

def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    # скинути вибрану радіо-кнопку
    RadioGroup.setExclusive(False) # зняли обмеження, щоб можна було скинути вибір радіокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # повернули обмеження, тепер лише одна радіокнопка може бути вибрана
