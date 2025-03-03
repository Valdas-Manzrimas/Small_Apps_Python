import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QImage, QPixmap

try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Install it by typing 'pip install pillow' in the command prompt.")
    sys.exit(1)

class ScreenshotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.browser = None  # Initialize browser reference

    def initUI(self):
        self.setWindowTitle('Web Screenshot')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.url_label = QLabel('Enter website URL:')
        self.url_entry = QLineEdit('https://www.google.com')
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_entry)

        self.width_label = QLabel('Enter width:')
        self.width_entry = QLineEdit('1024')
        layout.addWidget(self.width_label)
        layout.addWidget(self.width_entry)

        self.height_label = QLabel('Enter height:')
        self.height_entry = QLineEdit('2048')
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_entry)

        self.screenshot_button = QPushButton('Take Screenshot')
        self.screenshot_button.clicked.connect(self.take_screenshot)
        layout.addWidget(self.screenshot_button)

        self.setLayout(layout)

    def take_screenshot(self):
        url = self.url_entry.text()
        width = int(self.width_entry.text())
        height = int(self.height_entry.text())

        # Create hidden browser widget
        self.browser = QWebEngineView(self)
        self.browser.hide()  # Keep browser hidden
        self.browser.resize(width, height)
        self.browser.load(QUrl(url))

        self.browser.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, ok):
        if ok:
            print("Page loaded successfully")
            # Ensure browser is rendered before capture
            QTimer.singleShot(3000, self.force_repaint)
        else:
            print("Failed to load URL")

    def force_repaint(self):
        """Force browser repaint before capturing"""
        self.browser.page().runJavaScript("""
            requestAnimationFrame(() => {
                document.body.style.visibility = 'visible';
            });
        """)
        QTimer.singleShot(1000, self.save_screenshot)

    def save_screenshot(self):
        # Capture only the browser content
        pixmap = QPixmap(self.browser.size())
        self.browser.render(pixmap)
        pixmap.save("screenshot.png", "PNG")
        print("Screenshot saved successfully")
        self.open_with_default_app("screenshot.png")
        self.browser.deleteLater()

    def open_with_default_app(self, path):
        try:
            if sys.platform.startswith("darwin"):
                subprocess.run(["open", path], check=True)
            elif os.name == "nt":
                os.startfile(path)
            elif os.name == "posix":
                subprocess.run(["xdg-open", path], check=True)
        except Exception as e:
            print(f"Error opening file: {e}")

if __name__ == '__main__':
    os.environ["QT_LOGGING_RULES"] = "qt.qpa.fonts=false"
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu"
    app = QApplication(sys.argv)
    ex = ScreenshotApp()
    ex.show()
    sys.exit(app.exec_())