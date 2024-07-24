import os
import subprocess

# Define the command template
command_template = 'PersonaEditorCMD.exe "{}" -expall'

# Get the current working directory
base_dir = os.getcwd()

# Walk through all files in the directory and subdirectories
for root, dirs, files in os.walk(base_dir):
    for file in files:
        # Construct the full file path
        file_path = os.path.join(root, file)
        
        # Construct the command to execute
        command = command_template.format(file_path)
        
        # Execute the command
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Executed: {command}\nOutput: {result.stdout.decode()}\n")
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute: {command}\nError: {e.stderr.decode()}\n")
