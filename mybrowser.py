from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My Own Browser")
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.Url_bar = QLineEdit()
        self.Url_bar.returnPressed.connect(self.navigate_to_Url)
        navbar.addWidget(self.Url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_Url(self):
        url = self.Url_bar.text()
        self.browser.setUrl(QUrl(url))

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def update_url(self, q):
        self.Url_bar.setText(q.toString())


app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec()
