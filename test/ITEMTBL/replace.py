import csv

def read_replacements_from_csv(csv_file_path):
    replacements = {}
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) == 2:
                search, replace = row
                replacements[search.strip()] = replace.strip()
    return replacements

def replace_lines_in_text_file(text_file_path, replacements):
    with open(text_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line in replacements:
            new_lines.append(replacements[stripped_line] + '\n')
        else:
            new_lines.append(line)

    with open(text_file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

def main():
    csv_file_path = 'Q1items.csv'
    text_file_path = 'q2tbl - replacements.txt'

    replacements = read_replacements_from_csv(csv_file_path)
    replace_lines_in_text_file(text_file_path, replacements)

if __name__ == '__main__':
    main()
