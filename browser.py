import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Definir a janela principal
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        
        # Definir layout
        self.setCentralWidget(self.browser)
        
        # Criar a barra de navegação
        self.navbar = QToolBar()
        self.addToolBar(self.navbar)
        
        # Botões da barra de navegação
        self.back_button = QAction("Voltar", self)
        self.back_button.triggered.connect(self.browser.back)
        self.navbar.addAction(self.back_button)
        
        self.forward_button = QAction("Avançar", self)
        self.forward_button.triggered.connect(self.browser.forward)
        self.navbar.addAction(self.forward_button)
        
        self.reload_button = QAction("Recarregar", self)
        self.reload_button.triggered.connect(self.browser.reload)
        self.navbar.addAction(self.reload_button)
        
        # Barra de endereço
        self.address_bar = QLineEdit(self)
        self.address_bar.returnPressed.connect(self.navigate_to_url)
        self.navbar.addWidget(self.address_bar)
        
        # Atualizar a barra de endereço quando a URL mudar
        self.browser.urlChanged.connect(self.update_address_bar)
        
        # Configurar a janela principal
        self.setWindowTitle("Navegador Python")
        self.setGeometry(100, 100, 1024, 768)
        self.show()
    
    def navigate_to_url(self):
        url = self.address_bar.text()
        self.browser.setUrl(QUrl(url))
    
    def update_address_bar(self, qurl):
        self.address_bar.setText(qurl.toString())

# Configuração e execução do aplicativo
app = QApplication(sys.argv)
QApplication.setApplicationName("Navegador Python")
window = Browser()
sys.exit(app.exec_())
