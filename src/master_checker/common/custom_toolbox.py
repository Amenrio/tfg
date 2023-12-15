from PySide2.QtWidgets import (
    QTableWidgetItem,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QTableWidget,
    QMenu,
    QAction,
    QSizePolicy,
    QAbstractScrollArea,
    QAbstractItemView,
)
from PySide2.QtGui import QBrush, QColor, QGradient, QGuiApplication, QPalette


HEADER_BUTTON_STYLESHEET = """
        QPushButton {
        text-align: left;
        padding-left: 10px;
        font-size: 13px;
        font-weight: bold;
        background-color: rgb(50,50,50);
        border-radius: 3px;
        }
        QPushButton:hover {
        background-color: rgb(73,73,73)
        }
        QPushButton:pressed {
        background-color: rgb(25, 25, 25);
        }

        """


class CustomToolbox(QWidget):
    """_summary_

    Args:
        QWidget (_type_): _description_
    """
    def __init__(self, department, checker_class_object):
        super().__init__()
        # Name of the toolbox represented by the department to check
        self.department_name = department
        # Instance of the same department checker class
        self.checker_class = checker_class_object

        self.column_labels = ["Name", "Status"]
        self.create_layout()

    def create_layout(self):
        """_summary_
        """
        self.header_button = QPushButton(f"▼   {self.department_name.capitalize()}")
        self.header_button.setSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.Fixed
        )
        self.header_button.setMinimumSize(0, 25)

        self.vertical_layout = QVBoxLayout()
        self.header_button.setStyleSheet(HEADER_BUTTON_STYLESHEET)

        self.vertical_layout.addWidget(self.header_button)
        self.setLayout(self.vertical_layout)
