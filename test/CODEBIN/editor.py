import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QScrollArea
import re

def split_content(content):
    parts = []
    i = 0
    current_part = ""
    while i < len(content):
        if content[i:i+2] == '\\x':
            if current_part:
                parts.append(current_part)
                current_part = ""
            parts.append(content[i:i+4])
            i += 4
        else:
            current_part += content[i]
            i += 1
    if current_part:
        parts.append(current_part)
    return parts

class Editor(QWidget):
    def __init__(self, offsets):
        super().__init__()
        self.offsets = offsets
        self.setWindowTitle("Code.bin Editor")
        self.resize(800, 600)
        self.initUI()

        self.found_indices = []
        self.current_index = -1

    def initUI(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.setStyleSheet("""
            QWidget {
                background-color: #000;
                color: #fff;
            }
            QLabel {
                background-color: #000;
                color: #fff;
                border: 1px solid #000;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #555;
            }
            QPushButton {
                background-color: #555;
                color: #fff;
                border: 1px solid #333;
                padding: 5px;
            }
            QLineEdit {
                selection-background-color: #666;
                background-color: #333;
                border: 1px solid #555;
                font-size: 18px;
            }
        
        """)

        self.line_edits = {}

        for offset, content in self.offsets.items():
            label_offset = QLabel(f"{offset}:")
            self.scroll_layout.addWidget(label_offset)

            parts = split_content(content)
            linetext = []

            i = 0
            while i < len(parts):
                part = parts[i]
                if part.startswith('\\x00'):
                    linetext.append(part)
                    # Find the end of the consecutive \x00 parts
                    while i + 1 < len(parts) and parts[i + 1].startswith('\\x00'):
                        linetext.append(parts[i + 1])
                        i += 1
                    # Separate the last \x00 part
                    last_part = linetext.pop()
                    if linetext:
                        self.combine_text_parts(offset, linetext)
                        linetext = []
                    # Add the last \x00 part as QLabel
                    qlabel = QLabel(last_part)
                    self.scroll_layout.addWidget(qlabel)
                elif part.startswith('\\x') and part != '\\x0a':
                    if linetext:
                        self.combine_text_parts(offset, linetext)
                        linetext = []
                    qlabel = QLabel(part)
                    self.scroll_layout.addWidget(qlabel)
                else:
                    linetext.append(part)
                i += 1

            if linetext:
                self.combine_text_parts(offset, linetext)

        scroll_area.setWidget(self.scroll_content)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll_area)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_changes)
        layout.addWidget(save_button)
        
        self.search_input = QLineEdit()
        layout.addWidget(self.search_input)

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_text)
        layout.addWidget(search_button)

        next_button = QPushButton("Next")
        next_button.clicked.connect(self.next_match)
        layout.addWidget(next_button)

        self.setLayout(layout)

    def combine_text_parts(self, offset, text_parts):
        combined_text = ''.join(text_parts)
        qlineedit = QLineEdit()
        combined_text_fix_extra_zeros = combined_text.replace("\\x00", "$")
        qlineedit.setText(combined_text_fix_extra_zeros)
        qlineedit.setMaxLength(len(combined_text_fix_extra_zeros))
        self.scroll_layout.addWidget(qlineedit)
        self.line_edits[offset] = qlineedit

    def save_changes(self):
        updated_offsets = {}

        current_offset = None
        updated_content = []

        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i).widget()

            if isinstance(item, QLabel):
                if item.text().endswith(":"):
                    if current_offset is not None:
                        combined_text = ''.join(updated_content)
                        updated_offsets[current_offset] = combined_text
                        updated_content = []

                    current_offset = item.text()[:-1]
                else:
                    updated_content.append(item.text())
            elif isinstance(item, QLineEdit):
                text = item.text()
                if len(text) < item.maxLength():
                    text += "$" * (item.maxLength() - len(text)) # Rellenar con $ si la longitud es menor
                updated_content.append(text.replace("$", "\\x00"))

        if current_offset is not None:
            combined_text = ''.join(updated_content)
            updated_offsets[current_offset] = combined_text

        with open("modified_content.txt", 'w', encoding='utf-8') as file:
            for offset, content in updated_offsets.items():
                file.write(f"{offset}:\n{content}\n\n")

        QMessageBox.information(self, "Save", "Changes have been saved successfully.")

    def search_text(self):
        self.clear_search_results()
        
        text = self.search_input.text()

        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i).widget()
            if isinstance(item, QLineEdit):
                if text in item.text():
                    self.found_indices.append(i)
                    item.setStyleSheet("background-color: #666900")

        if not self.found_indices:
            QMessageBox.information(self, "Search", "Text not found.")
        else:
            self.current_index = 0
            self.highlight_current_match()

    def next_match(self):
        if not self.found_indices:
            return
            
        self.current_index += 1
        if self.current_index >= len(self.found_indices):
            self.current_index = 0

        self.highlight_current_match()

    def clear_search_results(self):
        for index in self.found_indices:
            item = self.scroll_layout.itemAt(index).widget()
            if isinstance(item, QLineEdit):
                item.setStyleSheet("background-color: #333")
        self.found_indices.clear()

    def highlight_current_match(self):
        for index in self.found_indices:
            item = self.scroll_layout.itemAt(index).widget()
            if isinstance(item, QLineEdit):
                item.setStyleSheet("background-color: #333")

        if not self.found_indices:
            return

        self.current_index %= len(self.found_indices)
        
        item = self.scroll_layout.itemAt(self.found_indices[self.current_index]).widget()
        if isinstance(item, QLineEdit):
            item.setStyleSheet("background-color: #666900")
            item.setFocus()

            scroll_area = self.scroll_content.parentWidget().parentWidget() 
            if isinstance(scroll_area, QScrollArea):
                scroll_widget = self.scroll_layout.itemAt(self.found_indices[self.current_index]).widget()
                scroll_area.ensureWidgetVisible(scroll_widget)
            else:
                print("Error: No se encontró QScrollArea.")



def load_offsets_from_file(filename):
    offsets = {}
    with open(filename, 'r', encoding='utf-8') as file:
        current_offset = None
        current_content = ""
        for line in file:
            if line.startswith("Offset "):
                if current_offset:
                    offsets[current_offset] = current_content.rstrip()
                current_offset = line.split(":")[0].strip()
                current_content = ""
            else:
                current_content += line
        if current_offset:
            offsets[current_offset] = current_content.rstrip()
    return offsets

if __name__ == "__main__":
    extracted_content_file = "modified_content.txt"
    offsets = load_offsets_from_file(extracted_content_file)

    app = QApplication(sys.argv)
    editor = Editor(offsets)
    editor.show()
    sys.exit(app.exec_())
