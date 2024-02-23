import tkinter as tk
from tkinter import filedialog, messagebox

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


def abrir_explorador():
    file = filedialog.askopenfilename(filetypes=[("file", "*.msg")])
    if file:
        entrada_file.delete(0, tk.END)
        entrada_file.insert(tk.END, file)
        show_content(file)

        save_button = tk.Button(root, text="Guardar",
                                command=lambda: save_content(file))
        save_button.pack(side=tk.TOP, padx=5, pady=5)


def save_content(file):
    try:
        with open(file, 'w', encoding='utf-8') as f:
            for widget in frame.winfo_children():
                if isinstance(widget, tk.Entry):
                    text = widget.get().strip()
                    if text.startswith('{SmallFont}'):
                        # Reemplazar inversamente utilizando el diccionario
                        text = ''.join(replace_keys.get(char, char)
                                       for char in text[11:])
                    f.write(text + '\n')
        messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")


def show_content(file):
    encode = ['utf-8']

    for codificacion in encode:
        try:
            with open(file, 'r', encoding=codificacion) as f:
                lines = f.readlines()
                for widget in frame.winfo_children():
                    widget.destroy()
                for i, line in enumerate(lines):
                    replaced_text = replace_characters(line.strip())
                    entry_variable = tk.StringVar()
                    entry_variable.set(replaced_text)
                    entry = tk.Entry(
                        frame, textvariable=entry_variable, width=90, justify='left', font=('Arial', 10))
                    entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
                    checkbox_var = tk.BooleanVar()
                    if replaced_text != line.strip():
                        # Aplicar negritas solo si hay reemplazo
                        entry.config(font=('Arial', 10, 'bold'))
                        # agregar {SmallFont} al inicio del texto
                        entry_variable.set('{SmallFont}' + replaced_text)
                        checkbox_var = tk.BooleanVar(value=True)
                    checkbox = tk.Checkbutton(frame, variable=checkbox_var, command=lambda entry=entry,
                                              checkbox_var=checkbox_var: toggle_formatting(entry, checkbox_var))
                    checkbox.grid(row=i, column=0, padx=5)

                canvas.config(scrollregion=canvas.bbox("all"))
                return
        except Exception as e:
            print(
                f"Error al abrir el archivo con codificación '{codificacion}': {e}")

    messagebox.showerror(
        "Error", "No se pudo abrir el archivo con ninguna codificación.")


def replace_characters(line):
    for key, value in replace_keys.items():
        line = line.replace(key, value)
    return line


def toggle_formatting(entry, checkbox_var):
    entry_text = entry.get()
    if checkbox_var.get():
        # check if the text is not already formatted
        if not '{SmallFont}' in entry_text or 'bold' in entry.cget('font'):
            entry_text = '{SmallFont}' + entry_text
            entry.config(font=('Arial', 10, 'bold'))
    else:
        entry_text = entry_text.replace(
            '{SmallFont}', '')
        entry.config(font=('Arial', 10))
    entry.delete(0, tk.END)
    entry.insert(tk.END, entry_text)


def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


def on_mousewheel(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


root = tk.Tk()
root.title("Font Switcher")

tk.Label(root, text="Seleccione un archivo:").pack()
frame_file = tk.Frame(root)
frame_file.pack(fill=tk.X)

entrada_file = tk.Entry(frame_file)
entrada_file.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

boton_explorador = tk.Button(
    frame_file, text="Explorar", command=abrir_explorador)
boton_explorador.pack(side=tk.LEFT)

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

frame.bind("<Configure>", on_frame_configure)

root.bind_all("<MouseWheel>", on_mousewheel)

frame.bindtags((str(frame), "Frame", ".", "all"))
for child in frame.winfo_children():
    child.bindtags((str(child), child.winfo_class(), ".", "all"))

frame.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()
