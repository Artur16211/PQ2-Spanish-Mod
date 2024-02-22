import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


class TextFileEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Archivo de Texto")

        self.default_entry_width = 200  # Ancho por defecto para los campos de entrada

        self.entries = []
        self.checkboxes = []

        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack()

        self.load_button = ttk.Button(
            self.root, text="Abrir archivo", command=self.open_file)
        self.load_button.pack(fill=tk.X)

        # Diccionario para el reemplazo de caracteres
        self.replace_options = {
            'A': 'だ',
            'B': 'ち',
            'C': 'ぢ',
            'D': 'っ',
            'E': 'つ',
            'F': 'づ',
            'G': 'て',
            'H': 'で',
            'I': 'と',
            'J': 'ど',
            'K': 'な',
            'L': 'に',
            'M': 'ぬ',
            'N': 'ね',
            'O': 'の',
            'P': 'は',
            'Q': 'ば',
            'R': 'ぱ',
            'S': 'ひ',
            'T': 'び',
            'U': 'ぴ',
            'V': 'ふ',
            'W': 'ぶ',
            'X': 'ぷ',
            'Y': 'へ',
            'Z': 'べ',
            'a': 'ぺ',
            'b': 'ほ',
            'c': 'ぼ',
            'd': 'ぽ',
            'e': 'ま',
            'f': 'み',
            'g': 'む',
            'h': 'め',
            'i': 'も',
            'j': 'ゃ',
            'k': 'や',
            'l': 'ゅ',
            'm': 'ゆ',
            'n': 'ょ',
            'o': 'よ',
            'p': 'ら',
            'q': 'り',
            'r': 'る',
            's': 'れ',
            't': 'ろ',
            'u': 'ゎ',
            'v': 'わ',
            'w': 'ゐ',
            'x': 'ゑ',
            'y': 'を',
            'z': 'ん',
            'á': 'ァ',
            'Á': 'ア',
            '¡': 'ィ',
            'é': 'イ',
            'É': 'ゥ',
            'í': 'ウ',
            'Í': 'ェ',
            '¿': 'エ',
            'ñ': 'ォ',
            'Ñ': 'オ',
            'ó': 'カ',
            'Ó': 'ガ',
            '/': 'ギ',
            'ú': 'グ',
            'Ú': 'ゲ',
            #
            '0': 'ゼ',
            '1': 'ソ',
            '2': 'ゾ',
            '3': 'タ',
            '4': 'ダ',
            '5': 'チ',
            '6': 'ヂ',
            '7': 'ッ',
            '8': 'ツ',
            '9': 'ヅ',
            '.': 'テ',
            ',': 'デ',
            ':': 'ト',
            '(': 'ド',
            ')': 'ナ',
            # fix old font
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

        # Diccionario invertido para el reemplazo inverso
        self.inverse_replace_options = {
            v: k for k, v in self.replace_options.items()}

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Archivo de texto", "*.msg")])
        if file_path:
            self.load_file(file_path)

    def load_file(self, file_path):
        self.clear_entries()

        def on_configure(event=None):
            # Configurar el scrollregion del canvas para permitir el desplazamiento de todo el contenido
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Crear un canvas con barra de desplazamiento vertical
        canvas = tk.Canvas(self.text_frame)
        scrollbar = tk.Scrollbar(
            self.text_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Contenedor para los elementos
        container = tk.Frame(canvas)
        canvas.create_window((0, 0), window=container, anchor="nw")

        container.bind("<Configure>", on_configure)

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line_frame = tk.Frame(container)
                line_frame.pack(anchor="w", fill="x")

                entry = ttk.Entry(line_frame, width=self.default_entry_width)
                entry.insert(tk.END, line.strip())
                entry.grid(row=0, column=0, sticky="ew")

                checkbox_var = tk.BooleanVar()
                checkbox_var.trace_add("write", lambda name, index, mode,
                                       var=checkbox_var, entry=entry: self.replace_characters(entry, var))
                checkbox = tk.Checkbutton(line_frame, variable=checkbox_var)
                checkbox.grid(row=0, column=1)

                self.entries.append(entry)
                self.checkboxes.append(checkbox_var)

        # Configurar el evento para desplazamiento con rueda de ratón
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mousewheel)

        # Llamar manualmente a on_configure una vez para configurar el scrollregion inicialmente
        on_configure()

        # Configurar la expansión del frame principal y el canvas
        self.text_frame.pack(side="top", fill="both", expand=True)

    def clear_entries(self):
        for entry in self.entries:
            entry.pack_forget()
            entry.destroy()
        self.entries.clear()

        for checkbox in self.checkboxes:
            checkbox.set(False)

    def replace_characters(self, entry, checkbox_var):
        original_text = entry.get()
        if checkbox_var.get():
            updated_text = self.replace_text(
                original_text, self.inverse_replace_options)
        else:
            updated_text = self.replace_text(
                original_text, self.replace_options)
        entry.delete(0, tk.END)
        entry.insert(tk.END, updated_text)

    def replace_text(self, text, replacement_dict):
        inside_brackets = False
        result = ''
        for char in text:
            if char == '[':
                inside_brackets = True
            elif char == ']':
                inside_brackets = False
            if not inside_brackets:
                for key, value in replacement_dict.items():
                    if char == key:
                        char = value
            result += char
        return result

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1250x600")
    root.resizable(False, False)
    editor = TextFileEditor(root)
    editor.run()
