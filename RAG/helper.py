import json
import os
import re

def read_content(file):
    try:
        with open(file,'r',encoding='utf-8') as f:
            content=f.read()
        #print(f"Successfully read data from '{file}'")
        return content
    except FileNotFoundError:
       # print(f"Error: Input file '{file}' not found.")
        exit(1)
    except IOError as e:
        #print(f"Error: Unable to read file '{file}'. Details: {e}")
        exit(1)


def write_content(file,content):
    try:
        with open(file,'w',encoding='utf-8') as f:
            f.write(content)
        #print(f"Successfully write data to '{file}'")
    except IOError as e:
        #print(f"Error: Unable to write file '{file}'. Details: {e}")
        exit(1)
    
def load_json(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        #print(f"Successfully load json data from '{file}'")     
        return json_data
    except FileNotFoundError:
        #print(f"Error: Input file '{file}' not found.")
        exit(1)
    except json.JSONDecodeError:
        #print(f"Error: Input file '{file}' is not valid JSON.")
        exit(1)


def json_dump(file,content):
    try:
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2)
        #print(f"Successfully dump json data to '{file}'")
    except IOError:
        #print(f"Error: Could not dump to output file '{file}'")
        exit(1)


def save_context(file_path,context):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(context, f, ensure_ascii=False, indent=4)

def load_context(file_path):
    if not os.path.exists(file_path):
        print(f'The conversation context information for {file_path} does not exist.')
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        print(f'Load conversation context from {file_path}')
        return json.load(f)


