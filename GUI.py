"""
MAIN SCRIPT WITH GUI

TODO: when first button pressed replace 0 with number
TODO: when button pressed currently adds space between every number - should only be between operators
TODO: fix look of buttons
TODO: fix what happens when '=' button pressed
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

import Interpreter

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Calculator'
        self.left = 200
        self.top = 200
        self.width = 320
        self.height = 530
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel(self)
        pixmap = QPixmap("BackGround.bmp")
        pixmap = pixmap.scaled(330, 530)  # Scale the pixmap to fit the label size
        self.label.setPixmap(pixmap)
        self.label.setGeometry(0, 0, 330, 530)  # Set the label size

        # Create a QLineEdit widget
        self.textbox = QLineEdit(self)
        self.textbox.move(30, 120)
        self.textbox.resize(280, 40)
        self.textbox.setStyleSheet('background-color: rgba(100, 100, 100, 0); color: white; font-size: 20px')
        # Connect returnPressed signal of QLineEdit to custom slot function
        # TODO: (POTENTIALLY) enter keypress currently only works when selected textbox
        self.textbox.returnPressed.connect(self.update_non_editable_label)
        self.textbox.setAlignment(Qt.AlignRight)

        # Create a QLabel widget for non-editable text
        self.label_e = QLabel(self)
        self.label_e.move(30, 60)
        self.label_e.resize(280, 40)
        non_editable_text = "0"
        self.label_e.setText(non_editable_text)
        self.label_e.setStyleSheet('background-color: rgba(100, 100, 100, 0); color: white; font-size: 20px')
        self.label_e.setAlignment(Qt.AlignRight)
        # Ensure label doesn't get focus
        self.label.setFocusPolicy(Qt.NoFocus)

        # Set initial text
        initial_text = "0"
        self.textbox.setText(initial_text)

        # TODO: Add the memory buttons and functionality
        buttons = [
            {"text": "%", "geometry": (0, 210, 80, 51), "function": self.button_percent_clicked},
            {"text": "CE", "geometry": (80, 210, 80, 51), "function": self.button_ce_clicked},
            {"text": "C", "geometry": (160, 210, 80, 51), "function": self.button_c_clicked},
            {"text": "⌫", "geometry": (240, 210, 80, 51), "function": self.button_backspace_clicked},
            {"text": "1/x", "geometry": (0, 263, 80, 51), "function": self.button_inverse_clicked},
            {"text": "x²", "geometry": (80, 263, 80, 51), "function": self.button_square_clicked},
            {"text": "√x", "geometry": (160, 263, 80, 51), "function": self.button_square_root_clicked},
            {"text": "7", "geometry": (0, 317, 80, 51), "function": self.button_7_clicked},
            {"text": "8", "geometry": (80, 317, 80, 51), "function": self.button_8_clicked},
            {"text": "9", "geometry": (160, 317, 80, 51), "function": self.button_9_clicked},
            {"text": "×", "geometry": (240, 317, 80, 51), "function": self.button_multiply_clicked},
            {"text": "4", "geometry": (0, 370, 80, 51), "function": self.button_4_clicked},
            {"text": "5", "geometry": (80, 370, 80, 51), "function": self.button_5_clicked},
            {"text": "6", "geometry": (160, 370, 80, 51), "function": self.button_6_clicked},
            {"text": "-", "geometry": (240, 370, 80, 51), "function": self.button_subtract_clicked},
            {"text": "1", "geometry": (0, 425, 80, 51), "function": self.button_1_clicked},
            {"text": "2", "geometry": (80, 425, 80, 51), "function": self.button_2_clicked},
            {"text": "3", "geometry": (160, 425, 80, 51), "function": self.button_3_clicked},
            {"text": "+", "geometry": (240, 425, 80, 51), "function": self.button_add_clicked},
            {"text": "+/-", "geometry": (0, 477, 80, 51), "function": self.button_plus_minus_clicked},
            {"text": "0", "geometry": (80, 477, 80, 51), "function": self.button_0_clicked},
            {"text": ".", "geometry": (160, 477, 80, 51), "function": self.button_dot_clicked},
            {"text": "=", "geometry": (240, 477, 80, 51), "function": self.button_equal_clicked},
            {"text": "÷", "geometry": (240, 263, 80, 51), "function": self.button_divide_clicked}
        ]

        for button_data in buttons:
            button = QPushButton(button_data["text"], self)
            button.setGeometry(*button_data["geometry"])
            button.clicked.connect(button_data["function"])
            button.setStyleSheet('background-color: rgba(100, 100, 100, 50)')
            button.raise_()

        self.show()

    def button_percent_clicked(self):
        self.button_press('%')
        print("% clicked")

    def button_ce_clicked(self):
        print("CE clicked")
        self.textbox.setText('0')

    def button_c_clicked(self):
        print("C clicked")
        self.textbox.setText('0')
        self.label_e.setText('0')

    def button_backspace_clicked(self):
        print("⌫ clicked")
        # Delete Text
        tex = self.textbox.text()
        if tex[:-1] == ' ':
            # Space in text - delete next
            self.textbox.setText(tex[:-2])
        else:
            self.textbox.setText(tex[:-1])

    def button_inverse_clicked(self):
        print("1/x clicked")
        # Do inverse calculation
        tex = self.textbox.text()
        self.textbox.setText(f"1 / ({tex})")

    def button_square_clicked(self):
        print("x² clicked")
        tex = self.textbox.text()
        self.textbox.setText(f"{tex}^2")

    def button_square_root_clicked(self):
        print("√x clicked")
        tex = self.textbox.text()
        self.textbox.setText(f"{tex}^(1/2)")
        # TODO: make sqrt symbol recognised instead - this could take some work as operator for this in wrong order
        # Also might need implicit multiplication as well for this

    def button_7_clicked(self):
        print("7 clicked")
        self.button_press('7')

    def button_8_clicked(self):
        print("8 clicked")
        self.button_press('8')

    def button_9_clicked(self):
        print("9 clicked")
        self.button_press('9')

    def button_multiply_clicked(self):
        print("× clicked")
        self.button_press('*')

    def button_4_clicked(self):
        print("4 clicked")
        self.button_press('4')

    def button_5_clicked(self):
        print("5 clicked")
        self.button_press('5')

    def button_6_clicked(self):
        print("6 clicked")
        self.button_press('6')

    def button_subtract_clicked(self):
        print("- clicked")
        self.button_press('-')

    def button_1_clicked(self):
        print("1 clicked")
        self.button_press('1')

    def button_2_clicked(self):
        print("2 clicked")
        self.button_press('2')

    def button_3_clicked(self):
        print("3 clicked")
        self.button_press('3')

    def button_add_clicked(self):
        print("+ clicked")
        self.button_press('+')

    def button_plus_minus_clicked(self):
        # TODO: Not sure this will work - fix
        print("+/- clicked")
        tex = self.textbox.text()
        if tex[0] == '-':
            tex = tex[1:]
        else:
            tex = f"-{tex}"

    def button_0_clicked(self):
        print("0 clicked")
        self.button_press('0')


    def button_dot_clicked(self):
        print(". clicked")
        self.button_press('.')

    def button_equal_clicked(self):
        print("= clicked")
        self.update_non_editable_label()

    def button_divide_clicked(self):
        print("÷ clicked")
        self.button_press('/')

    def button_press(self, letter):
        self.textbox.setText(f"{self.textbox.text()} {letter}")

    def update_non_editable_label(self):
        # Update non-editable label text to match editable text
        res = CALCLLLLLLLLLL.maina(self.textbox.text())
        self.label_e.setText(f"{self.textbox.text()} = ")
        self.textbox.setText(str(res))


stylesheet = """
    MainWindow {
        background-image: "BackGround.bmp"; 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    ex = App()
    sys.exit(app.exec_())
