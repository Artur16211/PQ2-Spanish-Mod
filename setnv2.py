import os
import subprocess
import shutil

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter
import sv_ttk
import sys
import configparser
import re

from tkinter import filedialog
# from deep_translator import GoogleTranslator


class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.config(state=tk.NORMAL)
        self.widget.insert(tk.END, str, (self.tag,))
        self.widget.see(tk.END)
        self.widget.config(state=tk.DISABLED)
        self.widget.update()
        root.update()

    def flush(self):
        pass


# Make a config parser
config = configparser.ConfigParser()

# Read the config file if it exists
if os.path.isfile('config.ini'):
    config.read('config.ini')
else:
    # If it doesn't exist, create it with default values
    config['Folders'] = {'mod_folder': '',
                         'output_folder': '', 'game': 'Persona Q2'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

# Get the saved values or set default values if they don't exist
mod_folder = config.get('Folders', 'mod_folder', fallback='')
# language_folder = config.get('Folders', 'language_folder', fallback='')
output_folder = config.get('Folders', 'output_folder', fallback='')
game = config.get('Folders', 'game', fallback='Persona 5 Royal')

root = customtkinter.CTk()


def disable_button():
    run_button.config(state="disabled")
    dropdown.config(state="disable")
    mod_folder_button.config(state="disable")
    language_folder_button.config(state="disable")
    output_folder_button.config(state="disable")
    mod_folder_entry.config(state="disable")
    language_folder_entry.config(state="disable")
    output_folder_entry.config(state="disable")
    checkbox.config(state="disable")


def enable_button():
    run_button.config(state="normal")
    dropdown.config(state="normal")
    mod_folder_button.config(state="normal")
    # language_folder_button.config(state="normal")
    output_folder_button.config(state="normal")
    mod_folder_entry.config(state="normal")
    # language_folder_entry.config(state="normal")
    output_folder_entry.config(state="normal")
    checkbox.config(state="normal")


# Log box with scrollbar and no text editing
log_box = tk.Text(root, height=20, width=50)
log_box.grid(row=5, columnspan=3, column=0, sticky='ew')
# use columnspan to make the widget span multiple columns
# log_box.grid(columnspan=2)
# Create a scrollbar and associate it with log_box
scrollbar = ttk.Scrollbar(root, command=log_box.yview)
scrollbar.grid(row=5, column=4, sticky='ns')
# Disable editing
log_box.config(state=tk.DISABLED, yscrollcommand=scrollbar.set)


sys.stdout = TextRedirector(log_box, "stdout")


def on_select(event):
    # Make the variable global so it can be used
    global game
    game = dropdown.get()
    # Clear the log box
    log_box.config(state=tk.NORMAL)
    log_box.delete('1.0', tk.END)
    log_box.config(state=tk.DISABLED)
    print(f"Game: {game}")


# Options for the dropdown
options = ["Persona 5 Royal", "Persona 5", "Persona Q2"]

# Make the dropdown
dropdown = ttk.Combobox(root, values=options)

# Check if the saved value in the config file exists in the options list
if game in options:
    # Set the saved value in the config file as the default option
    dropdown.current(options.index(game))
else:
    dropdown.current(0)

# Disable write in the dropdown
dropdown.configure(state="readonly")

# Add the on_select function to the dropdown
dropdown.bind("<<ComboboxSelected>>", on_select)

# Run the on_select function when the program starts
on_select(None)

# Set the position of the dropdown in the window
dropdown.grid(row=3, column=0, padx=10, pady=10)

# checkbox para cambiar el estado de una variable


# Disable SetN
def on_check():
    global setn
    setn = check_var.get()
    # clear the log box
    log_box.config(state=tk.NORMAL)
    log_box.delete('1.0', tk.END)
    log_box.config(state=tk.DISABLED)
    # print(f"setn: {setn}")
    if setn == 1:
        print("SetN desactivado")
    # else:
        # print("SetN activado")
    print(f"Game: {game}")


# Make the checkbox
check_var = tk.IntVar()
checkbox = ttk.Checkbutton(root, text="Desactivar SetN",
                           variable=check_var, command=on_check)

checkbox.grid(row=4, column=0, padx=10, pady=10)

# Run the on_check function when the program starts
on_check()
# Disable SetN

# specify the size of the window
root.geometry("820x600")

# disable resizing the GUI
root.resizable(False, False)


def browse_mod_folder():
    mod_folder = filedialog.askdirectory()
    mod_folder_entry.delete(0, tk.END)
    mod_folder_entry.insert(0, mod_folder)


def browse_language_folder():
    language_folder = filedialog.askdirectory()
    language_folder_entry.delete(0, tk.END)
    language_folder_entry.insert(0, language_folder)


def browse_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, output_folder)


def run_program():
    if not mod_folder_entry.get() or not output_folder_entry.get():
        messagebox.showerror(
            "Error", "Please fill in all fields.")
        return
    disable_button()
    # Clear the log box
    log_box.config(state=tk.NORMAL)
    log_box.delete('1.0', tk.END)
    log_box.config(state=tk.DISABLED)

    mod_folder = mod_folder_entry.get()
    output_folder = output_folder_entry.get()

    # List files and folders in mod_folder including those in subfolders and full path
    mod_files_list = []
    for root, dirs, files in os.walk(mod_folder):
        for file in files:
            path = os.path.join(root, file)
            mod_files_list.append(path)

    # Delete the value of mod_folder from the path
    mod_files_list = [x.replace(mod_folder, '') for x in mod_files_list]

    mod_files_list_updated = []
    for root, dirs, files in os.walk(mod_folder):
        for file in files:
            path = os.path.join(root, file)
            mod_files_list_updated.append(path)

    # Delete the path of mod_folder from the list
    mod_files_list_updated = [x.replace(mod_folder, '')
                              for x in mod_files_list_updated]

    # Path to the dependencies
    personaeditor_path = os.path.join(
        'dependencies', 'personaeditor', 'personaeditorcmd.exe')
    atlus_script_tools_path = os.path.join(
        "dependencies", "atlusscripttools", "AtlusScriptCompiler.exe")

    # Current directory
    current_dir = os.path.abspath(os.path.dirname(__file__))

    def ASCCompile(input_file_path):
        input_file_name = os.path.basename(input_file_path)
        if game == "Persona 5 Royal":
            print(f"Compiling BMD file: {input_file_name} with P5R library")
            output_file_path = os.path.splitext(input_file_path)[0] + '.bmd'
            subprocess.run([atlus_script_tools_path, input_file_path, "-Out",
                            output_file_path, "-Compile", "-OutFormat", "V1BE", "-Library", "P5R", "-Encoding", "P5"])
        elif game == "Persona 5":
            print(f"Compiling BMD file: {input_file_name} with P5 library")
            output_file_path = os.path.splitext(input_file_path)[0] + '.bmd'
            subprocess.run([atlus_script_tools_path, input_file_path, "-Out",
                            output_file_path, "-Compile", "-OutFormat", "V1BE", "-Library", "P5", "-Encoding", "P5"])
        elif game == "Persona Q2":
            # print(f"Compiling BMD file: {input_file_name} with PQ2 library")
            output_file_path = os.path.splitext(input_file_path)[0] + '.bmd'
            subprocess.run([atlus_script_tools_path, input_file_path, "-Out",
                            output_file_path, "-Compile", "-OutFormat", "V1", "-Library", "PQ2", "-Encoding", "SJ"])

    def PEImport(input_file_path):
        subprocess.run([personaeditor_path, input_file_path,
                        '-impall', '-save', input_file_path])

    # replace
    def process_msg(name_file):

        # get the name of the file without the extension and add .msg
        name_file_msg = os.path.splitext(name_file)[0] + '.msg'

        # Read the lines of the mod .msg file and replace line = replace_brackets(line) when not starting with [msg or empty line or //
        with open(name_file_msg, 'r', encoding='utf-8-sig', errors='ignore') as f:
            linesbfix = f.readlines()

        # make a list with the msg
        mod_msgs = []
        # list with names
        mod_msg_names = []

        match = r"\[[^\[\]]*\]|\[[^\[]*[^\s\[\]]\]"

        # Read the lines of the mod .msg file when not starting with [msg or empty line or // and create a list with the lines
        with open(name_file_msg, 'r', encoding='utf-8-sig', errors='ignore') as f:
            for line in f:
                if not line.startswith('[msg') and not line.startswith('//') and not line.strip() == '' and not line.startswith('[sel'):
                    # Apply regular expression to remove text between brackets
                    result = []
                    position = 0
                    while True:
                        coincidencia = re.search(match, line[position:])
                        if coincidencia:
                            result.append(coincidencia.group(0))
                            position += coincidencia.end()
                        else:
                            break

                        # Check if the next character is a space or a bracket
                        if len(line[position:].strip()) == 0 or line[position:position+5] == "[var " or line[position:position+7] == "[f 4 1]" or line[position:position+7] == "[f 4 2]" or line[position:position+5] == "[clr " or line[position:position+5] == "[Navi" or line[position] != "[":
                            break

                    # Remove the text between brackets and the characters "[w]" and "[e]"
                    for item in result:
                        line = line.replace(item, "")
                    line = line.replace("[w]", "").replace("[e]", "")
                    for item in result:
                        line = line.replace("縲縲", "").replace(
                            "縲縲", "").replace("　　", "")
                        line = re.sub(
                            r'\[n\]\[f \d+ \d+ \d+ \d+ \d+.*?\]', '', line)
                    last_occurrence_index = line.rfind("[n]")
                    if game == "Persona Q2":
                        # Delete all lines after the last occurrence of "[n]"
                        if last_occurrence_index != -1:
                            line = line[:last_occurrence_index]
                        # if line no find "[n]", find the last [
                        else:
                            last_occurrence_index = line.rfind("[")
                            if last_occurrence_index != -1:
                                line = line[:last_occurrence_index]
                            # add "# " in start of the line to differentiate the sel lines
                            line = "# " + line
                            # Remove # for tutorial ↑
                    if game == "Persona 5" or game == "Persona 5 Royal":
                        if last_occurrence_index != -1:
                            line = line[:last_occurrence_index] + \
                                line[last_occurrence_index:].replace(
                                    "[n]", "", 1)
                    # add the line to the list
                    # print(f"Line: {line}")
                    mod_msgs.append(line)
                # [msg names

        # Make a list with the messages in spanish
        mod_msgs_nfix = []

        # fill the mod_msgs_nfix list with the content of the mod_msgs list
        for line in mod_msgs:
            mod_msgs_nfix.append(line)

        replacement_dict = {
            'á': '茨',
            'é': '姻',
            'í': '胤',
            'ó': '吋',
            'ú': '雨',
            'ñ': '隠',
            '¿': '夷',
            '¡': '斡',
            'Á': '威',
            'É': '畏',
            'Í': '緯',
            'Ó': '遺',
            'Ú': '郁',
            'Ñ': '謂',
            '吋': '吋',
            '係': '茨',
            '契': '姻',
            '慶': '胤',
            '矩': '吋',
            '具': '雨',
            '狗': '隠',
            '空': '夷',
            '緊': '斡',
            '寓': '威',
            '掘': '畏',
            '轡': '緯',
            '繰': '遺',
            '訓': '郁',
            '粂': '謂',
            'Sub-Personas': 'Personas Secundarias',
            'Sub-Persona': 'Persona Secundaria',
        }

        def replace_characters(text, replacement_dict):
            for key in replacement_dict:
                text = text.replace(key, replacement_dict[key])
            return text

        # Replace the characters in the list
        for i in range(len(mod_msgs_nfix)):
            mod_msgs_nfix[i] = replace_characters(
                mod_msgs_nfix[i], replacement_dict)

        # print(mod_msg_names_es)
        # Create a dictionary with the messages in english as keys and the messages in spanish as values
        mod_msgs_dict = dict(zip(mod_msgs, mod_msgs_nfix))

        # print the dictionary
        # for key, value in mod_msgs_dict.items():
        # print(key, ' : ', value)

        # Copy the .msg file to the output folder
        name_file_output = name_file_msg.replace(mod_folder, output_folder)

        print(
            f"Reemplazando mensajes en el archivo .msg de {name_file_output}...")

        # la carpeta del archivo es la siguiente despues de la carpeta "setn"

        # Convertir la ruta a minúsculas
        name_file_output_2 = name_file_output.lower()

        name_file_output_2 = name_file_output_2.replace('/', '\\')

        # print(f"Ruta en minúsculas: {name_file_output_2}")

        # Dividir la ruta en partes
        path_parts = name_file_output_2.split(os.path.sep)

        # Encontrar el índice de la carpeta 'setn'
        index_setn = path_parts.index('setn')

        # Obtener la carpeta después de 'setn'
        folder_name_msg = path_parts[index_setn + 1]

        # try:
        # Encontrar el índice de la carpeta 'setn'
        # index_setn = path_parts.index('setn')

        # Obtener la carpeta después de 'setn'
        # folder_name_msg = path_parts[index_setn + 1]
        # print(f"Carpeta después de 'setn': {folder_name_msg}")
        # except ValueError:
        # print("'setn' no encontrado en la ruta.")

        for key, value in mod_msgs_dict.items():
            if value is not None:
                # delete all [n] from the lines
                value = value.replace("[n]", " ")
                # si no empieza por #
                if not value.startswith("# "):
                    if setn != 1:
                        # obtener el nombre de la carpeta, ya sea: "battle, camp, dungeon, event, facility, init, shared, tutorial" dependiendo de la carpeta en la que se encuentre el archivo .msg, se aplicara un intervalo diferente
                        # Cambiar el 43 dependiendo del tipo de dialogo, 43 para los eventos
                        if folder_name_msg == "battle":
                            # if after path_parts[index_setn + 1] is "battle", and after battle is "event", use interval 43
                            if path_parts[index_setn + 2] == "event" or path_parts[index_setn + 2] == "combination":
                                # print("La carpeta es battle/event, usando intervalo 43")

                                def insert_n_character(line, interval=43):
                                    target_position = interval

                                    intervalo_div = int(target_position / 43)

                                    if intervalo_div != 1:
                                        target_position += 3 * intervalo_div

                                    if len(line) <= target_position or len(line) <= target_position + 2:
                                        return line

                                    left_bracket = line.rfind(
                                        '[', 0, target_position)
                                    right_bracket = line.find(
                                        ']', target_position)

                                    if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                        sum_brackets = line[left_bracket:right_bracket + 1]
                                        target_position += len(sum_brackets)

                                    last_space_position = line.rfind(
                                        ' ', 0, target_position)

                                    if last_space_position == -1:
                                        return line
                                    else:
                                        target_position = last_space_position

                                    line = line[:target_position] + \
                                        '[n]' + line[target_position + 1:]

                                    return insert_n_character(line, interval=interval + 43)

                                value = insert_n_character(value)
                            else:
                                # print("La carpeta es battle (navegadores), usando intervalo 36")

                                # Los caracteres no deben pasar de 41, por eso se usa un intervalo de 34
                                def insert_n_character(line, interval=34):
                                    target_position = interval

                                    intervalo_div = int(target_position / 34)

                                    if intervalo_div != 1:
                                        target_position += 3 * intervalo_div

                                    if len(line) <= target_position or len(line) <= target_position + 2:
                                        return line

                                    left_bracket = line.rfind(
                                        '[', 0, target_position)
                                    right_bracket = line.find(
                                        ']', target_position)

                                    if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                        sum_brackets = line[left_bracket:right_bracket + 1]
                                        target_position += len(sum_brackets)

                                    last_space_position = line.rfind(
                                        ' ', 0, target_position)

                                    if last_space_position == -1:
                                        return line
                                    else:
                                        target_position = last_space_position

                                    line = line[:target_position] + \
                                        '[n]' + line[target_position + 1:]

                                    return line

                                value = insert_n_character(value)
                        elif folder_name_msg == "camp":
                            # print("La carpeta es camp, usando intervalo 43")

                            def insert_n_character(line, interval=43):
                                target_position = interval

                                intervalo_div = int(target_position / 43)

                                if intervalo_div != 1:
                                    target_position += 3 * intervalo_div

                                if len(line) <= target_position or len(line) <= target_position + 2:
                                    return line

                                left_bracket = line.rfind(
                                    '[', 0, target_position)
                                right_bracket = line.find(
                                    ']', target_position)

                                if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                    sum_brackets = line[left_bracket:right_bracket + 1]
                                    target_position += len(sum_brackets)

                                last_space_position = line.rfind(
                                    ' ', 0, target_position)

                                if last_space_position == -1:
                                    return line
                                else:
                                    target_position = last_space_position

                                line = line[:target_position] + \
                                    '[n]' + line[target_position + 1:]

                                return insert_n_character(line, interval=interval + 43)

                            value = insert_n_character(value)
                        elif folder_name_msg == "dungeon":
                            if path_parts[index_setn + 2] == "script" and path_parts[index_setn + 3] == "support":
                                # print("La carpeta es dungeon, usando intervalo 43")

                                def insert_n_character(line, interval=34):
                                    target_position = interval

                                    intervalo_div = int(target_position / 34)

                                    if intervalo_div != 1:
                                        target_position += 3 * intervalo_div

                                    if len(line) <= target_position or len(line) <= target_position + 2:
                                        return line

                                    left_bracket = line.rfind(
                                        '[', 0, target_position)
                                    right_bracket = line.find(
                                        ']', target_position)

                                    if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                        sum_brackets = line[left_bracket:right_bracket + 1]
                                        target_position += len(sum_brackets)

                                    last_space_position = line.rfind(
                                        ' ', 0, target_position)

                                    if last_space_position == -1:
                                        return line
                                    else:
                                        target_position = last_space_position

                                    line = line[:target_position] + \
                                        '[n]' + line[target_position + 1:]

                                    return line
                                value = insert_n_character(value)
                            else:
                                def insert_n_character(line, interval=43):
                                    target_position = interval

                                    intervalo_div = int(target_position / 43)

                                    if intervalo_div != 1:
                                        target_position += 3 * intervalo_div

                                    if len(line) <= target_position or len(line) <= target_position + 2:
                                        return line

                                    left_bracket = line.rfind(
                                        '[', 0, target_position)
                                    right_bracket = line.find(
                                        ']', target_position)

                                    if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                        sum_brackets = line[left_bracket:right_bracket + 1]
                                        target_position += len(sum_brackets)

                                    last_space_position = line.rfind(
                                        ' ', 0, target_position)

                                    if last_space_position == -1:
                                        return line
                                    else:
                                        target_position = last_space_position

                                    line = line[:target_position] + \
                                        '[n]' + line[target_position + 1:]

                                    return insert_n_character(line, interval=interval + 43)
                            value = insert_n_character(value)
                        elif folder_name_msg == "event":
                            # print("La carpeta es event, usando intervalo 43")

                            # Los caracteres no deben pasar de 47, por eso se usa un intervalo de 43
                            def insert_n_character(line, interval=43):
                                target_position = interval

                                intervalo_div = int(target_position / 43)

                                if intervalo_div != 1:
                                    target_position += 3 * intervalo_div

                                if len(line) <= target_position or len(line) <= target_position + 2:
                                    return line

                                left_bracket = line.rfind(
                                    '[', 0, target_position)
                                right_bracket = line.find(
                                    ']', target_position)

                                if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                    sum_brackets = line[left_bracket:right_bracket + 1]
                                    target_position += len(sum_brackets)

                                last_space_position = line.rfind(
                                    ' ', 0, target_position)

                                if last_space_position == -1:
                                    return line
                                else:
                                    target_position = last_space_position

                                line = line[:target_position] + \
                                    '[n]' + line[target_position + 1:]

                                return insert_n_character(line, interval=interval + 43)

                            value = insert_n_character(value)
                        elif folder_name_msg == "facility":
                            if path_parts[index_setn + 2] == "townsupport.bmd.msg":
                                # print("La carpeta es battle (navegadores), usando intervalo 36")

                                # Los caracteres no deben pasar de 41, por eso se usa un intervalo de 34
                                def insert_n_character(line, interval=34):
                                    target_position = interval

                                    intervalo_div = int(target_position / 34)

                                    if intervalo_div != 1:
                                        target_position += 3 * intervalo_div

                                    if len(line) <= target_position or len(line) <= target_position + 2:
                                        return line

                                    left_bracket = line.rfind(
                                        '[', 0, target_position)
                                    right_bracket = line.find(
                                        ']', target_position)

                                    if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                        sum_brackets = line[left_bracket:right_bracket + 1]
                                        target_position += len(sum_brackets)

                                    last_space_position = line.rfind(
                                        ' ', 0, target_position)

                                    if last_space_position == -1:
                                        return line
                                    else:
                                        target_position = last_space_position

                                    line = line[:target_position] + \
                                        '[n]' + line[target_position + 1:]

                                    return line

                                value = insert_n_character(value)
                            else:
                                # print("La carpeta es facility, usando intervalo 43")
                                def insert_n_character(line, interval=43):
                                    target_position = interval

                                    intervalo_div = int(target_position / 43)

                                    if intervalo_div != 1:
                                        target_position += 3 * intervalo_div

                                    if len(line) <= target_position or len(line) <= target_position + 2:
                                        return line

                                    left_bracket = line.rfind(
                                        '[', 0, target_position)
                                    right_bracket = line.find(
                                        ']', target_position)

                                    if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                        sum_brackets = line[left_bracket:right_bracket + 1]
                                        target_position += len(sum_brackets)

                                    last_space_position = line.rfind(
                                        ' ', 0, target_position)

                                    if last_space_position == -1:
                                        return line
                                    else:
                                        target_position = last_space_position

                                    line = line[:target_position] + \
                                        '[n]' + line[target_position + 1:]

                                    return insert_n_character(line, interval=interval + 43)

                                value = insert_n_character(value)
                        elif folder_name_msg == "init":
                            # print("La carpeta es init, usando intervalo 40")

                            # Los caracteres no deben pasar de 45, por eso se usa un intervalo de 40
                            def insert_n_character(line, interval=40):
                                target_position = interval

                                intervalo_div = int(target_position / 40)

                                if intervalo_div != 1:
                                    target_position += 3 * intervalo_div

                                if len(line) <= target_position or len(line) <= target_position + 2:
                                    return line

                                left_bracket = line.rfind(
                                    '[', 0, target_position)
                                right_bracket = line.find(
                                    ']', target_position)

                                if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                    sum_brackets = line[left_bracket:right_bracket + 1]
                                    target_position += len(sum_brackets)

                                last_space_position = line.rfind(
                                    ' ', 0, target_position)

                                if last_space_position == -1:
                                    return line
                                else:
                                    target_position = last_space_position

                                line = line[:target_position] + \
                                    '[n]' + line[target_position + 1:]

                                return line

                            value = insert_n_character(value)
                        elif folder_name_msg == "shared":
                            # print("La carpeta es shared, usando intervalo 43")

                            def insert_n_character(line, interval=43):
                                target_position = interval

                                intervalo_div = int(target_position / 43)

                                if intervalo_div != 1:
                                    target_position += 3 * intervalo_div

                                if len(line) <= target_position or len(line) <= target_position + 2:
                                    return line

                                left_bracket = line.rfind(
                                    '[', 0, target_position)
                                right_bracket = line.find(
                                    ']', target_position)

                                if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                    sum_brackets = line[left_bracket:right_bracket + 1]
                                    target_position += len(sum_brackets)

                                last_space_position = line.rfind(
                                    ' ', 0, target_position)

                                if last_space_position == -1:
                                    return line
                                else:
                                    target_position = last_space_position

                                line = line[:target_position] + \
                                    '[n]' + line[target_position + 1:]

                                return insert_n_character(line, interval=interval + 43)

                            value = insert_n_character(value)
                        elif folder_name_msg == "tutorial":
                            # print("La carpeta es tutorial, usando intervalo 52")

                            # Los caracteres no deben pasar de 56, por eso se usa un intervalo de 52
                            def insert_n_character(line, interval=52):
                                target_position = interval

                                intervalo_div = int(target_position / 52)

                                if intervalo_div != 1:
                                    target_position += 3 * intervalo_div

                                if len(line) <= target_position or len(line) <= target_position + 2:
                                    return line

                                left_bracket = line.rfind(
                                    '[', 0, target_position)
                                right_bracket = line.find(
                                    ']', target_position)

                                if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                    sum_brackets = line[left_bracket:right_bracket + 1]
                                    target_position += len(sum_brackets)

                                last_space_position = line.rfind(
                                    ' ', 0, target_position)

                                if last_space_position == -1:
                                    return line
                                else:
                                    target_position = last_space_position

                                line = line[:target_position] + \
                                    '[n]' + line[target_position + 1:]

                                return insert_n_character(line, interval=interval + 52)

                            value = insert_n_character(value)
                        else:
                            # print("La carpeta no coincide con ninguna, usando intervalo 43, al igual que en event")
                            def insert_n_character(line, interval=43):
                                target_position = interval

                                intervalo_div = int(target_position / 43)

                                if intervalo_div != 1:
                                    target_position += 3 * intervalo_div

                                if len(line) <= target_position or len(line) <= target_position + 2:
                                    return line

                                left_bracket = line.rfind(
                                    '[', 0, target_position)
                                right_bracket = line.find(
                                    ']', target_position)

                                if left_bracket != -1 and right_bracket != -1 and left_bracket < target_position and right_bracket > target_position:

                                    sum_brackets = line[left_bracket:right_bracket + 1]
                                    target_position += len(sum_brackets)

                                last_space_position = line.rfind(
                                    ' ', 0, target_position)

                                if last_space_position == -1:
                                    return line
                                else:
                                    target_position = last_space_position

                                line = line[:target_position] + \
                                    '[n]' + line[target_position + 1:]

                                return insert_n_character(line, interval=interval + 43)

                            value = insert_n_character(value)
                    else:
                        # al desactivar setn, se usa un intervalo de 500, de esta forma se evita que se agregue el [n] en los mensajes que no lo necesitan (teniendo en cuenta que ningun mensaje tendra mas de 500 caracteres)
                        # print("SetN desactivado, usando intervalo 500")

                        def insert_n_character(line, interval=500):
                            target_position = interval
                            if len(line) <= target_position or len(line) <= target_position + 2:
                                return line

                            left_bracket = line.rfind(
                                '[', 0, target_position)
                            right_bracket = line.find(
                                ']', target_position)

                            # check if the target position is inside a bracket
                            if left_bracket != -1 and right_bracket != -1 and left_bracket < right_bracket:
                                insert_position = right_bracket + 1
                            else:
                                left_space = line.rfind(
                                    ' ', 0, target_position)
                                right_space = line.find(
                                    ' ', target_position)

                                if left_space == -1 and right_space == -1:
                                    return line
                                if left_space == -1:
                                    insert_position = right_space
                                elif right_space == -1:
                                    insert_position = left_space + 1
                                else:
                                    if abs(target_position - left_space) <= abs(right_space - target_position):
                                        insert_position = left_space + 1
                                    else:
                                        insert_position = right_space

                            line = line[:insert_position] + \
                                '[n]' + line[insert_position:]
                            # Cambiar el 43 dependiendo del tipo de dialogo, 43 para los eventos
                            return insert_n_character(line, interval=interval + 500)

                        value = insert_n_character(value)
                # Delete the spaces before and after the [n]
                value = value.replace(' [n] ', '[n]').replace(
                    ' [n]', '[n]').replace('[n] ', '[n]')
                # replace the fix_dict to fix compile errors
                value = value.replace('[f[n]0 1 0]', '[n][f 0 1 0]').replace(
                    '[f 0 1[n]8]', '[n][f 0 1 8]').replace('[f[n]6 1 4 0 30]', '[n][f 6 1 4 0 30]')
                # La primera letra del mensaje debe ser mayúscula
                if len(value) > 0:
                    value = value[0].upper() + value[1:]
                # Delete "# "
                if value.startswith("# "):
                    value = value[2:]
                mod_msgs_dict[key] = value

        # Crear una lista para almacenar las claves a modificar
        keys_to_modify = []

        # Identificar las claves que necesitan modificación
        for key in mod_msgs_dict:
            if key.startswith("# "):
                keys_to_modify.append(key)

        # Modificar las claves después de la iteración
        for key in keys_to_modify:
            value = mod_msgs_dict[key]
            new_key = key[2:]
            del mod_msgs_dict[key]
            mod_msgs_dict[new_key] = value

        # Replace the text strings that match the dictionary keys
        with open(name_file_output, 'r', encoding='utf-8-sig', errors='ignore') as f:
            filedata = f.read()

        for key, value in mod_msgs_dict.items():
            if value is not None:
                filedata = filedata.replace(key, value)

        with open(name_file_output + ".tmp", 'w', encoding='utf-8-sig', errors='ignore') as f:
            f.write(filedata)

        # Delete the original file
        os.remove(name_file_output)
        # Rename the temporary file to the original name
        os.rename(name_file_output + ".tmp", name_file_output)

    # def fix_FemMC(name_file):
    #     # read the lines of the file
    #     with open(name_file, 'r', encoding='utf-8-sig', errors='ignore') as f:
    #         lines = f.readlines()
    #     # the next line after the line what finish with [P3 Fem Protag]] is the line to modify
    #     for i in range(len(lines)):
    #         if lines[i].endswith("[P3 Fem Protag]]\n"):
    #             lines[i+1] = lines[i+1].replace(
    #                # replace [f 1 5][f 6 1 28 0 0 0] with

    # Delete all files that are not .msg or .bf
    # print("Deleting all files that are not .msg or .bf")
    # for folder in [mod_folder]:
        # for file in os.scandir(folder):
        # if file.is_file() and not file.name.lower().endswith((".msg", ".bf")):
        # os.remove(file.path)

    # Copy all the files and folders from mod_folder to output_folder
    print("Copying all the files and folders from mod_folder to output_folder")
    for folder in [mod_folder]:
        for file in os.scandir(folder):
            if file.is_file():
                shutil.copy2(file.path, output_folder)
            if file.is_dir():
                shutil.copytree(file.path, os.path.join(
                    output_folder, file.name))

    # process all the .msg files in the output folder
    print("Processing all the .msg files in the output folder")
    for folder_name, subfolders, files in os.walk(output_folder):
        for file in files:
            if file.endswith(".msg"):
                process_msg(os.path.join(folder_name, file))

    print("Done!")
    enable_button()
    tk.messagebox.showinfo("Finished", "Replaced all the names in the mod!")


# Mod folder
mod_folder_label = ttk.Label(root, text="Mod folder:", background="#242424")
mod_folder_entry = ttk.Entry(root, width=60)
mod_folder_button = ttk.Button(root, text="Browse", command=browse_mod_folder)
mod_folder_entry.insert(0, mod_folder)  # Insert the saved value

mod_folder_label.grid(row=0, column=0, padx=5, pady=10)
mod_folder_entry.grid(row=0, column=1, padx=5, pady=10)
mod_folder_button.grid(row=0, column=2, padx=5, pady=10)

# Language folder
language_folder_label = ttk.Label(
    root, text="Language folder:", background="#242424")
language_folder_entry = ttk.Entry(root, width=60)
language_folder_button = ttk.Button(
    root, text="Browse", command=browse_language_folder)
# language_folder_entry.insert(0, language_folder)  # Insert the saved value
# Disable the language folder entry and button
language_folder_entry.config(state="disabled")
language_folder_button.config(state="disabled")

language_folder_label.grid(row=1, column=0, padx=5, pady=10)
language_folder_entry.grid(row=1, column=1, padx=5, pady=10)
language_folder_button.grid(row=1, column=2, padx=5, pady=10)

# Output folder
output_folder_label = ttk.Label(
    root, text="Output folder:", background="#242424")
output_folder_entry = ttk.Entry(root, width=60)
output_folder_button = ttk.Button(
    root, text="Browse", command=browse_output_folder)
output_folder_entry.insert(0, output_folder)  # Insert the saved value

output_folder_label.grid(row=2, column=0, padx=5, pady=10)
output_folder_entry.grid(row=2, column=1, padx=5, pady=10)
output_folder_button.grid(row=2, column=2, padx=5, pady=10)

# Run button
run_button = ttk.Button(root, text="Replace", command=run_program)
run_button.grid(row=4, column=1, padx=0, pady=15)


def save_config():
    # Save the values in the config file
    config['Folders'] = {
        'mod_folder': mod_folder_entry.get(),
        # 'language_folder': language_folder_entry.get(),
        'output_folder': output_folder_entry.get(),
        'game': game
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def save_log_on_file():
    # Save the log box on a file
    with open('log.txt', 'w') as f:
        f.write(log_box.get("1.0", tk.END))


def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        save_config()
        root.destroy()


# Run the on_closing function when the window is closed
root.protocol("WM_DELETE_WINDOW", on_closing)

sv_ttk.set_theme("dark")

# set theme dark in cttk
customtkinter.set_appearance_mode("dark")

root.iconbitmap("dependencies/test2.ico")

root.title("Persona Q2 SET N")

root.mainloop()