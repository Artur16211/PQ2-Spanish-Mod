import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QScrollArea, QPushButton, QMessageBox, QFileDialog, QCheckBox
from PyQt5.QtCore import QFile, QTextStream, Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from configparser import ConfigParser
import os


class LineResult:
    def __init__(self, removeline, last_remove_line, real_last_remove_line):
        self.removeline = removeline
        self.last_remove_line = last_remove_line
        self.real_last_remove_line = real_last_remove_line


small_font = {
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
    '謂': 'オ',
    #
    "位": 'グ',
    "案": 'カ',
    "按": 'ォ',
}

show_font = {
    "ú": "位",
    "ó": "案",
    "ñ": "按",
    #
    "ú": "グ",
    "ó": "カ",
    #
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
    "Ñ": "謂",
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
    def __init__(self, file_path=None):
        super().__init__()
        self.initUI()
        # self.modified = False
        self.checkBoxes = []  # Lista para mantener referencias a los checkboxes
        if file_path:
            self.process_file(file_path)
        # change the close event handler
        self.closeEvent = self.close_event_handler

    def close_event_handler(self, event):
        # if self.modified:
        reply = QMessageBox.question(self, 'Guardar cambios', "¿Deseas guardar los cambios antes de salir?",
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.save_file()
        elif reply == QMessageBox.Cancel:
            event.ignore()
            return
        event.accept()

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

        # Agregar el botón "openOG"
        open_og_button = QPushButton("OpenOG")
        open_og_button.clicked.connect(self.open_og_file)
        button_layout.addWidget(open_og_button)

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

        # Agregar el QLineEdit para ingresar el texto a buscar
        self.search_line_edit = QLineEdit()
        self.search_line_edit.setPlaceholderText("Search...")
        # change outline color
        self.search_line_edit.setStyleSheet(
            "border: 0.5px solid #646464; border-radius: 10px; padding: 0 8px; color: #fff;")
        self.search_line_edit.textChanged.connect(
            self.search_text)  # Conectar la señal textChanged
        main_layout.addWidget(self.search_line_edit)

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

    def search_text(self):
        search_text = self.search_line_edit.text().strip().lower()
        scroll_content = self.scroll_area.widget()
        layout = scroll_content.layout()

        text_found = False  # Inicializar la variable fuera del bucle

        # Limpiar el estilo CSS de todos los QLineEdit
        for i in range(layout.count()):
            entry_layout = layout.itemAt(i).layout()
            entry = entry_layout.itemAt(2).widget()
            # Limpiar el estilo CSS
            entry.setStyleSheet(
                "")

        if search_text:  # Verificar si la cadena de búsqueda no está vacía
            text_found = False

            # Recorrer todos los QLineEdit en el scroll area y buscar el texto
            for i in range(layout.count()):
                entry_layout = layout.itemAt(i).layout()
                entry = entry_layout.itemAt(2).widget()
                original_text = entry.text().strip().lower()
                if not original_text.startswith("[msg") and not original_text.startswith("["):
                    if search_text in original_text:
                        self.search_line_edit.setStyleSheet(
                            "")  # Limpiar el estilo CSS
                        entry.setStyleSheet(
                            "background-color: #CECB00; color: black;")
                        text_found = True  # Se encontró el texto

                        # Desplazar el área de desplazamiento al primer resultado encontrado
                        scroll_bar = self.scroll_area.verticalScrollBar()
                        # Establecer el valor de desplazamiento
                        scroll_bar.setValue(entry_layout.geometry().top())

            if not text_found:
                # Si no se encontró el texto, marcar de rojo el QLineEdit y quitarlo al volver a escribir
                self.search_line_edit.setStyleSheet(
                    "background-color: #9A0000;")
        else:
            self.search_line_edit.setStyleSheet(
                "border: 0.5px solid #646464; border-radius: 10px; padding: 0 8px; color: #fff;")  # Limpiar el estilo CSS

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
            item = scroll_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                sub_layout = item.layout()
                while sub_layout.count():
                    sub_item = sub_layout.takeAt(0)
                    sub_widget = sub_item.widget()
                    if sub_widget is not None:
                        sub_widget.deleteLater()
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
                checkbox = QCheckBox()
                checkbox.setStyleSheet(
                    "QCheckBox::indicator:checked { background-color: white; border: 1px solid black; }"
                    "QCheckBox::indicator:unchecked { background-color: #262626; border: 1px solid black; }"
                )
                hbox.addWidget(checkbox)
                #
                entry2 = QLineEdit(line_result.last_remove_line)
                entry2.setFont(QFont("Arial", 12))
                small_font_replaced = False
                # replace the text with the small font
                # if exists a character of the small font in the line replace it
                for key, value in small_font.items():
                    if key in entry2.text():
                        entry2.setText(entry2.text().replace(key, value))
                        small_font_replaced = True
                if small_font_replaced:
                    # bold the text and add {SmallFont} start
                    entry2.setFont(QFont("Arial", 12, QFont.Bold))
                    checkbox.setChecked(True)
                    entry2.setText("{SmallFont}" + entry2.text())
                hbox.addWidget(entry2)
                # checkbox to toggle the formatting
                checkbox.stateChanged.connect(
                    lambda state, entry=entry2, replaced_text=line_result.last_remove_line: self.toggle_formatting(entry, state, replaced_text))
                # self.checkBoxes.append(checkbox)
                #
                entry3 = QLineEdit(line_result.real_last_remove_line)
                entry3.setReadOnly(True)
                entry3.setFixedWidth(50)
                hbox.addWidget(entry3)
                self.line_results.append(line_result)

                scroll_widget = self.scroll_area.widget()
                scroll_layout = scroll_widget.layout()
                scroll_layout.addLayout(hbox)

    def toggle_formatting(self, entry, state, replaced_text):
        if state == Qt.Checked:
            entry.setText('{SmallFont}' + replaced_text)
            # replace the text with the small font
            for key, value in small_font.items():
                if key in entry.text():
                    entry.setText(entry.text().replace(key, value))
            entry.setStyleSheet("font-weight: bold;")
        else:
            entry.setText(replaced_text)
            # replace the text with the small font
            for key, value in small_font.items():
                if key in entry.text():
                    entry.setText(entry.text().replace(key, value))
            entry.setStyleSheet("font-weight: normal;")

    def open_og_file(self):
        # Obtener la ruta base del archivo "msgv_pathog.ini"
        base_path = self.get_base_path_from_ini()

        if not base_path:
            base_path = "D:\\Q2\\Dump\\data_usa.cpk_decompiled\\"
        if not os.path.exists(base_path):
            QMessageBox.warning(
                self, "Warning", "No base path found in msgv_pathog.ini file or the path does not exist.")
            return

        # Obtener la ruta del archivo actual seleccionado por el usuario
        current_file_path = self.file_path_label.text()

        # get the last 2 folders of the current file path
        current_file_dir = os.path.basename(os.path.dirname(current_file_path))
        parent_dir = os.path.basename(os.path.dirname(
            os.path.dirname(current_file_path)))

        # print(f"Current file dir: {current_file_dir}")
        # print(f"Parent dir: {parent_dir}")

        actual_file_name = os.path.basename(current_file_path)
        # Sumar la ruta base con las últimas dos carpetas del archivo actual
        og_file_path = os.path.join(
            base_path, parent_dir, current_file_dir, actual_file_name)
        og_file_path2 = os.path.join(
            base_path, current_file_dir, actual_file_name)
        if os.path.exists(og_file_path):
            # open file
            os.startfile(og_file_path)
        elif os.path.exists(og_file_path2):
            os.startfile(og_file_path2)
        else:
            QMessageBox.information(
                self, "Information", "No OG file found in" + f"{base_path}{parent_dir}" + "\\" + f"{current_file_dir}" + "or" + f"{base_path}{current_file_dir}" + "\\" + f"{actual_file_name}")

    def get_base_path_from_ini(self):
        ini_file_path = "msgv_pathog.ini"
        # get the base path from the ini file
        config = ConfigParser()
        config.read(ini_file_path, encoding='utf-8-sig')
        if 'Path' in config:
            return config['Path'].get('base_path', '')
        else:
            # Manejar el caso cuando el archivo INI no existe
            return None

    def update_line_results(self):
        for index, line_result in enumerate(self.line_results):
            entry1 = self.scroll_area.widget().layout().itemAt(index).itemAt(0).widget()
            entry2 = self.scroll_area.widget().layout().itemAt(index).itemAt(2).widget()
            entry3 = self.scroll_area.widget().layout().itemAt(index).itemAt(3).widget()
            # print(f"Line {index + 1} - entry1 text: {entry1.text()} entry2 text: {entry2.text()} - entry3 text: {entry3.text()}")
            removeline = entry1.text()
            last_remove_line = entry2.text()
            real_last_remove_line = entry3.text()
            self.line_results[index] = LineResult(
                removeline, last_remove_line, real_last_remove_line)

    def replace_backwards(self, line):
        replaced_line = ""
        inside_brackets = False

        for char in line:
            if char == '[':
                inside_brackets = True
            elif char == ']':
                inside_brackets = False

            if not inside_brackets:
                for key, value in small_font.items():
                    if char == value:
                        char = key
                        break

            replaced_line += char

        return replaced_line

    def save_file(self):
        self.update_line_results()
        # print(f"Line results: {self.line_results}")

        output_lines = []
        for line_result in self.line_results:
            removeline = line_result.removeline
            last_remove_line = line_result.last_remove_line
            real_last_remove_line = line_result.real_last_remove_line

            for key, value in show_font.items():
                last_remove_line = last_remove_line.replace(key, value)

            # Restore for small font if starts with {SmallFont}
            if last_remove_line.startswith("{SmallFont}"):
                last_remove_line = last_remove_line.replace(
                    "{SmallFont}", "")
                last_remove_line = self.replace_backwards(last_remove_line)

            output_line = f"{removeline}{last_remove_line}{real_last_remove_line}\n"

            output_lines.append(output_line)

        # Obtener la ruta del archivo original
        original_file_path = self.file_path_label.text()

        # Preguntar al usuario antes de sobrescribir el archivo
        reply = QMessageBox.question(self, 'Guardar archivo',
                                     f"¿Desea guardar los cambios en {original_file_path}?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Guardar el archivo en la misma ruta que el original
            with open(original_file_path, "w", encoding="utf-8") as output_file:
                output_file.writelines(output_lines)
            QMessageBox.information(
                self, "Guardar", "Archivo guardado exitosamente.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    if len(sys.argv) > 1:
        window = MyApp(sys.argv[1])
    else:
        window = MyApp()
    window.setWindowTitle('MSG Viewer')
    window.resize(1500, 600)
    window.show()
    sys.exit(app.exec_())
