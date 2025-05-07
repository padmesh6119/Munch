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

If all of em are installled , then 
   python3 munch.py 
to run and that's it

Have a good day
