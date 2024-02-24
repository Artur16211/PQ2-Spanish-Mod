import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QScrollArea
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtGui import QFont


class LineResult:
    def __init__(self, removeline, last_remove_line, real_last_remove_line):
        self.removeline = removeline
        self.last_remove_line = last_remove_line
        self.real_last_remove_line = real_last_remove_line


def process_line(line):
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
        layout = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        with open("input.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                # if line:
                line_result = process_line(line)
                hbox = QHBoxLayout()
                layout.addLayout(hbox)
                # hbox.addWidget(QLabel("Removeline:"))
                entry1 = QLineEdit(line_result.removeline)
                entry1.setReadOnly(True)
                # change size of the entry
                entry1.setFixedWidth(50)
                hbox.addWidget(entry1)
                # hbox.addWidget(QLabel("LastRemoveLine:"))
                entry2 = QLineEdit(line_result.last_remove_line)
                # change text size
                entry2.setFont(QFont("Arial", 12))
                hbox.addWidget(entry2)
                # hbox.addWidget(QLabel("RealLastRemoveLine:"))
                entry3 = QLineEdit(line_result.real_last_remove_line)
                entry3.setReadOnly(True)
                # change size of the entry
                entry3.setFixedWidth(50)
                hbox.addWidget(entry3)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

        # Aplicar el tema oscuro
        self.setStyleSheet("background-color: #333; color: #fff;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Aplicar estilo Fusion para una apariencia uniforme en todos los sistemas operativos
    app.setStyle("Fusion")
    window = MyApp()
    window.setWindowTitle('MSG Viewer')
    # change the window size
    window.resize(1500, 600)
    window.show()
    sys.exit(app.exec_())
