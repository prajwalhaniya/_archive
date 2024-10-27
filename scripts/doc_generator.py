import os

def process_file_name(file_name):
    file_name = file_name.strip()
    underscore_index = file_name.find('_')

    if underscore_index != -1:
        processed_name = file_name[underscore_index + 1:]
    else:
        processed_name = file_name

    markdown_file = processed_name.endswith('.md')
    python_file = processed_name.endswith('.py')
    pdf_file = processed_name.endswith('.pdf')

    if markdown_file or python_file:
        processed_name = processed_name[:-3]

    if pdf_file:
        processed_name = processed_name[:-4]

    processed_name = processed_name.replace('_', ' ')

    return processed_name

def write_to_file(content):
    file_path = f'../README.md'

    with open(file_path, 'a') as file:
        file.write(content)

def delete_contents_from_readme(line_number):
    try:
        with open('../README.md', 'r') as file:
            lines = file.readlines()

        if line_number < 1 or line_number > len(lines):
            print("Invalid line number")
            return

        new_lines = lines[:line_number - 1]

        with open('../README.md', 'w') as file:
            file.writelines(new_lines)
            print(f"Contents from line {line_number} onward have been deleted from README.md.")
    except FileNotFoundError:
        print("README.md file is not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_files_in_directory(directory):
    try:
        entries = os.listdir(directory)
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
        if files:
            for file in files:
                file_name = process_file_name(file).capitalize()
                content = f'- [{file_name}]({directory[2:]}/{file}) \n'
                print(content)
                write_to_file(content)
    except FileNotFoundError:
         print("The directory '{}' does not exist.".format(directory))
    except Exception as e:
        print('An error occurred: {}'.format(e))


directories_list = [
    '../Research_papers',
    '../articles',
    '../ml',
    '../Algorithms',
    '../pattern_problems',
    '../data_structures/array/easy',
    '../data_structures/array/medium',
    '../data_structures/linked_list/easy'
]

line_number = 3
delete_contents_from_readme(line_number)

for index, directory in enumerate(directories_list):
    write_to_file(f'\n #### {directory[3:]} \n')
    list_files_in_directory(directory)