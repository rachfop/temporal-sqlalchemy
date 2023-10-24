import argparse
import os

import pyperclip

folder_path = "."  # Replace with the path to your folder
file_contents = []

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="Input file")
parser.add_argument("--output", type=str, help="Output file")
args = parser.parse_args()

if args.file:
    with open(args.file, "r") as f:
        file_contents.append("```python\n")
        file_contents.append(f"#{args.file}\n")
        file_contents.append(f.read())
        file_contents.append("\n```\n")
else:
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".py") and file_name != "clippy.py":
            with open(os.path.join(folder_path, file_name), "r") as f:
                file_contents.append("```python\n")
                file_contents.append(f"#{file_name}\n")
                file_contents.append(f.read())
                file_contents.append("\n```\n")
output_text = "".join(file_contents)

if args.output:
    with open(args.output, "w") as f:
        f.write(output_text)

clipboard_text = "".join(file_contents)
password = str(pyperclip.copy(clipboard_text))
print(clipboard_text)
