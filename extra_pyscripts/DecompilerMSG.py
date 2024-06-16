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

from tkinter import filedialog


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
if os.path.isfile('config_decom.ini'):
    config.read('config_decom.ini')
else:
    # If it doesn't exist, create it with default values
    config['Folders'] = {'mod_folder': '',
                         'output_folder': '', 'game': 'Persona Q2'}
    with open('config_decom.ini', 'w') as configfile:
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


def enable_button():
    run_button.config(state="normal")
    dropdown.config(state="normal")
    mod_folder_button.config(state="normal")
    # language_folder_button.config(state="normal")
    output_folder_button.config(state="normal")
    mod_folder_entry.config(state="normal")
    # language_folder_entry.config(state="normal")
    output_folder_entry.config(state="normal")


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

    def ASCDecompile(input_file_path):
        input_file_name = os.path.basename(input_file_path)
        if game == "Persona 5 Royal":

            # print(f"Decompiling BMD file: {input_file_name} with P5R library")
            subprocess.run([atlus_script_tools_path, input_file_path,
                            "-Decompiled", "-Library", "P5R", "-Encoding", "P5"])
        elif game == "Persona 5":
            # print(f"Decompiling BMD file: {input_file_name} with P5 library")
            subprocess.run([atlus_script_tools_path, input_file_path,
                            "-Decompiled", "-Library", "P5", "-Encoding", "P5"])
        elif game == "Persona Q2":
            # print(f"Decompiling BMD file: {input_file_name} with PQ2 library")
            subprocess.run([atlus_script_tools_path, input_file_path,
                            "-Decompiled", "-Library", "PQ2", "-Encoding", "SJ"])

    # PersonaEditor functions
    def PEExport(input_file_path):
        subprocess.run([personaeditor_path, input_file_path, '-expall'])

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

    # Export all the .bmd files in the "Output" folder with PersonaEditor
    print("Exporting all the .bmd files in the Output folder")
    for root, dirs, files in os.walk(output_folder):
        for msg_file in files:
            if msg_file.lower().endswith(('.bf', '.pak', '.pac')):
                # print(f"Exporting {msg_file}")
                PEExport(os.path.join(root, msg_file))

    # print("Decomp all the .bmd files")
    for root, dirs, files in os.walk(output_folder):
        for msg_file in files:
            if msg_file.lower().endswith('.bmd'):
                # print(f"Decomp {msg_file}")
                ASCDecompile(os.path.join(root, msg_file))

    # Change all the endwith .bmd.bmd to .bmd
    # print("Renaming all the .bmd.bmd files to .bmd")
    # for root, dirs, files in os.walk(output_folder):
    #     for name in files:
    #         if name.lower().endswith('.bmd.bmd'):
    #             old_path = os.path.join(root, name)
    #             new_path = os.path.join(root, name[:-8] + ".bmd")
                # print(f"Renaming {old_path} to {new_path}")
                # try:
                #     os.rename(old_path, new_path)
                # except FileExistsError:
                # print(f"Skipping {old_path} as {new_path} already exists")
                # continue

    # Import all .bf files in the "Output" folder with PEImport
    # print("Importing all the .bf files in the Output folder")
    # for root, dirs, files in os.walk(output_folder):
    #     for mod_file in files:
    #         if mod_file.lower().endswith('.bf'):
    #             mod_file_path = os.path.join(root, mod_file)
                # print(f"Importing {mod_file} in {root}")
                # PEImport(mod_file_path)
            # mod_file_name_new = mod_file.split('.')[0]

    # Delete all .msg files in the "Output" folder
    print("Deleting all the .h files in the Output folder")
    for root, dirs, files in os.walk(output_folder):
        for mod_file in files:
            if mod_file.lower().endswith('.h'):
                mod_file_path = os.path.join(root, mod_file)
                print(f"Deleting {mod_file_path}")
                os.remove(mod_file_path)

    def delete_files_not_in_list(folder_path, files_list):
        # Make a list with all the files in the folder including the ones in the subfolders
        Del_files = []
        for root, dirs, files in os.walk(folder_path):
            for name in files:
                Del_files.append(os.path.join(root, name))
        Mod_List_Keep = []
        for i in range(len(files_list)):
            Mod_List_Keep.append(
                folder_path + files_list[i])
        # Delete all lines from Del_files that are in Mod_List_Keep
        for i in range(len(Mod_List_Keep)):
            for j in range(len(Del_files)):
                if Mod_List_Keep[i].lower() == Del_files[j].lower():
                    Del_files[j] = ""
        # Delete all the empty lines
        while "" in Del_files:
            Del_files.remove("")
        # Delete the files that are left in the keep_files list
        for file in Del_files:
            try:
                # print(f"Deleting {file}")
                os.remove(file)
            except FileNotFoundError:
                # print(f"Skipping {file} as it doesn't exist")
                continue

    # delete_files_not_in_list(output_folder, mod_files_list)
    # delete_files_not_in_list(mod_folder, mod_files_list)

    def delete_empty_folders(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in dirs:
                full_path = os.path.join(root, name)
                if not os.listdir(full_path):  # check if directory is empty
                    os.rmdir(full_path)
                else:
                    # recursively delete all files and subfolders
                    delete_empty_folders(full_path)

    # delete_empty_folders(output_folder)
    # delete_empty_folders(mod_folder)

    print("Done!")
    enable_button()
    tk.messagebox.showinfo("Finished", "Replaced all the names in the mod!")


# Mod folder
mod_folder_label = ttk.Label(
    root, text="Original folder:", background="#242424")
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

    with open('config_decom.ini', 'w') as configfile:
        config.write(configfile)


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

root.title("Persona Q2 MSG Decompiler")

root.mainloop()
