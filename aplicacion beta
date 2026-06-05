from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

ANCHO, ALTO = 700, 500
COR_X, COR_Y = 200, 200
TITULO = 'Project PyQt5'
INPUT_TEXT = 'Ingrese Algo...'
BTN_TEXT = 'Enviar'

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.set_window()
        self.config_window()
        self.event_handler()
        self.show()

    def set_window(self): 
        # FUNCION QUE ESTABLECE EL DISEÑO DE LA APP
        # widgets
        self.input = QLineEdit(INPUT_TEXT)
        self.btn = QPushButton(BTN_TEXT)
        self.label = QLabel()

        layout = QHBoxLayout()
        layout.addWidget(self.input, alignment=Qt.AlignLeft)
        layout.addWidget(self.btn, alignment=Qt.AlignLeft)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def config_window(self):
        # CONFIGURA PARAMETRO INICIALES DE LA VENTANA
        self.setGeometry(COR_X, COR_Y, ANCHO, ALTO)
        self.setWindowTitle(TITULO)

    def event_handler(self):
        # FUNCION QUE SE ENCARGA DE MANEJAR LA LOGICA
        self.btn.clicked.connect(self.show_text)

    # AQUI SE DEFINEN TODAS LAS FUNCIONALIDADES DE LA APP
    def show_text(self):
        text = self.input.text()
        self.label.setText(text)

def run():
    # CREA Y EJECUTA LA APP
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()

if __name__ == "__main__":
    run()
