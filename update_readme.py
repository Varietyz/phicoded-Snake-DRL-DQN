import os

def save_tree_structure(start_path, exclude_entries=None, output_file='README.md'):
	"""
	Recursively generates a tree structure of the directory contents starting from `start_path`
	and writes the output to a Markdown file wrapped in code fences.

	The output is enclosed within triple backticks (```) so that it renders as a formatted code block.
	A variety of emojis are used to represent different file types.

	Parameters:
	- start_path (str): The starting directory path.
	- exclude_entries (list, optional): Files or directories to exclude.
	- output_file (str, optional): The name of the output Markdown file.
	"""
	if exclude_entries is None:
		exclude_entries = [
			'desktop.ini',
			'node_modules',
			'.git',
			'dist',
			'.venv',
			'Image-ExifTool-13.26',
			'resources',
   			'Navigation.md',
			'.gitignore',
			'.gitattributes',
			'package-lock.json',
   			'update_readme.py',
      		'__pycache__',
			'all_contents.txt',
			'content_extract.py',
   			'__manual_conversion__'
		]

	file_emojis = {
		'.py': '🐍',
		'.js': '📜',
		'.json': '🔧',
		'.txt': '📄',
		'.md': '📝',
		'.html': '🌐',
		'.css': '🎨',
		'.jpg': '🖼️',
		'.jpeg': '🖼️',
		'.png': '🖼️',
		'.gif': '🖼️',
		'.ico': '🖼️',
		'.mp3': '🎵',
		'.wav': '🎵',
		'.mp4': '🎞️',
		'.pdf': '📕',
		'.gdoc': '🗄️',
		'.xlsx': '🧮',
		'.psd': '🖌️',
	}

	def get_file_emoji(filename):
		"""
		Returns an emoji representing the file based on text-based or extension-based mappings.
		"""
		filename_lower = filename.lower()

		text_mapping = {
			'readme': '📘',
			'license': '⚖️',
			'receipt': '🧾',
			'faq': '❓',
			'rules': '📖',
			'invitation': '💌',
			'agenda': '📅',
			'analytics': '📈',
			'brainstorming': '🧠',
			'insights': '🔎',
			'guidelines': 'ℹ️',
			'tools': '🛠️',
			'sponsor': '💵',
			'finished': '✅',
			'bot': '🤖',
			'data': '📊',
		}

		for pattern, emoji in text_mapping.items():
			if pattern in filename_lower:
				return emoji

		ext = os.path.splitext(filename)[1].lower()
		return file_emojis.get(ext, '📄')

	def walk_directory(directory, depth=0, prefix=''):
		"""
		Recursively walks the directory structure, building a list of strings representing
		each file and folder in a tree format.

		Parameters:
		- directory (str): The directory to traverse.
		- depth (int): The current recursion depth.
		- prefix (str): The string prefix for the current depth (used for formatting).

		Returns:
		- list of str: The formatted lines representing the tree structure.
		"""
		if any(excluded in directory for excluded in exclude_entries):
			return []

		tree_lines = []
		entries = os.listdir(directory)
		entries = [entry for entry in entries if entry not in exclude_entries]
		total_entries = len(entries)

		for idx, entry in enumerate(entries):
			full_path = os.path.join(directory, entry)
			is_last = idx == total_entries - 1
			symbol = '└─' if is_last else '├─'
			new_prefix = prefix + ('    ' if is_last else '│   ')

			if os.path.isdir(full_path):
				emoji = '📂'
				tree_lines.append(f'{prefix}{symbol} {emoji} {entry}')
				tree_lines.extend(walk_directory(full_path, depth + 1, new_prefix))
			else:
				emoji = get_file_emoji(entry)
				tree_lines.append(f'{prefix}{symbol} {emoji} {entry}')

		return tree_lines

	directory_structure = walk_directory(start_path)

	markdown_output = """

# φ PHICODE Engine 

**φ PHICODE Engine** is a custom Python runtime and import system that enables running code written in a symbolic, concise language called **PHICODE**. PHICODE replaces Python keywords and syntax with unique symbols, providing a compact and visually distinct alternative syntax layer on top of Python. 

---

## Features

* **Symbolic Syntax Mapping**
  Keywords and operators are mapped to unique Unicode symbols, creating a compact and expressive symbolic language.

* **On-the-fly PHICODE to Python Translation**
  The engine transparently converts PHICODE source files (`*.phicode`) into Python at import time, enabling direct execution of PHICODE modules.

* **Custom Importer Integration**
  Implements a Python `sys.meta_path` finder and loader that locates and loads PHICODE files as Python modules without modification to the Python interpreter.

* **Support for Modular Project Structure**
  Allows organizing PHICODE source files as modules and packages, supporting Python-style imports across PHICODE files.

* **Runtime Script for Easy Execution**
  Provides a `runtime.py` script that sets up the import system and runs a specified PHICODE module or automatically runs `main.phicode`.

---

## Installation

Clone the repository or place the PHICODE engine files in your project directory:

```
phicode-engine/
├── mapping.py
├── phicode_importer.py
├── runtime.py
└── (φ)/                # Your PHICODE source folder
    ├── main.phicode
    └── ...
```

---

## Usage

1. **Prepare Your PHICODE Source Files**
   Write your modules using PHICODE syntax with `.phicode` extensions inside your PHICODE source folder (default folder `(φ)`).

2. **Run the PHICODE Runtime**
   From your terminal, execute:

   ```bash
   python runtime.py
   ```

   This will automatically look for and run `main.phicode` in the source folder.

3. **Import PHICODE Modules as Usual**
   Inside your PHICODE files, use normal Python-style `import` statements (which map to PHICODE symbols) to organize and reuse code.

---

## PHICODE Syntax

PHICODE uses symbolic replacements for Python keywords and control flow, such as:

| Python   | PHICODE |
| -------- | ------- |
| `def`    | `ƒ`     |
| `if`     | `¿`     |
| `else`   | `⋄`     |
| `for`    | `∀`     |
| `return` | `⟲`     |
| `True`   | `✓`     |
| `False`  | `⊥`     |
| `None`   | `Ø`     |
| `import` | `⇒`     |

The full mapping is defined in `mapping.py`.

---

## Extending PHICODE

* You can add new symbols and mappings in `mapping.py`.
* The importer transparently handles decoding; no changes needed elsewhere.
* The runtime can be customized to support additional features or error handling.

---

## 📂 Current Project Structure
```\n""" + '\n'.join(directory_structure) + '\n```'

	with open(output_file, 'w', encoding='utf-8') as f:
		f.write(markdown_output)

	print(f'Folder structure has been saved to {output_file}')


if __name__ == '__main__':
	current_directory = os.getcwd()
	save_tree_structure(current_directory)
