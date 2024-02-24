import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QScrollArea, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QPalette, QColor, QFont


class LineResult:
    def __init__(self, removeline, last_remove_line, real_last_remove_line):
        self.removeline = removeline
        self.last_remove_line = last_remove_line
        self.real_last_remove_line = real_last_remove_line


show_font = {
    "á": "茨",
    "é": "姻",
    "í": "胤",
    "ó": "吋",
    "ú": "雨",
    "ñ": "隠",
    "¿": "夷",
    "¡": "斡",
    "Á": "威",
    "É": "畏",
    "Í": "緯",
    "Ó": "遺",
    "Ú": "郁",
    "Ñ": "謂"
}


def process_line(line):
    for key, value in show_font.items():
        line = line.replace(value, key)

    if not line.strip():
        return LineResult("", "", "")
    elif line.startswith("[sel") or line.startswith("[msg"):
        return LineResult("", line, "")

    result_line = ""
    inside_brackets = False
    skip_next_brackets = False

    for i, character in enumerate(line):
        if character == '[':
            inside_brackets = True
            end_index = line.find(']', i + 1)
            if end_index != -1:
                next_word = line[i + 1:end_index].strip()
                if next_word in ["var", "f 4 1", "f 4 2", "clr", "Navi"]:
                    skip_next_brackets = True
        elif character == ']':
            inside_brackets = False
            skip_next_brackets = False
        elif not inside_brackets and not skip_next_brackets:
            if i + 1 < len(line) and line[i] == '　' and line[i + 1] == '　':
                i += 1
            else:
                result_line += line[i:]
                break

    last_remove_line = result_line
    real_last_remove_line = ""

    last_n_bracket_index = last_remove_line.rfind("[n]")
    if last_n_bracket_index == -1:
        last_n_bracket_index = last_remove_line.rfind("[e]")
        if last_n_bracket_index != -1:
            last_remove_line = last_remove_line[:last_n_bracket_index + 3]
    else:
        last_remove_line = last_remove_line[:last_n_bracket_index + 3]

    if last_remove_line.endswith("[n]") or last_remove_line.endswith("[e]"):
        last_remove_line = last_remove_line[:-3]

    last_remove_line = last_remove_line.replace("[w]", "").replace("[e]", "")
    real_last_remove_line = result_line.replace(last_remove_line, "")

    removeline = line.replace(result_line, "")

    if "[n]" in last_remove_line and "[n][" not in last_remove_line:
        last_remove_line = last_remove_line.replace("[n]", " ")

    last_remove_line = last_remove_line.replace(
        "[sel]", "").replace("[msg]", "").strip()
    real_last_remove_line = real_last_remove_line.strip()

    return LineResult(removeline, last_remove_line, real_last_remove_line)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.line_results = []  # Create line_results attribute
        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        open_button = QPushButton("Open File")
        # Conecta el botón al método open_file_dialog
        open_button.clicked.connect(self.open_file_dialog)
        button_layout.addWidget(open_button)
        button_layout.addStretch(1)  # Add stretch to push button to the left
        main_layout.addLayout(button_layout)

        # Agrega un QLabel para mostrar la ruta del archivo seleccionado
        self.file_path_label = QLabel("No file selected")
        button_layout.addWidget(self.file_path_label)

        button_layout.addStretch(1)
        main_layout.addLayout(button_layout)

        save_button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_file)
        save_button_layout.addWidget(save_button)
        # Add stretch to push button to the left
        save_button_layout.addStretch(1)
        main_layout.addLayout(save_button_layout)

        self.scroll_area = QScrollArea()  # Mantener una referencia al QScrollArea
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_widget.setLayout(scroll_layout)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(scroll_widget)

        # Add scroll_area to main_layout
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

        self.setStyleSheet("background-color: #333; color: #fff;")

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        # Conecta fileSelected a process_selected_file
        file_dialog.fileSelected.connect(self.process_selected_file)
        file_dialog.exec_()

    def process_selected_file(self, file_path):
        if file_path:  # Verifica si se seleccionó un archivo
            self.process_file(file_path)

    def process_file(self, file_path):
        # eliminar todo antes de agregar nuevas líneas
        scroll_widget = self.scroll_area.widget()
        scroll_layout = scroll_widget.layout()
        while scroll_layout.count():
            child = scroll_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        # agregar la ruta del archivo
        self.file_path_label.setText(file_path)
        # procesar cada línea
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                line_result = process_line(line)
                hbox = QHBoxLayout()
                entry1 = QLineEdit(line_result.removeline)
                entry1.setReadOnly(True)
                entry1.setFixedWidth(50)
                hbox.addWidget(entry1)
                entry2 = QLineEdit(line_result.last_remove_line)
                entry2.setFont(QFont("Arial", 12))
                hbox.addWidget(entry2)
                entry3 = QLineEdit(line_result.real_last_remove_line)
                entry3.setReadOnly(True)
                entry3.setFixedWidth(50)
                hbox.addWidget(entry3)
                self.line_results.append(line_result)

                scroll_widget = self.scroll_area.widget()
                scroll_layout = scroll_widget.layout()
                scroll_layout.addLayout(hbox)

    def save_file(self):
        output_lines = []
        for line_result in self.line_results:
            removeline = line_result.removeline
            last_remove_line = line_result.last_remove_line
            real_last_remove_line = line_result.real_last_remove_line

            for key, value in show_font.items():
                last_remove_line = last_remove_line.replace(key, value)

            output_line = f"{removeline}{last_remove_line}{real_last_remove_line}\n"
            output_lines.append(output_line)

        with open("output.txt", "w", encoding="utf-8") as output_file:
            output_file.writelines(output_lines)

        QMessageBox.information(self, "Save", "File saved successfully.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MyApp()
    window.setWindowTitle('MSG Viewer')
    window.resize(1500, 600)
    window.show()
    sys.exit(app.exec_())
