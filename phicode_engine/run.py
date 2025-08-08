# run.py

import sys
import os
import traceback
from phicode_importer import install_phicode_importer

def main():
    # Default module to run
    module_name = "main"

    # φ is the default PHICODE source folder; adjust if needed
    phicode_src_folder = 'phicode_engine/(φ)'
    if not os.path.isdir(phicode_src_folder):
        print(f"PHICODE source folder not found: {phicode_src_folder}", file=sys.stderr)
        sys.exit(2)

    # Install the PHICODE import system
    install_phicode_importer(phicode_src_folder)

    print("Starting PHICODE runtime...")
    try:
        __import__(module_name)
        print("Imported main module successfully")
    except Exception as e:
        print(f"Error running module '{module_name}': {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(3)

if __name__ == "__main__":
    main()
