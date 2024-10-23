import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class LumiMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the main window title and size
        self.setWindowTitle("Lumi - Drag and Drop UI Builder")
        self.setGeometry(100, 100, 800, 600)

if __name__ == "__main__":
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    
    # Create the main window
    main_window = LumiMainWindow()
    main_window.show()

    # Execute the application loop
    sys.exit(app.exec_())


