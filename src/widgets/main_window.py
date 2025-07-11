from PySide6.QtWidgets import (
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from widgets.input import Input
from widgets.settings import Settings
from widgets.voice_selector import VoiceSelector


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("VocalScript")
        self.setCentralWidget(QWidget(self))
        self.setStatusBar(QStatusBar())

        voice_selector = VoiceSelector(self.centralWidget())
        _ = voice_selector.status.connect(lambda msg: self.statusBar().showMessage(msg))

        settings = Settings(self)
        _ = settings.accepted.connect(lambda: voice_selector.load_voices())
        _ = (
            self.menuBar()
            .addAction("&Settings")
            .triggered.connect(lambda: settings.open())
        )

        input = Input(self.centralWidget())
        _ = input.status.connect(lambda msg: self.statusBar().showMessage(msg))

        main_layout: QVBoxLayout = QVBoxLayout(self.centralWidget())
        main_layout.addWidget(voice_selector)
        main_layout.addWidget(input)
        self.centralWidget().setLayout(main_layout)
