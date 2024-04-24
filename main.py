import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class Janela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exemplo PyQt')
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel('Olá, Mundo!', self)
        self.label.move(100, 50)

        self.botao = QPushButton('Clique Aqui', self)
        self.botao.move(100, 100)
        self.botao.clicked.connect(self.mostrar_mensagem)

    def mostrar_mensagem(self):
        self.label.setText('Botão Clicado')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())
