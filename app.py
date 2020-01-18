import sys
import random
import time
from PySide2 import QtCore, QtWidgets, QtGui
from life import Grid

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button_start = QtWidgets.QPushButton("Initialize Grid")
        self.button_play = QtWidgets.QPushButton("Play")
        self.text = QtWidgets.QLabel("Click Play")

        font = QtGui.QFont("Monospace") 
        self.text.setFont(font)
        
        self.setWindowTitle("Conway's Game of Life")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button_start)
        self.layout.addWidget(self.button_play)
        self.setLayout(self.layout)

        self.button_start.clicked.connect(self.start)
        self.button_play.clicked.connect(self.simulate)


    def start(self):

        self.grid = Grid(40)
        self.text.setText(self.grid.grid_to_string())
        self.text.repaint()

    def simulate(self):
        print("sim")
        for gen in range(40):
            self.grid.simulate()
            self.text.setText(self.grid.grid_to_string())
            self.text.repaint()
            print(gen)
            # time.sleep(.05)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(300, 300)
    widget.start()
    widget.show()

    sys.exit(app.exec_())