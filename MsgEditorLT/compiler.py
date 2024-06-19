import os
import subprocess
import shutil
import logging

logging.basicConfig(level=logging.INFO)

mod_folder = "imported"
output_folder = "compiled"
personaeditor_path = os.path.join('dependencies', 'personaeditor', 'personaeditorcmd.exe')
atlus_script_tools_path = os.path.join("dependencies", "atlusscripttools", "AtlusScriptCompiler.exe")

def ASCCompile(input_file_path):
    input_file_name = os.path.basename(input_file_path)
    logging.info(f"Compiling BMD file: {input_file_name} with PQ2 library")
    output_file_path = os.path.splitext(input_file_path)[0] + '.bmd'
    subprocess.run([atlus_script_tools_path, input_file_path, "-Out", output_file_path, "-Compile", "-OutFormat", "V1", "-Library", "PQ2", "-Encoding", "SJ"])

def PEImport(input_file_path):
    logging.info(f"Importing Persona Editor file: {input_file_path}")
    subprocess.run([personaeditor_path, input_file_path, '-impall', '-save', input_file_path])

def delete_files_not_in_list(folder_path, files_list):
    Del_files = []
    for root, dirs, files in os.walk(folder_path):
        for name in files:
            Del_files.append(os.path.join(root, name))
    Mod_List_Keep = [folder_path + file for file in files_list]
    Del_files = [file for file in Del_files if file.lower() not in map(str.lower, Mod_List_Keep)]
    for file in Del_files:
        try:
            os.remove(file)
            logging.info(f"Deleted file: {file}")
        except FileNotFoundError:
            continue

def delete_empty_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            full_path = os.path.join(root, name)
            if not os.listdir(full_path):
                os.rmdir(full_path)
                logging.info(f"Deleted empty folder: {full_path}")
            else:
                delete_empty_folders(full_path)

def run_program(mod_folder, output_folder):
    mod_files_list = []
    for root, dirs, files in os.walk(mod_folder):
        for file in files:
            path = os.path.join(root, file)
            mod_files_list.append(path)

    mod_files_list = [x.replace(mod_folder, '') for x in mod_files_list]

    logging.info("Copying all the files and folders from mod_folder to output_folder")
    for folder in [mod_folder]:
        for file in os.scandir(folder):
            if file.is_file():
                shutil.copy2(file.path, output_folder)
                logging.info(f"Copied file: {file.path} to {output_folder}")
            if file.is_dir():
                shutil.copytree(file.path, os.path.join(output_folder, file.name))
                logging.info(f"Copied folder: {file.path} to {os.path.join(output_folder, file.name)}")

    logging.info("Compiling all the .msg files")
    for root, dirs, files in os.walk(output_folder):
        for msg_file in files:
            if msg_file.lower().endswith('.msg'):
                ASCCompile(os.path.join(root, msg_file))

    logging.info("Renaming all the .bmd.bmd files to .bmd")
    for root, dirs, files in os.walk(output_folder):
        for name in files:
            if name.lower().endswith('.bmd.bmd'):
                old_path = os.path.join(root, name)
                new_path = os.path.join(root, name[:-8] + ".bmd")
                try:
                    os.rename(old_path, new_path)
                    logging.info(f"Renamed file: {old_path} to {new_path}")
                except FileExistsError:
                    os.remove(new_path)
                    os.rename(old_path, new_path)
                    logging.info(f"Renamed and replaced existing file: {old_path} to {new_path}")

    logging.info("Importing all the .bf files in the Output folder")
    for root, dirs, files in os.walk(output_folder):
        for mod_file in files:
            if mod_file.lower().endswith('.bf'):
                mod_file_path = os.path.join(root, mod_file)
                PEImport(mod_file_path)

    logging.info("Deleting all the .msg files in the Output folder")
    for root, dirs, files in os.walk(output_folder):
        for mod_file in files:
            if mod_file.lower().endswith('.msg'):
                mod_file_path = os.path.join(root, mod_file)
                os.remove(mod_file_path)
                logging.info(f"Deleted file: {mod_file_path}")

    delete_files_not_in_list(mod_folder, mod_files_list)
    delete_empty_folders(mod_folder)

    logging.info("Done!")

if __name__ == "__main__":
    run_program(mod_folder, output_folder)
