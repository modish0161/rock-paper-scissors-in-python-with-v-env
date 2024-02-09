import os

def print_tree(directory, indent=''):
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path) and item not in ['venv', '.venv', '__pycache__', '.vscode']:
            print(indent + '|-- ' + item)
            print_tree(full_path, indent + '    ')
        elif os.path.isfile(full_path):
            print(indent + '|-- ' + item)

if __name__ == '__main__':
    print_tree('.')
