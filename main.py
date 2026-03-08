from pynput import mouse, keyboard
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("███'█ EYE")

        button = QPushButton("BEGIN SEEKING")
        button.setFixedSize(QSize(175, 75))
        #button.setCheckable(True)
        button.clicked.connect(self.onClick)


        self.setFixedSize(QSize(800, 600))
        self.setCentralWidget(button)

    def onClick(self):
        #self.button.setEnabled(False)
        print("Clicked!")        

app = QApplication(sys.argv)
app.setStyleSheet("""
        QPushButton {
            background-color: blue;
            color: white;
            font-family: Roboto-Mono;
            border-radius: 1px;
            border-radius: 10px;
            border-color: beige;
            border-style: outset;
        }
        QMainWindow{
            background-color: white;
        }
""")
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

app.exec()
"""
def on_press(key):
    print(f'Key pressed: {key}')

def on_click(x, y, button, pressed):
    if pressed:
        print(f'Mouse clicked at ({x}, {y}) with {button}')

def on_move(x, y):
    # Uncomment to track movement; can be very noisy
    print(f'Mouse moved to ({x}, {y})')
    pass

keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

mouse_listener = mouse.Listener(on_click=on_click, on_move=on_move)
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()"""