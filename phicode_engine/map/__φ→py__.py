import os
import re
from map.mapping import PHICODE_TO_PYTHON

INPUT_DIR = "__manual_conversion__/converted(φ)"
OUTPUT_DIR = "__manual_conversion__/reconstructed(py)"

def translate_phicode_to_python(text):
    pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in PHICODE_TO_PYTHON.keys()) + r')\b')
    
    def replacer(match):
        return PHICODE_TO_PYTHON[match.group(0)]
    
    return pattern.sub(replacer, text)


def convert_files():
    for root, dirs, files in os.walk(INPUT_DIR):
        rel_path = os.path.relpath(root, INPUT_DIR)
        out_dir = os.path.join(OUTPUT_DIR, rel_path)
        
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        
        for filename in files:
            if filename.endswith(".φ"):
                input_path = os.path.join(root, filename)
                with open(input_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                converted_content = translate_phicode_to_python(content)
                
                output_filename = os.path.splitext(filename)[0] + ".py"
                output_path = os.path.join(out_dir, output_filename)
                
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(converted_content)
                
                print(f"Reconstructed (.py) {input_path} -> {output_path}")


if __name__ == "__main__":
    convert_files()
