import os
import re
from map.mapping import PYTHON_TO_PHICODE

INPUT_DIR = "__manual_conversion__/convert(py)"
OUTPUT_DIR = "__manual_conversion__/converted(φ)"

def remove_comments(text):
    def process_line(line):
        original_line_is_empty = (line.strip() == "")
        
        hash_positions = [m.start() for m in re.finditer(r'#', line)]
        if not hash_positions:
            return line  # no comment, keep as is
        
        for pos in hash_positions:
            before = line[pos-1] if pos > 0 else None
            after = line[pos+1] if pos+1 < len(line) else None
            
            before_space = before is None or before.isspace()
            after_space = after is None or after.isspace()
            after_digit = after is not None and after.isdigit()
            
            # Apply rules in order:
            # 1) If no space before and no space after # => keep entire line (not a comment)
            if not before_space and not after_space:
                continue  # do nothing, keep line
            
            # 2) If no space before and after is digit (e.g., foo#123) => keep line
            if not before_space and after_digit:
                continue  # keep
            
            # 3) If space before and after is digit (e.g., foo #123) => keep line
            if before_space and after_digit:
                continue  # keep
            
            # 4) If space before and after is space or end of line (e.g., foo # comment) => cut comment
            if before_space and (after_space or after is None):
                new_line = line[:pos].rstrip()
                if new_line == "" and not original_line_is_empty:
                    return None  # remove line if empty after trimming
                return new_line
            
            # 5) If space before and after is letter or non-digit non-space (e.g., foo #abc) => cut comment
            if before_space and after is not None and not after_space and not after_digit:
                new_line = line[:pos].rstrip()
                if new_line == "" and not original_line_is_empty:
                    return None
                return new_line
        
        return line  # no comment removed, keep original

    lines = text.splitlines()
    cleaned_lines = []
    for line in lines:
        new_line = process_line(line)
        if new_line is not None:
            cleaned_lines.append(new_line)
    return '\n'.join(cleaned_lines)

def translate_python_to_phicode(text):
    text = remove_comments(text)
    pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in PYTHON_TO_PHICODE.keys()) + r')\b')
    
    def replacer(match):
        return PYTHON_TO_PHICODE[match.group(0)]
    
    return pattern.sub(replacer, text)


def convert_files():
    for root, dirs, files in os.walk(INPUT_DIR):
        # Compute relative path from input root to current root
        rel_path = os.path.relpath(root, INPUT_DIR)
        # Compute corresponding output directory path
        out_dir = os.path.join(OUTPUT_DIR, rel_path)
        
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        
        for filename in files:
            if filename.endswith(".py"):
                input_path = os.path.join(root, filename)
                with open(input_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                converted_content = translate_python_to_phicode(content)
                
                output_filename = os.path.splitext(filename)[0] + ".φ"
                output_path = os.path.join(out_dir, output_filename)
                
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(converted_content)
                
                print(f"Converted (φ) {input_path} -> {output_path}")

if __name__ == "__main__":
    convert_files()
