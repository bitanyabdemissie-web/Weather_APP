import sys  # gives access to system functions (used for app arguments + clean exit)

from PyQt5.QtWidgets import QApplication, QMainWindow  # QApplication = app engine, QMainWindow = main window structure
from PyQt5.QtGui import QIcon  # used to set window icon


class MainWindow(QMainWindow):  # create your own window class based on QMainWindow
    def __init__(self):
        super().__init__()  # initialize the parent (VERY important)

        self.setWindowTitle("My first GUI")  # sets the title bar text

        self.setGeometry(0, 0, 500, 500)  # (x, y, width, height) → position + size

        self.setWindowIcon(QIcon("Gemini_Generated_Image_ap2ubcap2ubcap2u.png"))  
        # sets the window icon (image must exist in folder or give full path)


def main():
    app = QApplication(sys.argv)  
    # create application (handles events like clicks, typing, etc.)

    window = MainWindow()  
    # create an instance of your window

    window.show()  
    # display the window on screen

    sys.exit(app.exec_())  
    # start event loop (keeps app running) + clean exit when closed


if __name__ == "__main__":  
    # ensures this runs only when file is executed directly
    main()  
    # start the application