import os
import subprocess

# Define the path to PersonaEditorCMD.exe
personaeditor_path = 'PersonaEditorCMD.exe'  # Ajusta esta línea si el ejecutable está en otra ruta

# Get the current working directory
base_dir = os.getcwd()

# Walk through all files in the directory and subdirectories
for root, dirs, files in os.walk(base_dir):
    for file in files:
        # Construct the full file path
        input_file_path = os.path.join(root, file)
        
        # Construct the command to execute
        command = [personaeditor_path, input_file_path, '-impall', '-save', input_file_path]
        
        # Execute the command
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Executed: {' '.join(command)}\nOutput: {result.stdout.decode()}\n")
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute: {' '.join(command)}\nError: {e.stderr.decode()}\n")
