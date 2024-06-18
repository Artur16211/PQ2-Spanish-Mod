import os

def replace_dialog_in_files(msgs_dir, msgparams_dir, imported_dir):
    os.makedirs(imported_dir, exist_ok=True)
    
    for root, dirs, files in os.walk(msgs_dir):
        for file in files:
            if file.endswith('.msg'):
                msg_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, msgs_dir)
                
                params_file_path = os.path.join(msgparams_dir, relative_path, file)
                
                if os.path.exists(params_file_path):
                    with open(msg_file_path, 'r', encoding='utf-8') as source_file:
                        source_lines = source_file.readlines()
                    
                    with open(params_file_path, 'r', encoding='utf-8') as destination_file:
                        destination_lines = destination_file.readlines()
                    
                    # Replace {dialog} in the destination file with lines from the source file
                    for i, destination_line in enumerate(destination_lines):
                        if "{dialog}" in destination_line:
                            # Ensure the index is within the bounds of the source_lines
                            if i < len(source_lines):
                                source_line = source_lines[i].strip()
                                destination_lines[i] = destination_line.replace("{dialog}", source_line)
                    
                    imported_file_path = os.path.join(imported_dir, relative_path, file)
                    os.makedirs(os.path.dirname(imported_file_path), exist_ok=True)
                    
                    with open(imported_file_path, 'w', encoding='utf-8') as imported_file:
                        imported_file.writelines(destination_lines)
                else:
                    print(f"Corresponding params file not found for {msg_file_path}")
                    
msgs_dir = 'Data'
msgparams_dir = 'msgparams'
imported_dir = 'imported'

replace_dialog_in_files(msgs_dir, msgparams_dir, imported_dir)
