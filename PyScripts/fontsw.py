import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QScrollArea, QCheckBox

replace_keys = {
    'だ': 'A',
    'ち': 'B',
    'ぢ': 'C',
    'っ': 'D',
    'つ': 'E',
    'づ': 'F',
    'て': 'G',
    'で': 'H',
    'と': 'I',
    'ど': 'J',
    'な': 'K',
    'に': 'L',
    'ぬ': 'M',
    'ね': 'N',
    'の': 'O',
    'は': 'P',
    'ば': 'Q',
    'ぱ': 'R',
    'ひ': 'S',
    'び': 'T',
    'ぴ': 'U',
    'ふ': 'V',
    'ぶ': 'W',
    'ぷ': 'X',
    'へ': 'Y',
    'べ': 'Z',
    'ぺ': 'a',
    'ほ': 'b',
    'ぼ': 'c',
    'ぽ': 'd',
    'ま': 'e',
    'み': 'f',
    'む': 'g',
    'め': 'h',
    'も': 'i',
    'ゃ': 'j',
    'や': 'k',
    'ゅ': 'l',
    'ゆ': 'm',
    'ょ': 'n',
    'よ': 'o',
    'ら': 'p',
    'り': 'q',
    'る': 'r',
    'れ': 's',
    'ろ': 't',
    'ゎ': 'u',
    'わ': 'v',
    'ゐ': 'w',
    'ゑ': 'x',
    'を': 'y',
    'ん': 'z',
    'ァ': 'á',
    'ア': 'Á',
    'ィ': '¡',
    'イ': 'é',
    'ゥ': 'É',
    'ウ': 'í',
    'ェ': 'Í',
    'エ': '¿',
    'ォ': 'ñ',
    'オ': 'Ñ',
    'カ': 'ó',
    'ガ': 'Ó',
    'ギ': '/',
    'グ': 'ú',
    'ゲ': 'Ú',
    'ゼ': '0',
    'ソ': '1',
    'ゾ': '2',
    'タ': '3',
    'ダ': '4',
    'チ': '5',
    'ヂ': '6',
    'ッ': '7',
    'ツ': '8',
    'ヅ': '9',
    'テ': '.',
    'デ': ',',
    'ト': ':',
    'ド': '(',
    'ナ': ')',
    '茨': 'ァ',
    '姻': 'イ',
    '胤': 'ウ',
    '吋': 'カ',
    '雨': 'グ',
    '隠': 'ォ',
    '夷': 'エ',
    '斡': 'ィ',
    '威': 'ア',
    '畏': 'ゥ',
    '緯': 'ェ',
    '遺': 'ガ',
    '郁': 'ゲ',
    '謂': 'オ'
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Font Switcher")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        file_layout = QHBoxLayout()
        layout.addLayout(file_layout)

        file_label = QLabel("Seleccione un archivo:")
        file_layout.addWidget(file_label)

        self.file_line_edit = QLineEdit()
        file_layout.addWidget(self.file_line_edit)

        file_button = QPushButton("Explorar")
        file_button.clicked.connect(self.abrir_explorador)
        file_layout.addWidget(file_button)

        self.scroll_area = QScrollArea()
        layout.addWidget(self.scroll_area)

    def abrir_explorador(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar archivo", "", "Archivos (*.msg)")
        if file:
            self.file_line_edit.setText(file)
            self.show_content(file)

    def show_content(self, file):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content_widget = QWidget()
                content_layout = QVBoxLayout()
                content_widget.setLayout(content_layout)

                i = 0
                for line in f:
                    replaced_text = self.replace_characters(line.strip())

                    entry_layout = QHBoxLayout()

                    checkbox = QCheckBox()
                    entry_layout.addWidget(checkbox)

                    entry = QLineEdit(replaced_text)
                    entry.setReadOnly(True)
                    # Ajusta el ancho mínimo del QLineEdit
                    entry.setMinimumWidth(1000)
                    entry_layout.addWidget(entry)

                    content_layout.addLayout(entry_layout)

                    if replaced_text != line.strip():
                        entry.setStyleSheet("font-weight: bold;")
                        checkbox.setChecked(True)
                        entry.setText('{SmallFont}' + replaced_text)

                    checkbox.stateChanged.connect(
                        lambda state, entry=entry, replaced_text=replaced_text: self.toggle_formatting(entry, state, replaced_text))

                    i += 1

                scroll_content = QWidget()
                scroll_content.setLayout(content_layout)

                self.scroll_area.setWidget(scroll_content)
        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"No se pudo abrir el archivo: {e}")

    def replace_characters(self, line):
        for key, value in replace_keys.items():
            line = line.replace(key, value)
        return line

    def toggle_formatting(self, entry, state, replaced_text):
        if state == 2:  # 2 is equivalent to Qt.Checked
            entry.setText('{SmallFont}' + replaced_text)
            entry.setStyleSheet("font-weight: bold;")
        else:
            entry.setText(replaced_text)
            entry.setStyleSheet("font-weight: normal;")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
