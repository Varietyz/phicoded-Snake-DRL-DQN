import os

def collect_all_files_content(start_path, exclude_entries=None, output_file='all_contents.txt'):
    """
    Recursively collects content of all files under start_path (excluding specified entries)
    and writes all content to a single output file, separated by file path headers.
    """
    if exclude_entries is None:
        exclude_entries = [
            'desktop.ini', 'node_modules', '.git', 'dist', '.venv',
            'Image-ExifTool-13.26', 'resources', 'Navigation.md',
            '.gitignore', '.gitattributes', 'package-lock.json',
            'update_readme.py', '__pycache__', 'content_extract.py', 'score.json', 'ai_model.json',  'README.md',
            'requirements.txt', 'LICENSE', 'all_contents.txt', 'dqn_model.json', 'dqn_model.agent'
        ]

    def should_exclude(path):
        # Exclude if any excluded entry is part of path (folder or file)
        for excl in exclude_entries:
            if excl in path:
                return True
        return False

    collected_lines = []

    for root, dirs, files in os.walk(start_path):
        # Filter directories to avoid walking excluded ones
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]

        for filename in files:
            full_path = os.path.join(root, filename)
            if should_exclude(full_path):
                continue
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Add a header with file path to separate contents
                collected_lines.append(f"\n\n=== File: {os.path.relpath(full_path, start_path)} ===\n\n")
                collected_lines.append(content)
            except Exception as e:
                # Could be binary or unreadable file, skip or log
                collected_lines.append(f"\n\n=== File: {os.path.relpath(full_path, start_path)} ===\n")
                collected_lines.append(f"[Could not read file: {e}]\n")

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.writelines(collected_lines)

    print(f"All file contents collected into '{output_file}'.")

 
if __name__ == '__main__':
    current_directory = os.getcwd()
    collect_all_files_content(current_directory)
