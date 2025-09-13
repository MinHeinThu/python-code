import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QToolBar, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl



class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Min's Private Browser")
        self.setGeometry(200, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))


        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # Toolbar
        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        back_btn = QPushButton("<")
        back_btn.clicked.connect(self.browser.back)
        nav_bar.addWidget(back_btn)

        forward_btn = QPushButton(">")
        forward_btn.clicked.connect(self.browser.forward)
        nav_bar.addWidget(forward_btn)

        reload_btn = QPushButton("Reload")
        reload_btn.clicked.connect(self.browser.reload)
        nav_bar.addWidget(reload_btn)

        nav_bar.addWidget(self.url_bar)

        # Layout
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.browser.urlChanged.connect(self.update_url_bar)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(url)

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
