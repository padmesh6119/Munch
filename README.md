# 🧩 MUNCH

MUNCH is a command-line tool for basic encoding, decoding, and hashing. It's lightweight, animated, and just a bit cheeky. Think of it as a digital Swiss Army knife for text transformations.

---

## 🛠 What MUNCH Can Do

MUNCH offers 5 main functionalities:

1. **Encode** — Base64, Base32, Hex, Atbash, and ROT variations.
2. **Decode** — The reverse of the above.
3. **Generate Hashes** — Using popular algorithms like MD5, SHA1, SHA224, SHA256, SHA384, SHA512.
4. **Identify Hash** — Guess the hash type based on its length.
5. **Exit** — Gracefully quit the program.

---

## 📦 Ciphers and Hashing Explained

### 🔤 Atbash Cipher
A classic monoalphabetic cipher where `A ↔ Z`, `B ↔ Y`, etc. Works the same for lowercase.

### 🔁 ROT Cipher
ROT-N rotates letters by `N` positions. For example, ROT13 turns `A` into `N`, `B` into `O`, and so on. MUNCH shows all 25 possibilities for maximum flexibility.

### 🧬 Base64 / Base32 / Hex
- **Base64**: Commonly used in data transmission (email, web).
- **Base32**: Less compact but better for case-insensitive environments.
- **Hex**: Encodes binary data in hexadecimal (0-9, a-f).

### 🔐 Hashing
Hashes turn your text into fixed-length strings. MUNCH supports:
- `MD5` – Fast but not secure.
- `SHA1` – Better, but still broken.
- `SHA224`, `SHA256`, `SHA384`, `SHA512` – Stronger and widely used.

## Requirements
Before running MUNCH, ensure you have the following installed:

- **Python 3.x:** The program is written in Python, so you need Python 3.x installed.
- **termcolor library:** This Python library is used to add color to the terminal output.

### How to Install

1. **Install Python 3:**  
   MUNCH requires Python 3 to run. Download and install it from the [official Python website](https://www.python.org/downloads/) if it's not already installed.

2. **Install Dependencies:**
   Once Python 3 is installed, you need to install the required libraries.
   Open your terminal and run the following command to install the dependencies:
   ```bash
   pip install termcolor
## 🚧 Future Enhancements & Roadmap

As MUNCH matures, here are some powerful new features we're aiming to implement:

---

### 1. 🧬 Extended Hash Identification  
**Current Limitation:**  
MUNCH identifies hash types solely based on their character length. At present, it only supports:

- MD5
- SHA1
- SHA224
- SHA256
- SHA384
- SHA512

**Planned Upgrade:**
- Support for additional hashes such as:
  - SHA3 family
  - Whirlpool
  - Blake2, Blake3
  - RIPEMD
  - bcrypt, scrypt
- Smarter identification using entropy analysis and regex patterns.

---

### 2. 🔐 Enhanced ROT Cipher Support  
**Current Limitation:**  
- The ROT feature only includes ROT-1 to ROT-25 brute-force results.
- No direct input for a ROT-X number or support for ROT47.

**Planned Upgrade:**
- Allow user-defined ROT number for direct encoding/decoding.
- Add **ROT13 shortcut**.
- Introduce **ROT47**, which supports all printable ASCII characters.

---

### 3. 🎭 Cipher Expansion  
**Current Limitation:**  
- Encoding/Decoding options include: Base64, Base32, Hex, Atbash, and ROT.

**Planned Upgrade:**
- Add support for more classical ciphers:
  - Playfair Cipher
  - Affine Cipher
  - Rail Fence
  - Bacon’s Cipher
- Allow multi-layered encryption (e.g., Atbash + Base64).

---

### 4. 🎵 Audio Feedback (Fun Mode)  
**Concept:**  
Add simple space-themed sound effects for various tool actions.

- 🎶 Short tones for success, error, or input confirmation.
- Optional toggle for sound feedback (on/off mode).

---

### 5. 🧪 GUI/TUI Interface  
**Planned Upgrade:**
- Build a **Terminal UI (TUI)** using `rich` or `curses`.
- Option to create a GUI version using `Tkinter` or `PyQT`.

---

### 6. 🚀 Web Interface / API Support  
**Concept:**  
Expose MUNCH features via a simple **REST API** using Flask or FastAPI:

- Web-based interface
- Integration with external tools (like Discord bots or online analyzers)

---

### 7. 📂 File-Based Input/Output  
**Planned Upgrade:**
- Support for encoding/decoding text from `.txt` or binary files.
- Base64 encode images or documents directly from file path

Have a good day
