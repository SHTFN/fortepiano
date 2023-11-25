import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtMultimedia


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.c_noteButton.clicked.connect(self.run)
        self.d_noteButton.clicked.connect(self.run)
        self.e_noteButton.clicked.connect(self.run)
        self.f_noteButton.clicked.connect(self.run)
        self.g_noteButton.clicked.connect(self.run)
        self.a_noteButton.clicked.connect(self.run)
        self.b_noteButton.clicked.connect(self.run)

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def run(self, ):
        sender = self.sender()
        if sender == self.c_noteButton:
            self.load_mp3('./notes/do.mp3')
            self.player.play()
        elif sender == self.d_noteButton:
            self.load_mp3('./notes/re.mp3')
            self.player.play()
        elif sender == self.e_noteButton:
            self.load_mp3('./notes/mi.mp3')
            self.player.play()
        elif sender == self.f_noteButton:
            self.load_mp3('./notes/fa.mp3')
            self.player.play()
        elif sender == self.g_noteButton:
            self.load_mp3('./notes/sol.mp3')
            self.player.play()
        elif sender == self.a_noteButton:
            self.load_mp3('./notes/la.mp3')
            self.player.play()
        elif sender == self.b_noteButton:
            self.load_mp3('./notes/si.mp3')
            self.player.play()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.load_mp3('./notes/do.mp3')
            self.player.play()
        elif event.key() == Qt.Key_2:
            self.load_mp3('./notes/re.mp3')
            self.player.play()
        elif event.key() == Qt.Key_3:
            self.load_mp3('./notes/mi.mp3')
            self.player.play()
        elif event.key() == Qt.Key_4:
            self.load_mp3('./notes/fa.mp3')
            self.player.play()
        elif event.key() == Qt.Key_5:
            self.load_mp3('./notes/sol.mp3')
            self.player.play()
        elif event.key() == Qt.Key_6:
            self.load_mp3('./notes/la.mp3')
            self.player.play()
        elif event.key() == Qt.Key_7:
            self.load_mp3('./notes/si.mp3')
            self.player.play()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
