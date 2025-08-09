<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

# φ PHICODE Engine
A custom Python runtime and import system that enables running code written in a symbolic, concise language called **PHICODE**. PHICODE replaces Python keywords and syntax with unique symbols, providing a compact and visually distinct alternative syntax layer on top of Python. 

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
```
├─ 📂 (φ)
│   ├─ 📂 ai
│   │   ├─ 📄 agent_plugin.φ
│   │   ├─ 📄 connector.φ
│   │   ├─ 📄 dqn_agent.φ
│   │   ├─ 📂 game
│   │   │   ├─ 📄 enhancements.φ
│   │   │   ├─ 📄 penalties.φ
│   │   │   └─ 📄 rewards.φ
│   │   ├─ 📄 simple_nn.φ
│   │   └─ 📄 __init__.φ
│   ├─ 📂 common
│   │   ├─ 📄 utils.φ
│   │   └─ 📄 __init__.φ
│   ├─ 📄 config.φ
│   ├─ 📂 core
│   │   ├─ 📄 food.φ
│   │   ├─ 📄 score.φ
│   │   ├─ 📄 snake.φ
│   │   └─ 📄 __init__.φ
│   ├─ 📂 data
│   │   ├─ 📄 dqn_model.agent
│   │   ├─ 🔧 dqn_model.json
│   │   └─ 🔧 score.json
│   ├─ 📄 main.φ
│   └─ 📂 ui
│       ├─ 📄 bonus_manager.φ
│       ├─ 📄 controller.φ
│       ├─ 📄 input_handler.φ
│       ├─ 📄 metrics.φ
│       ├─ 📄 renderer.φ
│       └─ 📄 __init__.φ
├─ ⚖️ LICENSE
├─ 📄 phicode-1.1.0.vsix
├─ 📂 phicode_engine
│   ├─ 📂 core
│   │   └─ 🐍 phicode_importer.py
│   ├─ 📂 map
│   │   ├─ 🐍 mapping.py
│   │   ├─ 🐍 __py→φ__.py
│   │   └─ 🐍 __φ→py__.py
│   ├─ 🐍 run.py
│   └─ 🐍 __init__.py
└─ 📘 README.md
```