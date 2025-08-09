<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

# 🐍 PHICODE Snake Game

![PHICODE Logo](logo.png)

A classic Snake game implemented in PHICODE - a symbolic Python variant using expressive Unicode glyphs. Features AI integration with deep Q-learning for autonomous gameplay.

## 🌟 Features

- **PHICODE Implementation**: Entirely written in `.φ` files using symbolic Python syntax
- **Dual Control Modes**:
  - Traditional keyboard controls
  - AI agent with deep reinforcement learning
- **Game Enhancements**:
  - Bonus food with time-limited rewards
  - Progressive speed increase
  - Score tracking with persistent high scores
- **Modular Architecture**: Clean separation of game logic, rendering, and AI components

## 📦 Installation

1. Install the PHICODE runtime:
   ```bash
   pip install phicode
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/Varietyz/phicoded-Snake-DRL-DQN
   cd phicode-snake
   ```

## 🚀 Usage

Run the game:
```bash
phicode (φ)/main.φ
```
or if running from path (φ)
```bash
phicode # phicode ran without arguments will run main.φ
```
### Control Options:
- **Human Player**: Arrow keys (↑ ↓ ← →)
- **AI Mode**: Automatically controlled by the DQN agent

## 🧠 AI Architecture

The game features a deep Q-network (DQN) agent with:
- State preprocessing for snake position, food location, and danger detection
- Experience replay buffer
- Target network synchronization
- Custom reward shaping:
  ```φ
  REWARDS_CONFIG = {
      "ate_food": 250.0,
      "ate_bonus_food": 1000.0,
      "distance_to_food_delta_positive": 15.0,
      "distance_to_food_delta_negative": 30.0,
      "survival": 0.8,
      "danger_penalty_per_unit": 3.0
  }
  ```

## 🖥️ Technical Highlights

- **PHICODE-Python Interop**: Demonstrates seamless integration between symbolic and standard Python
- **Custom Neural Network**: Implemented in PHICODE (`simple_nn.φ`)
- **Persistent Learning**: Saves/loads model weights between sessions
- **Visual Feedback**: Real-time rendering of game state and metrics

## 🛠️ Development

This project includes a VS Code extension for PHICODE development:
[GitHub Repository](https://github.com/Varietyz/phicode-vscode-extension)

1. **Install the Extension**:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Click "Install from VSIX" and select `phicode-extension.vsix`

2. **Features**:
   - Syntax highlighting for `.φ` files
   - PHICODE ⇄ Python conversion
   - Symbol autocompletion
   - Breadcrumb navigation
   - Code formatting
   - Linting and error checking
   - Symbolic info tooltips
   - Copilot support

3. **Usage**:
   - Right-click any `.φ` file for conversion options
   - Use command palette `(Ctrl+Shift+P)` for:
		- Convert Python to PHICODE: `phicode.convertPythonToPhicode`
			- Transforms .py files to .φ with symbolic operators
		- Convert PHICODE to Python: `phicode.convertPhicodeToPython`
			- Reverts .φ files back to standard Python syntax


## 📂 Project Structure
```
├─ 📂 (φ)
│   ├─ 📂 ai
│   │   ├─ 🔱 agent_plugin.φ
│   │   ├─ 🔱 connector.φ
│   │   ├─ 🔱 dqn_agent.φ
│   │   ├─ 📂 game
│   │   │   ├─ 🔱 enhancements.φ
│   │   │   ├─ 🔱 penalties.φ
│   │   │   └─ 🔱 rewards.φ
│   │   ├─ 🔱 simple_nn.φ
│   │   └─ 🔱 __init__.φ
│   ├─ 📂 common
│   │   ├─ 🔱 utils.φ
│   │   └─ 🔱 __init__.φ
│   ├─ 🔱 config.φ
│   ├─ 📂 core
│   │   ├─ 🔱 food.φ
│   │   ├─ 🔱 score.φ
│   │   ├─ 🔱 snake.φ
│   │   └─ 🔱 __init__.φ
│   ├─ 📂 data
│   │   ├─ 🤖 dqn_model.agent
│   │   ├─ 🔧 dqn_model.json
│   │   └─ 🔧 score.json
│   ├─ 🔱 main.φ
│   └─ 📂 ui
│       ├─ 🔱 bonus_manager.φ
│       ├─ 🔱 controller.φ
│       ├─ 🔱 input_handler.φ
│       ├─ 🔱 metrics.φ
│       ├─ 🔱 renderer.φ
│       └─ 🔱 __init__.φ
├─ ⚖️ LICENSE
├─ 🖼️ logo.png
├─ 🔌 phicode-extension.vsix
└─ 📘 README.md
```