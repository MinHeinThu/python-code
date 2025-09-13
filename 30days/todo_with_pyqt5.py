import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLineEdit, QMessageBox
)

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(200, 200, 400, 400)

        # Layouts
        self.layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()
        self.button_layout = QHBoxLayout()

        # Widgets
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        self.task_list = QListWidget()

        self.add_btn = QPushButton("Add Task")
        self.delete_btn = QPushButton("Delete Task")
        self.modify_btn = QPushButton("Modify Task")
        self.exit_btn = QPushButton("Exit")

        # Add widgets to layouts
        self.input_layout.addWidget(self.task_input)
        self.input_layout.addWidget(self.add_btn)

        self.button_layout.addWidget(self.delete_btn)
        self.button_layout.addWidget(self.modify_btn)
        self.button_layout.addWidget(self.exit_btn)

        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.task_list)
        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

        # Signals
        self.add_btn.clicked.connect(self.add_task)
        self.delete_btn.clicked.connect(self.delete_task)
        self.modify_btn.clicked.connect(self.modify_task)
        self.exit_btn.clicked.connect(self.close)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty.")

    def delete_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            self.task_list.takeItem(selected)
        else:
            QMessageBox.warning(self, "Warning", "No task selected.")

    def modify_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            new_task, ok = QMessageBox.getText(
                self, "Modify Task", "Enter new task:"
            )
            if ok and new_task.strip():
                self.task_list.item(selected).setText(new_task.strip())
        else:
            QMessageBox.warning(self, "Warning", "No task selected.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())
