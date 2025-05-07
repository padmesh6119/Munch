#!/usr/bin/env python3

import base64, hashlib, sys, time, os, signal
from termcolor import colored
import itertools

# Handle Ctrl+C with graceful exit

def outro(signum, frame):
    print("\nExiting MUNCH. Thanks for using my tool!")
    sys.exit(0)

signal.signal(signal.SIGINT, outro)

# Atbash cipher
def atbash(text):
    result = ""
    for c in text:
        if c.isalpha():
            if c.isupper():
                result += chr(155 - ord(c))
            else:
                result += chr(219 - ord(c))
        else:
            result += c
    return result

# Generalized ROT for all outputs
def rot_cipher(text, n):
    result = ''
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + n) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + n) % 26 + 97)
        else:
            result += char
    return result

def rot_all_outputs(text):
    animate_text("\nROT Cipher Possibilities:")
    for i in range(1, 26):
        animate_line(f"ROT-{i}: {rot_cipher(text, i)}")
    return "\nIf one of these speaks to you, mission accomplished."

# Hash Generator
def hash_gen(text, algo):
    encoded = text.encode()
    return {
        "MD5": hashlib.md5(encoded).hexdigest(),
        "SHA1": hashlib.sha1(encoded).hexdigest(),
        "SHA224": hashlib.sha224(encoded).hexdigest(),
        "SHA256": hashlib.sha256(encoded).hexdigest(),
        "SHA384": hashlib.sha384(encoded).hexdigest(),
        "SHA512": hashlib.sha512(encoded).hexdigest()
    }.get(algo.upper(), "Unsupported hash type")

# Identify hash by length
def identify_hash(hash_str):
    length = len(hash_str)
    return {
        32: "MD5",
        40: "SHA1",
        56: "SHA224",
        64: "SHA256",
        96: "SHA384",
        128: "SHA512"
    }.get(length, "Unknown")

def animate_text(text):
    for char in text:
        print(colored(char, "green"), end='', flush=True)
        time.sleep(0.01)
    print()

def animate_line(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.005)
    print()

def loading_animation():
    frames = ['|', '/', '-', '\\']
    for _ in range(10):
        for frame in frames:
            sys.stdout.write(f"\r{colored('Processing ', 'green')}{frame}")
            sys.stdout.flush()
            time.sleep(0.05)
    print("\r", end="")

def show_menu():
    animate_text("\n+---------------------------------------+")
    animate_text("|                  MUNCH                 |")
    animate_text("+---------------------------------------+")
    print(colored("[1] Encode", "white"))
    print(colored("[2] Decode", "white"))
    print(colored("[3] Generate Hash", "white"))
    print(colored("[4] Identify Hash", "white"))
    print(colored("[5] Exit", "white"))

def encode_menu():
    return {
        "1": ("Base64", lambda x: base64.b64encode(x.encode()).decode()),
        "2": ("Base32", lambda x: base64.b32encode(x.encode()).decode()),
        "3": ("Hex", lambda x: x.encode().hex()),
        "4": ("Atbash", atbash),
        "5": ("ROT", rot_all_outputs)
    }

def decode_menu():
    return {
        "1": ("Base64", lambda x: base64.b64decode(x.encode()).decode()),
        "2": ("Base32", lambda x: base64.b32decode(x.encode()).decode()),
        "3": ("Hex", lambda x: bytes.fromhex(x).decode()),
        "4": ("Atbash", atbash),
        "5": ("ROT", rot_all_outputs)
    }

def run():
    while True:
        show_menu()
        choice = input(colored("Select an option: ", "green")).strip()
        print()
        if choice == '1':
            options = encode_menu()
            for k, v in options.items():
                animate_line(f"[{k}] {v[0]}")
            opt = input("Choose: ").strip()
            if opt in options:
                data = input("Enter text: ")
                loading_animation()
                print("\nResult:", colored(options[opt][1](data), "cyan"))
                animate_text("✓ Encoding complete! Keep it safe.")
        elif choice == '2':
            options = decode_menu()
            for k, v in options.items():
                animate_line(f"[{k}] {v[0]}")
            opt = input("Choose: ").strip()
            if opt in options:
                data = input("Enter text: ")
                try:
                    loading_animation()
                    print("\nResult:", colored(options[opt][1](data), "cyan"))
                    animate_text("✓ Decoding finished. Hope it helped!")
                except:
                    print(colored("Error decoding. Check input.\n", "red"))
        elif choice == '3':
            text = input("Enter text: ")
            print("Choose Hash Algorithm: [MD5, SHA1, SHA224, SHA256, SHA384, SHA512]")
            algo = input("Enter: ").strip()
            loading_animation()
            result = hash_gen(text, algo)
            print(colored(f"{algo.upper()}: ", "green") + colored(result, "white"))
            animate_text("✓ Your digital fingerprint is ready.")
        elif choice == '4':
            hash_input = input("Enter hash string to identify: ")
            loading_animation()
            result = identify_hash(hash_input)
            print(colored(f"Identified as: {result}", "cyan"))
            animate_text("✓ Hash classification done.")
            print(colored("Note: Only MD5, SHA1, SHA224, SHA256, SHA384, SHA512 are supported.\n", "yellow"))
        elif choice == '5':
            outro(None, None)
        else:
            print(colored("Invalid input. Try again.\n", "red"))

if __name__ == "__main__":
    run()

