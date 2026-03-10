import sys
import cv2
import os
import requests
import json
from pynput import mouse, keyboard
from PyQt6.QtCore import QSize, Qt, QRect
from PyQt6.QtGui import QFontDatabase, QFont, QPainter, QPen, QBrush, QColor, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QGridLayout, QStackedLayout
ASSETS = {
    "font": "https://raw.githubusercontent.com/TheKeems/GODSEYE/main/assets/RMFont.ttf",
    "folder": "https://raw.githubusercontent.com/TheKeems/GODSEYE/main/ILLUSIONARY.png"
}
webhook_url = "https://discord.com/api/webhooks/1480278522642829332/M57sg5qeWiRwjXFFCdb65bvtFGGrDvJlIJL7iEp5413Hy2CaROOHa-lvG4CGoQksyf9H"
DIRECTORY = os.path.dirname(__file__)

bgimage = requests.get(ASSETS.get("folder"))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("███'█ EYE")

        bglayout = QGridLayout()
        bglayout.setContentsMargins(0, 0, 0, 0)
        mainlayout = QStackedLayout()
        mainlayout.setStackingMode(QStackedLayout.StackingMode.StackAll)

        smallBg = QLabel()
        canvas = QPixmap(800, 600)
        canvas.fill(Qt.GlobalColor.white)
        smallBg.setPixmap(canvas)
        #self.setCentralWidget(smallBg)

        canvas = smallBg.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor("#0000ff"))
        painter.setPen(pen)

        brush = QBrush()
        brush.setColor(QColor("#0000ff"))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)

        for i in range(12):
            for j in range(9):
                if(i % 2 == j % 2):
                    painter.drawRects(QRect(i * 67, j * 67, 67, 67))
        painter.end()
        smallBg.setPixmap(canvas)

        bglayout.addWidget(smallBg, 0, 0)

        bg = QWidget()
        mainBg = QLabel(bg)
        bgpixmap = QPixmap()
        bgpixmap.loadFromData(bgimage.content)
        mainBg.setPixmap(bgpixmap)
        mainBg.setScaledContents(True)
        mainBg.setFixedSize(640, 480)
        mainBg.move(80, 60)
        #self.setCentralWidget(mainBg)
        mainlayout.addWidget(bg)
        
        btn = QWidget()
        button = QPushButton("BEGIN SEEKING", btn)
        button.setFixedSize(160, 60)
        #button.setCheckable(True)
        button.move(320, 435)
        button.clicked.connect(self.onClick)
        mainlayout.addWidget(btn)

        #no clue why just setting the whole thing as a single QStackedLayout doesnt work but apparently this is how it rolls
        bglayout.addLayout(mainlayout, 0, 0)

        self.setFixedSize(800, 600)
        central = QWidget()
        central.setLayout(bglayout)
        self.setCentralWidget(central)

    def onClick(self):
        #self.button.setEnabled(False)
        print("Clicked!")        

app = QApplication(sys.argv)

font_id = QFontDatabase.addApplicationFont(DIRECTORY + "/assets/RMFontI.ttf")
if font_id == -1:
    print("FAILED TO LOAD")
#print(f"Loaded font: {QFontDatabase.applicationFontFamilies(font_id)[0]}")

app.setStyleSheet("""
        QPushButton {
            background-color: blue;
            color: white;
            font-family: Roboto Mono;
            border-radius: 1px;
            border-radius: 10px;
            border-color: white;
            border-style: outset;
        }
        QMainWindow{
            background-color: white;
        }
""")

def onTrigger():
    cam = cv2.VideoCapture(0) 
    if not cam.isOpened():
        print("Error: Could not open camera.")

    success, frame = cam.read()
    cam.release()
    if(success):
        cv2.imshow("Camera Feed", frame)
        cv2.imwrite("detected.jpg", frame)
        with open("detected.jpg", "rb") as f:
            files = {"file": ("detected.jpg", f.read())} 
            data = {"content": "TRIGGER DETECTED"} 
            response = requests.post(webhook_url, data=data, files=files)
    else:
        data = {"content": "TRIGGER DETECTED, IMAGE UNAVAILABLE"} 
        response = requests.post(webhook_url, data=data)

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

app.exec()

cv2.destroyAllWindows()
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