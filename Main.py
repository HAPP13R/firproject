# k, d, a = map(int, input("Your KDA >> ").split("/"))
# if (d == 0):
#     print("Perfect!")
# elif ((k + a) / d > 5.0):
#     print("Awesome!")
# elif ((k + a) / d > 4.0):
#     print("Nice!")
# elif ((k + a) / d > 3.0):
#     print("Good!")
# elif ((k + a) / d > 2.0):
#     print("Cool")
# elif ((k + a) / d > 1.0):
#     print("LOL")
# else:
#     print("Noob :(")

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())