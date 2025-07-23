# FletGeneratorPassword

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/mihaiapostol14/FletGeneratorPassword?style=for-the-badge&logo=github)](https://github.com/mihaiapostol14/FletGeneratorPassword/stargazers)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/mihaiapostol14/FletGeneratorPassword?style=for-the-badge&logo=git&logoColor=white)](https://github.com/mihaiapostol14/FletGeneratorPassword/commits/main)

**A cryptographically secure desktop password generator built with Flet & Python**

[Features](#-features) • [Installation](#-installation--setup) • [Usage](#-usage) • [Architecture](#-architecture--tech-stack)

</div>

---

## 📸 Preview

<div align="center">

![FletGeneratorPassword Preview](https://github.com/mihaiapostol14/FletGeneratorPassword/blob/fc38fe43fc8770bff15076d34bb85ae1d82930d5/assets/preview.png)

</div>

---

## ⚡ Quick Start

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

| Tool | Version | Download |
|------|---------|----------|
| **Python** | 3.8+ | [python.org](https://www.python.org/downloads/) |
| **pip** | Latest | *Included with Python* |
| **git** | Latest | [git-scm.com](https://git-scm.com/) |
| **venv** | Built-in | [Python venv docs](https://docs.python.org/3/library/venv.html) |

---

## 🚀 Installation & Setup

### Step 1: Clone & Navigate

```bash
git clone https://github.com/mihaiapostol14/FletGeneratorPassword.git
cd FletGeneratorPassword
```

### Step 2: Create Virtual Environment

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Upgrade pip & Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python generator.py
```

---

## 📂 Project Structure

```
FletGeneratorPassword/
├── 📁 assets/
│   ├── 📄 preview.png              # UI preview screenshot
│   └── 📁 icon/
│       └── 🎨 generator.ico        # Application icon
│
├── 🐍 generator.py                 # Main application (Flet GUI + Logic)
├── 📋 requirements.txt              # Python dependencies
├── 📖 README.md                     # This file
└── 📜 LICENSE                       # MIT License
```

---

## ✨ Features

- **🔐 Cryptographically Secure** — Uses Python's `secrets` module for true randomness
- **🎛️ Flexible Character Sets** — Choose from Letters, Numbers, Symbols, or combinations
- **🔢 Configurable Length** — Generate passwords from 2 to 2,048 characters
- **📋 One-Click Copy** — Copy-to-clipboard with success notification
- **⚡ Lightweight & Fast** — Single-file GUI application with minimal overhead
- **🖥️ Cross-Platform** — Works on Windows, macOS, and Linux
- **🎨 Modern UI** — Built with Flet for a sleek, responsive interface

---

## 🏗️ Architecture & Tech Stack

```
┌─────────────────────────────────────────────┐
│         FletGeneratorPassword               │
├─────────────────────────────────────────────┤
│                   UI Layer                  │
│  (Flet Framework - Cross-platform GUI)     │
├─────────────────────────────────────────────┤
│                 Logic Layer                 │
│   • PasswordGenerator Class                 │
│   • Async event handlers                    │
│   • Input validation & error handling       │
├─────────────────────────────────────────────┤
│              Core Dependencies              │
│   • secrets (cryptographic randomness)     │
│   • string (character sets)                │
│   • flet (UI framework)                    │
└─────────────────────────────────────────────┘
```

### Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python 3.8+ | Core application logic |
| **GUI Framework** | Flet 0.86.2+ | Cross-platform desktop UI |
| **Randomness** | `secrets` (stdlib) | Cryptographically secure generation |
| **Character Sets** | `string` (stdlib) | Pre-defined character pools |
| **Deployment** | Flet-Desktop | Package as standalone executable |

---

## 🎮 Usage

1. **Launch the app** → `python generator.py`
2. **Set password length** → Enter desired length (2-2048)
3. **Choose character set** → Select from dropdown:
   - Letters (A-Z, a-z)
   - Numbers (0-9)
   - Symbols (!@#$%^&*)
   - Letters + Numbers
   - All Characters (mixed)
4. **Generate password** → Click button or press `Enter`
5. **Copy password** → Click the copy icon (clipboard notification appears)

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Generate password |
| `Ctrl+C` | Copy password (copy button) |

---

## 🔍 Code Quality & Security

### ✅ Best Practices Implemented

- **Secure Randomness** — `secrets.choice()` for cryptographic randomness (CSPRNG)
- **Input Validation** — Length bounds (2-2048) with error messages
- **Exception Handling** — Try-catch blocks for clipboard and input operations
- **UI Feedback** — SnackBar notifications for user actions

### ⚠️ Recommended Improvements

- [ ] Add module and class docstrings following PEP 257
- [ ] Implement type hints (especially return types)
- [ ] Replace `print()` with `logging` module
- [ ] Move magic numbers to module-level constants
- [ ] Add unit tests for password generation logic
- [ ] Trim `requirements.txt` to runtime dependencies only
- [ ] Add GitHub Actions CI/CD pipeline
- [ ] Consider clipboard auto-clear for security

---

## 🧪 Testing & CI/CD

### Local Testing

```bash
# Install test dependencies
pip install pytest pytest-asyncio pylint black

# Run linter
pylint generator.py

# Format code
black generator.py
```

### Future: Automated Testing

```bash
# Once tests are added
pytest tests/
```

---

## 📦 Packaging for Desktop

To create a standalone executable:

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --icon=assets/icon/generator.ico generator.py
```

Executable will be in the `dist/` folder.

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. **Fork** the repository
2. **Create a feature branch** → `git checkout -b feature/your-feature`
3. **Commit changes** → `git commit -m "feat: add your feature"`
4. **Push to branch** → `git push origin feature/your-feature`
5. **Open a Pull Request** → Describe your changes clearly

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions and classes
- Include type hints for function parameters and returns
- Test your changes before submitting PR
- Update README if adding new features

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Mihai Apostol**
- GitHub: [@mihaiapostol14](https://github.com/mihaiapostol14)

---

## 🙏 Acknowledgments

- [Flet Framework](https://flet.dev/) — For the elegant cross-platform GUI framework
- [Python Secrets Module](https://docs.python.org/3/library/secrets.html) — For cryptographically secure randomness
- Community feedback and contributions

---

## 📞 Support & Feedback

Have suggestions or found a bug?

- 🐛 **Report a bug** → [Open an issue](https://github.com/mihaiapostol14/FletGeneratorPassword/issues)
- 💡 **Suggest a feature** → [Discussions](https://github.com/mihaiapostol14/FletGeneratorPassword/discussions)
- ⭐ **Show support** → [Star the repo](https://github.com/mihaiapostol14/FletGeneratorPassword)

---

<div align="center">

**Made with ❤️ by Mihai Apostol**

[⬆ Back to top](#-fletgeneratorpassword)

</div>
